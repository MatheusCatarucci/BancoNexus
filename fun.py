import os
import getpass
from classes import *  # importa todas as classes do arquivo classes.py


# --- FUNÇÕES DE SISTEMA BÁSICAS ---
def limpar():
    os.system("cls")  # limpa o console


def pause():
    os.system("pause")  # pausa a execução até pressionar uma tecla


def msg_erro():
    print("Opção inválida, tente novamente")  # mensagem genérica de erro


# --- FUNÇÕES DE OPERAÇÕES BANCÁRIAS ---
def deposito(cliente):
    limpar()
    conta = cliente.getClasseContaCorrente()
    print(f"Saldo atual: R${cliente.getSaldo():.2f}")

    try:
        valor = float(input("Depósito\nR$: "))  # solicita valor ao usuário
    except ValueError:
        msg_erro()
        pause()
        return

    if valor > 0:
        conta.somarSaldo(valor)  # soma o valor ao saldo
        cliente.getClasseExtrato().adicionarOperacao(
            "Depósito",
            valor,
            remetente = None,
            destinatario = None
        )
        limpar()
        print("Depósito realizado com sucesso!")


def saques(cliente):
    limpar()
    conta = cliente.getClasseContaCorrente()
    print(f"Saldo atual: R${cliente.getSaldo():.2f}")

    try:
        valor = float(input("Quanto você deseja sacar: "))
    except ValueError:
        msg_erro()
        pause()
        return

    if valor > 0 and valor <= conta.getSaldo():
        conta.subtrairSaldo(valor)
        cliente.getClasseExtrato().adicionarOperacao(
            "Saque",
            valor,
            cliente.getNome(),
            destinatario = None
        )

        limpar()
        print("Saque realizado com sucesso!")


def transferencia(banco, cliente):
    while True:
        limpar()
        print("=== Transferência ===")

        try:
            cpf_destinatario = int(
                input("Informe o CPF do destinatário (0 para cancelar): ")
            )
            if cpf_destinatario != 0:
                valor_transferencia = float(input("Informe o valor da transferência: "))
                if cpf_destinatario == cliente.getCpf():
                    limpar()
                    print("Você não pode realizar uma transferência para você mesmo")
                    pause()

                destinatario = banco.buscarCliente(cpf_destinatario)
                if destinatario is None:
                    limpar()
                    print("Usuário não encontrado")
                    pause()
                    return

                conta_origem = cliente.getClasseContaCorrente()
                conta_destino = destinatario.getClasseContaCorrente()

                if valor_transferencia <= 0:
                    limpar()
                    print("Valor inválido")
                    pause()
                    return

                if conta_origem.getSaldo() < valor_transferencia:
                    print("Saldo insuficiente")
                    pause()
                    return

                # realiza a transferência
                conta_origem.subtrairSaldo(valor_transferencia)
                conta_destino.somarSaldo(valor_transferencia)

                # registra no extrato de ambos
                cliente.getClasseExtrato().adicionarOperacao(
                    "Transferência enviada",
                    valor_transferencia,
                    cliente.getNome(),
                    destinatario.getNome(),
                )
                destinatario.getClasseExtrato().adicionarOperacao(
                    "Transferência recebida",
                    valor_transferencia,
                    cliente.getNome(),
                    destinatario.getNome(),
                )

                limpar()
                print("Transferência realizada com sucesso")
                pause()
                break
            else:
                break
        except ValueError:
            msg_erro()
            pause()
            return


def extrato(cliente):
    limpar()
    extrato = cliente.getClasseExtrato().mostrarExtrato()  # obtém o extrato formatado
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
    print("Bem-vindo ao banco Nexus")

    try:
        nome = input("Informe seu nome: ").capitalize()  # formata o nome
        cpf_pegar = input("Informe seu CPF (Apenas 11 números): ")
        if not (cpf_pegar.isdigit() and len(cpf_pegar) == 11):
            limpar()
            print("CPF inválido. Deve conter exatamente 11 números.")
            pause()
            return
        cpf = int(cpf_pegar)
        senha = getpass.getpass("Informe sua senha: ")  # senha oculta
    except ValueError:
        msg_erro()
        pause()
        return

    # cria um novo cliente e adiciona ao banco
    usuario = Cliente(nome=nome, cpf=cpf, senha=senha)
    banco.addCliente(usuario)
    limpar()
    print("Cadastro realizado com sucesso!")
    pause()


def login(banco):
    limpar()
    print("Bem-vindo ao banco Nexus")

    try:
        cpf = int(input("Informe seu CPF: "))
        senha = getpass.getpass("Informe sua senha: ")
    except ValueError:
        msg_erro()
        pause()
        return

    cliente = autenticar(banco, senha, cpf)
    if cliente:
        main(cliente, banco)  # entra no menu principal do cliente
    else:
        limpar()
        print("Usuário não encontrado")
        pause()


# percorre todos os clientes e verifica credenciais
def autenticar(banco, senha, cpf):
    for cliente in banco.getClientes():
        if cliente.getCpf() == cpf and cliente.getSenha() == senha:
            return cliente
    return None  # só retorna None se nenhum cliente corresponder


# Menu principal após login
def main(cliente, banco):
    while True:
        limpar()
        print(f"Usuário: {cliente.getNome()}")
        print(f"Saldo: R${cliente.getSaldo():.2f}")
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
            continue

        match escolha:
            case 1:
                deposito(cliente)
            case 2:
                saques(cliente)
            case 3:
                transferencia(banco, cliente)
            case 4:
                extrato(cliente)
            case 5:
                break
            case _:
                limpar()
                msg_erro()
                pause()
