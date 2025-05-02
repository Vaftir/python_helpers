## Visão Geral

A classe **EnviaEmail** simplifica o envio de mensagens via SMTP, permitindo o uso de templates definidos em JSON para notificações de sucesso e erro de processos. Ela suporta conteúdo HTML, anexos, cópia (CC) e cópia oculta (BCC), além de oferecer métodos prontos para envio de e-mails de sucesso e de erro baseados em configurações.

---

## Estrutura do Projeto

```
.
├── config/
│   └── config.json             # Configurações de e-mail e templates
├── modules/
│   └── config/
│       └── ConfigHandler.py    # Carrega e manipula o JSON de configurações
├── modules/
│   └── email/
│       └── EnviaEmail.py       # Esta classe
└── README.md                   # Este arquivo
```

---

## Dependências

* Python 3.6+
* Biblioteca padrão:

  * `smtplib`
  * `email.message.EmailMessage`
  * `datetime`
  * `os`
* Módulo interno:

  * `modules.config.ConfigHandler`

Instale o driver de sua escolha ou garanta que seu ambiente suporte SMTP TLS (não há bibliotecas externas específicas além da padrão).

---

## Exemplo de `config.json`

```json
{
  "email": {
    "smtp_server": "smtp.exemplo.com",
    "smtp_port": 587,
    "user": "usuario@exemplo.com",
    "password": "sua_senha",
    "from": "usuario@exemplo.com",
    "alias": "Meu Robô",
    "cc": ["backup@exemplo.com"],
    "email_log": "logs@exemplo.com",
    "destinatario": "destino@exemplo.com"
  },
  "nome_robo": "Automatizador CTE",
  "process_success": {
    "subject": "Relatório gerado em {data} pelo {NomeRobo}",
    "body": "<p>O relatório foi gerado com sucesso em {data}.</p><p>Mensagem: {mensagem}</p>"
  },
  "process_error": {
    "subject": "Erro em {data} no {NomeRobo}",
    "body": "<p>Ocorreu um erro em {data}.</p><p>Detalhes: {mensagem}</p>"
  }
}
```

* **email**: configurações de conexão SMTP e remetentes
* **nome\_robo**: nome usado nos templates
* **process\_success** / **process\_error**: templates de assunto e corpo, com placeholders `{data}`, `{NomeRobo}`, `{mensagem}`

---

## Uso Básico

```python
from modules.email.EnviaEmail import EnviaEmail

# Inicializa com o caminho para o JSON
enviador = EnviaEmail(config_path="config/config.json")

# Envio genérico
enviador.enviar_email(
    destinatario="usuario@exemplo.com",
    assunto="Teste de envio",
    mensagem="<h1>Olá!</h1><p>Este é um teste.</p>",
    anexo="/caminho/arquivo.pdf",
    cc=["copiar@exemplo.com"],
    bcc=["oculto@exemplo.com"]
)
```

---

## Métodos de Conveniência

### `enviar_email_sucesso(file_path=None, destinatario=None, cc=None, bcc=None, mensagem=None)`

* Usa o template **process\_success** do JSON.
* Substitui `{data}` pela data atual (dd/mm/YYYY) e `{NomeRobo}` pelo nome do robô.
* Anexa arquivo se `file_path` informado, e remove o arquivo após envio.

**Exemplo**

```python
enviador.enviar_email_sucesso(
    file_path="relatorio.xlsx",
    mensagem="Dados extraídos sem erros."
)
```

### `enviar_email_erro(destinatario=None, error_message=None, cc=None, bcc=None)`

* Usa o template **process\_error**.
* Envia ao `email_log` definido em config.
* Inclui detalhes do erro em `{mensagem}`.

**Exemplo**

```python
enviador.enviar_email_erro(
    error_message="Falha na conexão com o banco."
)
```

---

## Internals

* **Login TLS**: usa `starttls()` para segurança.
* **Anexos**: lidos em binário e adicionados como `application/octet-stream`.
* **Fallbacks**:

  * Se faltarem configurações, lança `ValueError`.
  * São usados valores padrão para alias e destinatários, se não definidos.

---

## Boas Práticas

* Proteja suas credenciais (use variáveis de ambiente ou `.env` em produção).
* Valide caminhos de anexos antes de chamar `enviar_email`.
* Mantenha os templates HTML seguros (evite injeção de conteúdo).
* Use tratamento de exceções para capturar falhas de rede.

---

## Licença

MIT License. Adapte conforme suas necessidades!
