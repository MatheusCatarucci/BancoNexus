import os
import getpass
from classes import *  # importa tudo do arquivo classes.py (ex: classes de usuários ou contas)


# Função para limpar o terminal (no Windows usa 'cls')
def limpar():
    os.system("cls")


# Função para pausar a execução até o usuário apertar uma tecla
def pause():
    os.system("pause")


# Função para exibir mensagem padrão de erro
def msg_erro():
    print("Opção inválida, tente novamente")


# Função do menu principal
def menu():
    limpar()
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    try:
        # Tenta converter a entrada em inteiro
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        # Caso o usuário digite algo inválido
        msg_erro()
        pause()


# Função para cadastrar novo usuário
def cadastro():
    limpar()
    print("Bem vindo ao banco nexus")

    try:
        # Solicita o nome do usuário e coloca a primeira letra em maiúsculo
        nome = input("Informe seu nome: ").capitalize()
    except ValueError:
        msg_erro()
        pause()

    try:
        # Solicita o CPF e converte para inteiro
        cpf = int(input("Informe seu cpf apenas com números sem espaços: "))
    except ValueError:
        msg_erro()
        pause()

    try:
        # Solicita a senha (sem mostrar na tela)
        senha = getpass.getpass("Informe sua senha: ")
    except ValueError:
        msg_erro()
        pause()

    # Cria o dicionário representando o usuário
    usuario = {cpf: {"nome": nome, "senha": senha}}

    # Retorna o dicionário para ser adicionado à lista geral de usuários
    return usuario


# (Código comentado que imprime os usuários cadastrados)
# for cpf, valores in usuarios.items():
#     print(f"CPF - {cpf}")
#     print(f"Nome - {valores['nome']}")
#     print(f"Senha - {valores['senha']}")
#     print(20 * "-")
#     pause()


# Função de login
def login():
    limpar()
    print("Bem vindo ao banco nexus")

    try:
        # Solicita o nome do usuário e coloca a primeira letra em maiúsculo
        nome = input("Informe seu nome: ").capitalize()
    except ValueError:
        msg_erro()
        pause()

    try:
        # Solicita o CPF e converte para inteiro
        cpf = int(input("Informe seu cpf apenas com números sem espaços: "))
    except ValueError:
        msg_erro()
        pause()

    try:
        # Solicita a senha (sem mostrar na tela)
        senha = getpass.getpass("Informe sua senha: ")
    except ValueError:
        msg_erro()
        pause()