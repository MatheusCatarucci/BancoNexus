import os
from classes import *

def limpar():
    os.system("cls")


def menu():
    limpar()
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    e = int(input("Escolha uma opção: "))
    return e

def cadastro():
    pass

def login():
    pass