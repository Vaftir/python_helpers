## Visão Geral

A classe **ManipulaPastas** fornece métodos simples para criação de diretórios e limpeza de arquivos dentro deles. Ideal para preparar estruturas de pastas antes de processamentos, gravação de logs ou geração de resultados, garantindo que caminhos existam e estejam livres de arquivos antigos.

---

## Estrutura do Projeto

```
.
├── modules/
│   └── arquivo/
│       └── ManipulaPastas.py   # Classe para gerenciar pastas e arquivos
└── README.md                   # Este arquivo
```

---

## Dependências

* Python 3.6+

* Módulos da biblioteca padrão:
  
  * `os`
  * `glob`

Nenhuma instalação adicional é necessária.

---

## Uso

1. **Importe** e **instancie** a classe:
   
   ```python
   from modules.arquivo.ManipulaPastas import ManipulaPastas
   
   mp = ManipulaPastas()
   ```

2. **Crie** uma ou mais pastas (aninhadas ou não):
   
   ```python
   mp.cria_pastas('resultado', 'logs', 'logs/subpasta/pasta_x')
   # Saída:
   # Pasta criada: resultado
   # Pasta criada: logs
   # Pasta criada: logs/subpasta/pasta_x
   ```

3. **Limpe** todos os arquivos de um diretório, sem apagar a pasta:
   
   ```python
   mp.limpa_diretorio('logs')
   # Se houver arquivos:
   # Arquivo removido: logs/arquivo1.txt
   # ...
   # Se estiver vazio:
   # Pasta de logs vazia: logs
   # Se não existir:
   # Pasta não encontrada: logs
   ```

---

## Métodos Públicos

| Método                       | Descrição                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| `cria_pastas(*pastas)`       | Cria cada caminho informado, incluindo subpastas; pula se já existir.                     |
| `limpa_diretorio(diretorio)` | Remove todos os arquivos dentro do diretório informado; valida existência e tipo de path. |

---

## Detalhes de Implementação

```python
class ManipulaPastas:
    def __init__(self):
        pass

    def cria_pastas(self, *pastas):
        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)
                print(f'Pasta criada: {pasta}')
            else:
                print(f'Pasta já existe: {pasta}')

    def limpa_diretorio(self, diretorio):
        if os.path.exists(diretorio) and os.path.isdir(diretorio):
            files = glob.glob(os.path.join(diretorio, '*'))
            if files:
                for f in files:
                    os.remove(f)
                    print(f'Arquivo removido: {f}')
            else:
                print(f'Pasta de logs vazia: {diretorio}')
        else:
            print(f'Pasta não encontrada: {diretorio}')
```

* **`os.makedirs`**: cria todo o caminho de diretórios, se não existir.
* **`glob.glob`**: lista todos os arquivos no diretório informado.
* **`os.remove`**: apaga cada arquivo encontrado.

---

## Licença

MIT License. Sinta-se à vontade para adaptar e estender conforme suas necessidades!
