from fun import *

while True:
    match menu():
        case 1:
            cadastro()
        case 2:
            login()
        case 3:
            exit()
        case _:
            pass
