import os
import getpass
from classes import *  # importa tudo do arquivo classes.py

# Dicionário global que armazena todos os usuários cadastrados
# Exemplo de estrutura:
# usuarios = {12345678900: {"nome": "João", "senha": "123", "saldo": 50000}}
usuarios = {}


# --- FUNÇÕES DE OPERAÇÕES BANCÁRIAS (ainda não implementadas) ---
def limpar():
    os.system("cls")


def pause():
    os.system("pause")


def msg_erro():
    print("Opção inválida, tente novamente")


# --- FUNÇÕES DE OPERAÇÕES BANCÁRIAS (ainda não implementadas) ---
def deposito():
    pass
    # Depósito deve adicionar um valor ao saldo da conta do usuário


def saques():
    pass
    # Saque deve subtrair um valor do saldo da conta do usuário


def transferencia():
    pass
    # Transferência deve subtrair da conta do remetente e adicionar à do destinatário


def extrato():
    pass
    # Extrato deve exibir o histórico de movimentações da conta


# --- FUNÇÕES DE SISTEMA ---
def menu():
    limpar()
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    try:
        escolha = int(input("Escolha uma opção: "))  # leitura do menu principal
        return escolha
    except ValueError:
        msg_erro()
        pause()


def cadastro():
    limpar()
    print("Bem vindo ao banco nexus")

    try:
        nome = input("Informe seu nome: ").capitalize()  # primeira letra maiúscula
    except ValueError:
        msg_erro()
        pause()

    try:
        cpf = int(
            input("Informe seu cpf apenas com números sem espaços: ")
        )  # CPF como inteiro
    except ValueError:
        msg_erro()
        pause()

    try:
        senha = getpass.getpass("Informe sua senha: ")  # senha não aparece na tela
    except ValueError:
        msg_erro()
        pause()

    # Cria o dicionário representando o novo usuário
    usuario = {
        cpf: {"nome": nome, "senha": senha, "saldo": 50000}
    }  # saldo inicial de 50.000

    # Retorna o dicionário para ser adicionado ao dicionário principal "usuarios"
    usuarios.update(usuario)


def login():
    limpar()
    print("Bem vindo ao banco nexus")

    try:
        cpf = int(input("Informe seu cpf apenas com números sem espaços: "))
    except ValueError:
        msg_erro()
        pause()

    try:
        senha = getpass.getpass("Informe sua senha: ")
    except ValueError:
        msg_erro()
        pause()

    # Verifica se o CPF e senha estão corretos
    if autenticar(cpf, senha, usuarios):
        banco(cpf)  # entra no menu do banco
    else:
        limpar()
        print("Usuário não encontrado")
        pause()


def autenticar(cpf, senha, usuarios):
    # Aqui há um pequeno erro lógico:
    # deve acessar usuarios[cpf]["senha"], não usuarios["senha"]
    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        conta = True
    else:
        conta = False

    return conta


# Banco (após o login)
def banco(cpf):
    while True:
        usuario = usuarios[
            cpf
        ]  # obtém o dicionário com as informações do usuário logado
        limpar()
        print(f"Usuário: {usuario['nome']}")
        print(f"Saldo: {usuario['saldo']}")
        print(40 * "-")
        print("1 - Depósito")
        print("2 - Saques")
        print("3 - Transferência")
        print("4 - Extrato")

        try:
            e = int(
                input("Escolha uma opção: ")
            )  # tenta converter a escolha em número inteiro
            return e
        except ValueError:
            msg_erro()
            pause()
