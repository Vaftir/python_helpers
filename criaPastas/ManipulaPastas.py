# Autor: Yago Assis Mendes Faria
import os
import glob


#classe para criar pastas e limpar arquios

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

# Exemplo de uso:
#cria_pastas = CriaPastas()
#cria_pastas.cria_pastas('resultado', 'logs', 'logs/subpasta/pasta_x')

# Limpar a pasta de logs
#cria_pastas.limpa_logs('logs')
