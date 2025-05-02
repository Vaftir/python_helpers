## Visão Geral

A classe **ConfigHandler** é responsável por gerenciar um arquivo de configuração em formato JSON. Ela permite:

* Carregar configurações de um arquivo.
* Recuperar seções específicas da configuração.
* Definir, deletar valores e salvar alterações de volta no arquivo.

---

## Estrutura do Projeto

```
.
├── config/
│   └── config.json         # Arquivo de configuração de exemplo
├── modules/
│   └── config/
│       ├── ConfigHandler.py
│       └── README.md       # Este arquivo
└── ...
```

---

## Dependências

* Python 3.6+
* Módulo padrão `json`

Nenhuma dependência externa adicional é necessária.

---

## Exemplo de `config.json`

Coloque este arquivo em `config/config.json`:

```json
{
    "api_keys": {
        "OPENAI_API_KEY": "sua_chave_aqui"
    },
    "services": {
        "criar_chamados_csc": {
            "url": "https://api.exemplo.com/chamados",
            "timeout": 30
        }
    },
    "users": {
        "gobots_user": {
            "username": "usuario_exemplo",
            "password": "senha_exemplo"
        }
    }
}
```

---

## Uso

1. **Importe** e crie uma instância, apontando para o caminho do seu JSON:

   ```python
   from modules.config.ConfigHandler import ConfigHandler

   config_handler = ConfigHandler('config/config.json')
   ```
2. **Carregue** ou **atualize** valores:

   ```python
   # Obter toda a seção 'services'
   services = config_handler.get_data('services')
   print("Serviços:", services)

   # Definir ou alterar um valor
   config_handler.set_config_value('new_key', {'foo': 'bar'})

   # Deletar um valor
   config_handler.delete_config_value('old_key')

   # Salvar alterações no arquivo
   config_handler.save_config()
   ```

---

## Estrutura da Classe `ConfigHandler`

```python
class ConfigHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()
        print(f"Instância de ConfigHandler criada com o arquivo {file_path}")

    def __del__(self):
        print(f"Instância de ConfigHandler com o arquivo {self.file_path} está sendo destruída.")

    def load_config(self):
        """
        Lê o arquivo JSON em UTF-8 e retorna o conteúdo como dict.
        Retorna None em caso de erro de leitura ou decodificação.
        """
        try:
            with open(self.file_path, 'r', encoding="UTF-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Config file {self.file_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the config file {self.file_path}.")
            return None

    def get_data(self, key):
        """
        Retorna o valor associado à chave, ou {} se não existir.
        """
        if self.config is None:
            return None
        return self.config.get(key, {})

    def save_config(self):
        """
        Salva o dict de configuração de volta ao arquivo em formato JSON com indentação.
        """
        try:
            with open(self.file_path, 'w', encoding="UTF-8") as file:
                json.dump(self.config, file, indent=4)
        except Exception as e:
            print(f"Error saving config to file {self.file_path}: {e}")

    def set_config_value(self, key, value):
        """
        Define ou atualiza o valor de uma chave na configuração.
        """
        if self.config is None:
            self.config = {}
        self.config[key] = value

    def delete_config_value(self, key):
        """
        Remove a chave (e seu valor) da configuração, se existir.
        """
        if self.config and key in self.config:
            del self.config[key]
```

