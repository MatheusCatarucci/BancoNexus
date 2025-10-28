from fun import *  # importa todas as funções e classes necessárias

# Cria uma instância do banco
banco = Banco()

# Loop principal do sistema
while True:
    match menu():  # chama o menu principal
        case 1:
            cadastro(banco)  # opção de cadastro
        case 2:
            login(banco)  # opção de login
        case 3:
            exit()  # encerra o programa
        case _:
            msg_erro()  # tratamento de erro de opção
            pause()
