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


def saques(cliente):
    limpar()
    conta = cliente.getContaCorrente()
    print(f"Saldo atual: R${cliente.getSaldo():.2f}")
    try:
        valor = float(input("Quanto você deseja sacar: "))
    except ValueError:
        msg_erro()
        pause()
    if valor > 0 and valor <= conta.getSaldo():
        conta.subitrairSaldo(valor)
        limpar()
        print("Saque realizado com sucesso!")


def transferencia():
    pass
    # Transferência deve subtrair da conta do remetente e adicionar à do destinatário


def extrato(cliente):
    limpar()
    extrato = cliente.getClasseExtrato().mostrarExtrato()
    print(extrato)
    pause()


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
            input("Informe seu CPF apenas com números sem espaços: ")
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
        print("5 - Sair")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            msg_erro()
            pause()

        match escolha:
            case 1:
                deposito()
            case 2:
                saques(cliente)
            case 3:
                transferencia()
            case 4:
                extrato(cliente)
            case 5:
                break
            case _:
                limpar()
                msg_erro()
                pause()
