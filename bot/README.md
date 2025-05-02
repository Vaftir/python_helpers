
## Visão Geral

A classe **AssistenteChamado** tem como objetivo gerar automaticamente o texto de um chamado a partir de uma descrição fornecida pelo usuário. Para isso, ela utiliza o **LangChain** junto com o modelo **ChatOpenAI**, lendo configurações de API e parâmetros de geração a partir de um arquivo JSON de configuração.

---

## Estrutura do Projeto

```
.
├── config/
│   └── config.json         # Arquivo de configuração
├── modules/
│   └── config/
│       └── ConfigHandler.py
├── modules/
│   └── AssistenteChamado.py
└── README.md               # Este arquivo
```

---

## Dependências

* Python 3.8+
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [langchain](https://pypi.org/project/langchain/)
* [langchain-openai](https://pypi.org/project/langchain-openai/)
* getpass, os (módulos da biblioteca padrão)

Instale as dependências via pip:

```bash
pip install python-dotenv langchain langchain-openai
```

---

## Configuração

Todos os parâmetros necessários (chave de API, modelo, temperatura, tokens, prompt template, etc.) são lidos de um arquivo JSON.
Coloque seu `config.json` em `config/config.json`. A seguir, um exemplo:

```json
{
  "api_keys": {
    "OPENAI_API_KEY": "sua_chave_aqui"
  },
  "model": {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 512,
    "prompt": "Você é um assistente de suporte técnico. Gere um texto de chamado claro e profissional com base na descrição do usuário."
  }
}
```

* **OPENAI\_API\_KEY**: Chave de API obtida no site da OpenAI.
* **model**:

  * `model`: identificador do modelo (ex.: `gpt-3.5-turbo`).
  * `temperature`: grau de criatividade (0.0–1.0).
  * `max_tokens`: limite de tokens na resposta.
  * `prompt`: template do sistema usado pelo LangChain.

---

## Uso

1. **Configure** o arquivo `config/config.json` conforme o exemplo acima.
2. **Instancie** o assistente e gere o texto:

```python
from modules.AssistenteChamado import AssistenteChamado

if __name__ == "__main__":
    assistente = AssistenteChamado(config_path='config/config.json')
    descricao = (
        "O serviço mirage não está funcionando corretamente, "
        "já tentei reiniciá-lo e não funcionou. O que eu faço?"
    )
    chamado = assistente.gerar_texto_chamado(descricao)
    print(chamado)
```

O método `gerar_texto_chamado` retorna uma string pronta para ser enviada ao suporte.

---

## Estrutura da Classe `AssistenteChamado`

```python
class AssistenteChamado:
  
    def __init__(self, config_path='config/config.json'):
        # Carrega configurações (API KEY, modelo, prompt, etc.)
        self.config = ConfigHandler(config_path).load_config()
        self.api_key = self.config['api_keys']['OPENAI_API_KEY']
        self.model = self.config['model']['model']
        self.temperature = self.config['model']['temperature']
        self.max_tokens = self.config['model']['max_tokens']
        self.prompt_template = self.config['model']['prompt']
        
        # Monta prompt, LLM e parser
        self.prompt = self._prompt()
        self.llm = self._llm_model()
        self.parser = StrOutputParser()
        
        # Cria chain de execução
        self.chain = self._chain()
  
    def _prompt(self):
        return ChatPromptTemplate.from_messages([
            ("system", "{prompt}"),
            ("user", "{input}")
        ])
  
    def _llm_model(self):
        return ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            openai_api_key=self.api_key,
            max_tokens=self.max_tokens
        )
  
    def _chain(self):
        return self.prompt | self.llm | self.parser
  
    def gerar_texto_chamado(self, input_text):
        # Executa pipeline e retorna resultado
        return self.chain.invoke({
            "prompt": self.prompt_template,
            "input": input_text
        })
```

---

## Exemplo de `config.json`

```json
{
  "api_keys": {
    "OPENAI_API_KEY": "sk-********************************"
  },
  "model": {
    "model": "gpt-3.5-turbo",
    "temperature": 0.5,
    "max_tokens": 300,
    "prompt": "Você é um assistente de suporte técnico. Gere um texto formal e objetivo para o suporte."
  }
}
```

---


