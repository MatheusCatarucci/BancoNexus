import os
import getpass
from classes import *  # importa tudo do arquivo classes.py


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


def cadastro(banco):
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
    usuario = Cliente(nome=nome, cpf=cpf, senha=senha)
    banco.addCliente(usuario)


def login(banco):
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
    cliente = autenticar(banco, senha, cpf)
    if cliente:
        main(cliente)  # entra no menu do banco
    else:
        limpar()
        print("Usuário não encontrado")
        pause()


def autenticar(banco, senha, cpf):
    for cliente in banco.getClientes():
        if cliente.getCpf() == cpf and cliente.getSenha() == senha:
            return cliente
        else:
            return None

# Banco (após o login)
def main(cliente):
    while True:
        limpar()
        print(f"Usuário: {cliente.getNome()}")
        print(f"Saldo: {cliente.getSaldo()}")
        print(40 * "-")
        print("1 - Depósito")
        print("2 - Saques")
        print("3 - Transferência")
        print("4 - Extrato")

        try:
            escolha = int(
                input("Escolha uma opção: ")
            )  # tenta converter a escolha em número inteiro
            return escolha
        except ValueError:
            msg_erro()
            pause()
