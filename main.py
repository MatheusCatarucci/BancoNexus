from fun import *

usuarios = {}

while True:
    match menu():
        case 1:
            novo_usuario = cadastro()
            usuarios.update(novo_usuario)
        case 2:
            login()
        case 3:
            exit()
        case _:
            pass
