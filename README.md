## Visão Geral

Este repositório reúne um conjunto de classes utilitárias para automação de tarefas comuns em Python: geração de textos via OpenAI, manipulação de arquivos JSON, conexão a banco MySQL, gestão de diretórios, criptografia simples e envio de e‑mails via SMTP. A ideia é fornecer componentes modulares e reusáveis para acelerar o desenvolvimento de scripts e pipelines de automação.

---

## Estrutura do Projeto

```
.
├── config/
│   └── config.json             # Exemplo de configurações
├── modules/
│   ├── chamado/
│   │   └── AssistenteChamado.py
│   ├── config/
│   │   └── ConfigHandler.py
│   ├── connection/
│   │   └── Connection.py
│   ├── arquivo/
│   │   └── ManipulaPastas.py
│   ├── criptografia/
│   │   └── Criptografia.py
│   └── email/
│       └── EnviaEmail.py
└── README.md                   # Este arquivo
```

---

## Instalação

1. **Clone** o repositório e entre na pasta raiz.

2. **Crie** um ambiente virtual (opcional, mas recomendado).

3. **Instale** dependências mínimas:

   ```bash
   pip install mysql-connector-python:contentReference[oaicite:0]{index=0} python-dotenv:contentReference[oaicite:1]{index=1} langchain-openai:contentReference[oaicite:2]{index=2} openai:contentReference[oaicite:3]{index=3}
   ```

4. **Configure** seu arquivo `config/config.json` conforme o exemplo desta pasta.

---

## Descrição das Classes

### 1. AssistenteChamado

Gera textos de chamados de suporte usando LangChain e OpenAI Chat ●

* **Depedências**: `langchain-openai`, `openai`
* **Funcionalidades**: carrega prompt template, chama `ChatOpenAI`, retorna string formatada.

### 2. ConfigHandler

Manipula arquivos JSON de configuração.

* **Depedência**: módulo padrão `json`
* **Métodos**:

  * `load_config()`, `get_data(key)`, `set_config_value()`, `delete_config_value()`, `save_config()`

### 3. Connection

Gerencia conexão e queries em MySQL.

* **Depedência**: `mysql-connector-python`
* **Context Manager**: suporte a `with` via protocolo 
* **Métodos**: `connect()`, `execute_query()`, `execute_read_query()`, `disconnect()`, `__enter__()`, `__exit__()`.

### 4. ManipulaPastas

Cria pastas e limpa arquivos em diretórios.

* **Depedências**: `os`, `glob`
* **Métodos**:

  * `cria_pastas(*pastas)`: `os.makedirs()` recursivo
  * `limpa_diretorio(dir)`: `glob.glob()` + `os.remove()`

### 5. Criptografia

Implementa cifra linear simples (multiplicação e deslocamento) com blocos hex de 6 dígitos.

* **Princípio**:
  $\text{enc} = \text{ord}(c)\times c_a + c_b$ → hex(6 dígitos)
  $\text{dec} = (\text{int(hex)} - c_b)/c_a$
* **Uso educacional**: não adequado para segurança real.

### 6. EnviaEmail

Envio de e‑mail via SMTP com suporte a HTML, anexos, CC e BCC.

* **Depedências**:

  * `smtplib`
  * `email.message.EmailMessage`
  * `datetime` (built‑in)
* **Funcionalidades**:

  * `enviar_email(...)` genérico
  * `enviar_email_sucesso(...)` e `enviar_email_erro(...)` usam templates JSON

---

## Exemplo de Configuração (`config/config.json`)

```json
{
  "api_keys": {
    "OPENAI_API_KEY": "sk-***************"
  },
  "model": {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 512,
    "prompt": "Você é um assistente de suporte técnico. Gere um texto profissional."
  },
  "email": {
    "smtp_server": "smtp.exemplo.com",
    "smtp_port": 587,
    "user": "user@exemplo.com",
    "password": "senha",
    "from": "user@exemplo.com",
    "alias": "Meu Robô",
    "cc": ["backup@exemplo.com"],
    "email_log": "logs@exemplo.com",
    "destinatario": "destino@exemplo.com"
  },
  "nome_robo": "Automatizador",
  "process_success": {
    "subject": "Relatório de {data}",
    "body": "<p>Gerado com sucesso em {data}.</p><p>{mensagem}</p>"
  },
  "process_error": {
    "subject": "Erro em {data}",
    "body": "<p>Falha em {data}.</p><p>{mensagem}</p>"
  }
}
```

---

## Exemplos de Uso

* **Texto de Chamado**

  ```python
  from modules.chamado.AssistenteChamado import AssistenteChamado
  ac = AssistenteChamado("config/config.json")
  print(ac.gerar_texto_chamado("Erro no serviço X"))
  ```

* **Config JSON**

  ```python
  from modules.config.ConfigHandler import ConfigHandler
  cfg = ConfigHandler("config/config.json")
  api_keys = cfg.get_data("api_keys")
  ```

* **MySQL**

  ```python
  from modules.connection.Connection import Connection
  with Connection("localhost","db","user","pass") as conn:
      conn.execute_query("CREATE TABLE teste (id INT)")
  ```

* **Pastas**

  ```python
  from modules.arquivo.ManipulaPastas import ManipulaPastas
  mp = ManipulaPastas()
  mp.cria_pastas("out","logs")
  mp.limpa_diretorio("logs")
  ```

* **Criptografia**

  ```python
  from modules.criptografia.Criptografia import Criptografia
  cr = Criptografia()
  cr.c_a, cr.c_b = 3, 5
  enc = cr.encriptar("Olá")
  print(cr.desencriptar(enc))
  ```

* **E‑mail**

  ```python
  from modules.email.EnviaEmail import EnviaEmail
  ee = EnviaEmail("config/config.json")
  ee.enviar_email_sucesso(
      file_path="relatorio.xlsx",
      mensagem="Processo concluído."
  )
  ```

---

## Licença

MIT License – fique à vontade para modificar e redistribuir.