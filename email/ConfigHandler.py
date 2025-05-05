# Autor: Yago Assis Mendes Faria
import json

'''
 Esta classe é responsável por manipular um arquivo de configuração JSON.
    Ela permite carregar, salvar e manipular valores de configuração.
    Atributos:
        file_path: str
        config: dict
    Métodos:
        load_config: dict
        get_data: dict
        save_config: None
        set_config_value: None
        delete_config_value: None
    dependencias:
        json
    
'''
class ConfigHandler:

    # region Construtores
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()
        print(f"Instância de ConfigHandler criada com o arquivo {file_path}")
    # endregion Construtores

    # region Destrutores
    def __del__(self):
        print(f"Instância de ConfigHandler com o arquivo {self.file_path} está sendo destruída.")
    # endregion Destrutores

    # region Métodos Públicos
    def load_config(self):
        # Lê o arquivo config.json em utf-8 e retorna o conteúdo
        try:
            with open(self.file_path, 'r',encoding="UTF-8" ) as file:
                return json.load(file)
        except FileNotFoundError:
            error_msg = f"Config file {self.file_path} not found."
            print(error_msg)
            return None
        except json.JSONDecodeError:
            error_msg = f"Error decoding JSON from the config file {self.file_path}."
            print(error_msg)
            return None


    def get_data(self, key):
        # Obtém um valor da configuração
        if self.config is None:
            return None
        try:
            return self.config.get(key, {})
        except Exception as e:
            error_msg = f"Error getting user credentials for key {key}: {e}"
            print(error_msg)
            return None

    def save_config(self):
        # Salva a configuração de volta no arquivo
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.config, file, indent=4)
        except Exception as e:
            error_msg = f"Error saving config to file {self.file_path}: {e}"
            print(error_msg)
            return None

    def set_config_value(self, key, value):
        # Define um valor na configuração
        if self.config is None:
            self.config = {}
        self.config[key] = value

    def delete_config_value(self, key):
        # Exclui um valor da configuração
        if self.config and key in self.config:
            del self.config[key]
    # endregion Métodos Públicos

# Exemplo de uso
'''
# Criando uma instância de ConfigHandler com o caminho do arquivo JSON
config_handler = ConfigHandler('config.json')

# Exemplo de obtenção de informações da API 'criar_chamados_csc'
api_info = config_handler.get_api_info('criar_chamados_csc')
if api_info:
    print("API Info:", api_info)
else:
    print("API 'criar_chamados_csc' não encontrada ou configuração não carregada.")

# Exemplo de obtenção de informações da URL 'url_gobots'
url_info = config_handler.get_url_info('url_gobots')
if url_info:
    print("URL Info:", url_info)
else:
    print("URL 'url_gobots' não encontrada ou configuração não carregada.")

# Exemplo de obtenção de credenciais do usuário 'gobots_user'
user_credentials = config_handler.get_user_credentials('gobots_user')
if user_credentials:
    print("User Credentials:", user_credentials)
else:
    print("Credenciais 'gobots_user' não encontradas ou configuração não carregada.")

# Exemplo de definição de um novo valor na configuração
config_handler.set_config_value('new_key', 'new_value')
# edita o valor de uma chave
config_handler.set_config_value('new_key', 'new_value2')

# Salva a configuração de volta no arquivo
config_handler.save_config()

# Exemplo de exclusão de um valor na configuração
config_handler.delete_config_value('new_key')
config_handler.save_config()
'''
