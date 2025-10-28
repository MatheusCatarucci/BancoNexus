from abc import abstractmethod, ABC
from datetime import *


# Interface que define as operações financeiras básicas
class OperacoesFinanceiras(ABC):
    # Método abstrato para saque — deve ser implementado nas subclasses
    @abstractmethod
    def sacar(self, valor):
        pass

    # Método abstrato para depósito — deve ser implementado nas subclasses
    @abstractmethod
    def depositar(self, valor):
        pass

    # Método abstrato para transferência — deve ser implementado nas subclasses
    @abstractmethod
    def transferir(self, valor, contaDestino):
        pass


# Classe que representa o banco e gerencia os clientes cadastrados
class Banco:
    def __init__(self):
        self.__clientes = []  # Lista privada de clientes cadastrados

    # Adiciona um novo cliente ao banco
    def addCliente(self, cliente):
        self.__clientes.append(cliente)

    # Busca um cliente pelo CPF e retorna o objeto correspondente, se existir
    def buscarCliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.getCpf() == cpf:
                return cliente
        return None  # Retorna None se o cliente não for encontrado

    # Retorna a lista de todos os clientes cadastrados
    def getClientes(self):
        return self.__clientes


# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome  # Nome do cliente
        self.__cpf = cpf  # CPF do cliente
        self.__senha = senha  # Senha do cliente
        self.__contas = []  # Lista de contas do cliente
        self.__extrato = Extrato()  # Cria uma instância de extrato
        self.__contaCorrente = ContaCorrente()  # Cria uma conta corrente padrão

    # Retorna o nome do cliente
    def getNome(self):
        return self.__nome

    # Retorna o CPF do cliente
    def getCpf(self):
        return self.__cpf

    # Retorna a senha do cliente
    def getSenha(self):
        return self.__senha

    # Retorna todas as contas do cliente
    def getContas(self):
        return self.__contas

    # Adiciona uma nova conta à lista do cliente
    def abrirConta(self, conta):
        self.__contas.append(conta)

    # Retorna o saldo da conta corrente do cliente
    def getSaldo(self):
        return self.__contaCorrente.getSaldo()

    # Retorna a instância da classe Extrato
    def getClasseExtrato(self):
        return self.__extrato

    # Retorna a instância da classe ContaCorrente
    def getClasseContaCorrente(self):
        return self.__contaCorrente


# Classe responsável por registrar as operações realizadas
class Extrato:
    def __init__(self):
        self.__operacoes = []  # Lista de dicionários com tipo, valor e data

    # Adiciona uma operação ao extrato
    def adicionarOperacao(self, tipo, valor, remetente, destinatario):
        self.__operacoes.append(
            {
                "tipo": tipo,
                "valor": valor,
                "data": datetime.now(),
                "remetente": remetente,
                "destinatario": destinatario,
                # Registra a data e hora da operação
            }
        )

    # Retorna o extrato formatado como texto
    def mostrarExtrato(self):
        linhas = ["=== Extrato ==="]
        for operacao in self.__operacoes:
            linha = f"{operacao['data'].strftime('%d/%m/%Y %H:%M')} - {operacao['tipo']}: R${operacao['valor']:.2f}\nRemetente: {operacao['remetente']} - Destinatário: {operacao['destinatario']}"
            linhas.append(linha)
        return "\n".join(linhas)

    # Retorna a lista de operações (em formato bruto)
    def getExtrato(self):
        return self.__operacoes


# Classe base para contas bancárias (abstrata)
class Conta(OperacoesFinanceiras, ABC):
    def __init__(self, saldoInicial=0):
        self.__saldo = saldoInicial  # Saldo inicial da conta

    # Retorna o saldo atual
    def getSaldo(self):
        return self.__saldo

    # Soma um valor ao saldo
    def somarSaldo(self, valor):
        self.__saldo += valor

    # Subtrai um valor do saldo
    def subitrairSaldo(self, valor):
        self.__saldo -= valor


# Classe que representa uma conta corrente — versão padronizada
# Conta Corrente
class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if valor > self.getSaldo():
            print("Saldo insuficiente.")
            return
        self.subitrairSaldo(valor)
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
            return
        self.somarSaldo(valor)
        print(
            f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}"
        )

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido para transferência.")
            return
        if valor > self.getSaldo():
            print("Saldo insuficiente.")
            return
        self.subitrairSaldo(valor)
        conta_destino.somarSaldo(valor)
        print(f"Transferência de R${valor:.2f} realizada para o destinatário.")


# Classe que representa uma conta poupança — versão padronizada
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if self.getSaldo() - valor < 100:  # saldo mínimo de 100
            print("Saldo mínimo de R$100,00 exigido para saques.")
            return
        self.subitrairSaldo(valor)
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
            return
        self.somarSaldo(valor)
        print(
            f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}"
        )

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido para transferência.")
            return
        if valor > self.getSaldo() - 100:  # mantém saldo mínimo
            print("Saldo insuficiente para transferência.")
            return
        self.subitrairSaldo(valor)
        conta_destino.somarSaldo(valor)
        print(f"Transferência de R${valor:.2f} realizada para o destinatário.")
