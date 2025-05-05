import datetime
import smtplib
import os
from email.message import EmailMessage
#from modules.config.ConfigHandler import ConfigHandler
from ConfigHandler import ConfigHandler

class EnviaEmail:
    def __init__(self, config_path="config/config.json"):
        """Inicializa a classe com as credenciais do servidor SMTP."""
        self.config = ConfigHandler(config_path)  # Usa a nova classe corretamente
        email_config = self.config.get_data("email")  # Obtém a seção "email"
        self.nome_robo = self.config.get_data("nome_robo") or "Robô Desconhecido"  # Se não existir, usa um valor padrão

        if not email_config:
            raise ValueError("❌ Configuração de e-mail não encontrada no arquivo JSON.")

        self.servidor_smtp = email_config.get("smtp_server")
        self.porta = email_config.get("smtp_port")
        self.usuario = email_config.get("user")
        self.senha = email_config.get("password")
        self.from_ = email_config.get("from")
        self.alias = email_config.get("alias")
        self.cc = email_config.get("cc") or []
        self.email_log = email_config.get("email_log")
        self.destinatario = email_config.get("destinatario")
        

    def enviar_email(self, destinatario, assunto, mensagem, anexo=None, cc=None, bcc=None):
        """Envia um e-mail com suporte a HTML, anexo opcional, cópia (CC) e cópia oculta (BCC)."""
        try:
            msg = EmailMessage()
            msg["From"] = f"{self.alias} <{self.from_}>"
            msg["To"] = destinatario
            msg["Subject"] = assunto
            msg.set_content(mensagem, subtype="html")
            cc = cc or self.cc

            if cc:
                msg["Cc"] = ", ".join(cc) if isinstance(cc, list) else cc
            if bcc:
                msg["Bcc"] = ", ".join(bcc) if isinstance(bcc, list) else bcc

            if anexo:
                self._adicionar_anexo(msg, anexo)

            with smtplib.SMTP(self.servidor_smtp, self.porta) as servidor:
                servidor.ehlo()
                servidor.starttls()  # Ativar criptografia TLS
                servidor.login(self.usuario, self.senha)
                servidor.send_message(msg)

            print(" E-mail enviado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

    def _adicionar_anexo(self, msg, caminho_anexo):
        """Adiciona um anexo ao e-mail."""
        try:
            if not os.path.exists(caminho_anexo):
                print(f" Arquivo {caminho_anexo} não encontrado!")
                return

            with open(caminho_anexo, "rb") as arquivo:
                dados = arquivo.read()
                nome_arquivo = os.path.basename(caminho_anexo)
                msg.add_attachment(dados, maintype="application", subtype="octet-stream", filename=nome_arquivo)

        except Exception as e:
            print(f" Erro ao adicionar anexo: {e}")

    def enviar_email_sucesso(self, file_path=None, destinatario=None, cc=None, bcc=None, mensagem=None):
        """Envia um e-mail informando que o relatório CTE foi gerado com sucesso."""
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        process_config = self.config.get_data("process_success")
        cc = self.cc or cc
        destinatario = self.destinatario

        if not process_config:
            raise ValueError(" Configuração de sucesso do processo não encontrada no arquivo JSON.")

        # Substituir variáveis no template
        assunto_email = process_config["subject"].replace("{data}", data_atual).replace("{NomeRobo}", self.nome_robo)
        mensagem_email = process_config["body"].replace("{data}", data_atual).replace("{NomeRobo}", self.nome_robo).replace("{mensagem}", mensagem or "")

        self.enviar_email(destinatario, assunto_email, mensagem_email, anexo=file_path, cc=cc or [], bcc=bcc or [])

        if os.path.exists(file_path):
            print(f" Arquivo {file_path} removido após envio.")

    def enviar_email_erro(self, destinatario=None, error_message=None, cc=None, bcc=None):
        """Envia um e-mail informando sobre um erro no processo."""
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        process_config = self.config.get_data("process_error")
        cc = self.cc or cc
        destinatario = self.email_log

        if not process_config:
            raise ValueError(" Configuração de erro do processo não encontrada no arquivo JSON.")

        # Substituir variáveis no template
        assunto_email = process_config["subject"].replace("{data}", data_atual).replace("{NomeRobo}", self.nome_robo)
        mensagem_email = process_config["body"].replace("{data}", data_atual).replace("{NomeRobo}", self.nome_robo).replace("{mensagem}", error_message)

        self.enviar_email(destinatario, assunto_email, mensagem_email, cc=cc or [], bcc=bcc or [])

# Teste de envio de e-mail

# def teste_envio_email():
#     enviador = EnviaEmail()
#     enviador.enviar_email(
#         destinatario="yago.faria@friopecas.com.br",
#         assunto="Teste de E-mail com CC",
#         mensagem="<h1>Olá, todos!</h1><p>Esse e-mail tem cópia.</p>",
#         anexo=r"C:\Users\yago.faria\Desktop\Desenvolvimento\AutomacaoCTE\data\resultado_190225.xlsx",
#         cc=["luis.ayerbe@friopecas.com.br"],  # Lista de e-mails em cópia
#         bcc=[]  # Lista de e-mails ocultos
#     )

# if __name__ == "__main__":
#     #teste_envio_email()
#     enviador = EnviaEmail()
#     enviador.enviar_email_cte_sucesso(
#         file_path=r"C:\Users\yago.faria\Desktop\Desenvolvimento\AutomacaoCTE\data\resultado_190225.xlsx",
#         destinatario="yago.faria@friopecas.com.br",
#         cc=["luis.ayerbe@friopeças.com.br"]
#     )

#     enviador.enviar_email_de_erro(
#         destinatario="yago.faria@friopecas.com.br",
#         error_message="Falha ao conectar ao banco de dados. Timeout atingido.",
#         cc=["luis.ayerbe@friopecas.com.br"]
#     )
