from fun import *

banco = Banco()

while True:
    match menu():
        case 1:
            cadastro(banco)
        case 2:
            login(banco)
        case 3:
            exit()
        case _:
            pass
