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


# Classe que representa o banco em si, contendo clientes
class Banco:
    def __init__(self):
        self.__clientes = []  # Lista privada de clientes cadastrados

    # Adiciona um cliente à lista do banco
    def addCliente(self, cliente):
        self.__clientes.append(cliente)

    # Busca um cliente pelo CPF e retorna o objeto correspondente
    def buscarCliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        else:
            return None  # Retorna None se o cliente não for encontrado

    def getClientes(self):
        return self.__clientes


# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome  # Nome do cliente
        self.__cpf = cpf  # CPF do cliente
        self.__senha = senha  # Senha do cliente
        self.__contas = []  # Lista de contas do cliente (pode ter mais de uma)
        self.__saldo = 50000

    # Retorna o nome do cliente
    def getNome(self):
        return self.__nome

    # Retorna o CPF do cliente
    def getCpf(self):
        return self.__cpf

    # Retorna todas as contas do cliente
    def getContas(self):
        return self.__contas

    # Adiciona uma nova conta ao cliente
    def abrirConta(self, conta):
        self.__contas.append(conta)

    def getSaldo(self):
        return self.__saldo

    def getSenha(self):
        return self.__senha


class Extrato:
    def __init__(self):
        self.__operacoes = []  # Lista de dicionários com tipo, valor e data

    # Adiciona uma operação ao extrato (saque, depósito, etc.)
    def adicionarOperacao(self, tipo, valor):
        self.__operacoes.append(
            {
                "tipo": tipo,
                "valor": valor,
                "data": datetime.now(),  # Registra a data e hora da operação
            }
        )

    # Exibe o extrato formatado no console
    def mostrarExtrato(self):
        print("=== Extrato ===")
        for operacao in self.__operacoes:
            print(
                f"{operacao['data'].strftime('%d/%m/%Y %H:%M')} - {operacao['tipo']}: R${operacao['valor']:.2f}"
            )


class Conta(OperacoesFinanceiras, ABC):
    def __init__(self, numero, saldoInicial=0):
        self.__numero = numero
        self.__saldo = saldoInicial
        self.__extrato = []

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo

    def getExtrato(self):
        return self.__extrato

    def alterarSaldo(self, valor):
        self.__saldo += valor

    def registrarOperacao(self, tipo, valor):
        self.__extrato.adicionarOperacao(tipo, valor)


class ContaCorrente(Conta):
    def __init__(self, numero, saldoInicial=0):
        super().__init__(numero, saldoInicial)

    def sacar(self, valor):
        # Verifica se o valor informado é válido
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        self.alterarSaldo(-valor)
        self.registrarOperacao("Saque", valor)
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
            return
        self.alterarSaldo(valor)
        self.registrarOperacao("Depósito", valor)
        print(
            f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}"
        )

    def transferir(self, valor, contaDestino):
        if valor <= 0 or valor > self.getSaldo():
            print("Transferência inválida.")
            return

        self.alterarSaldo(-valor)
        self.registrarOperacao("Transferência enviada", valor)
        contaDestino.alterarSaldo(valor)
        contaDestino.registrarOperacao("Transferência recebida", valor)

        print(
            f"Transferência de R${valor:.2f} realizada para conta {contaDestino.getNumero()}."
        )


class ContaPoupanca(Conta):
    def __init__(self, numero, saldoInicial=0):
        super().__init__(numero, saldoInicial)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if self.getSaldo() - valor < 100:
            print("Saldo mínimo de R$100,00 exigido para saques.")
            return
        self.__saldo -= valor
        self.__extrato.adicionarOperacao("Saque", valor)
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
            return
        self.__saldo += valor
        self.__extrato.adicionarOperacao("Depósito", valor)
        print(
            f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}"
        )

    def transferir(self, valor, contaDestino):
        if valor <= 0 or valor > self.getSaldo():
            print("Transferência inválida.")
            return
        self.__saldo -= valor
        contaDestino.__saldo += valor
        self.__extrato.adicionarOperacao("Transferência enviada", valor)
        contaDestino.__extrato.adicionarOperacao("Transferência recebida", valor)
        print(
            f"Transferência de R${valor:.2f} realizada para conta {contaDestino.getNumero()}."
        )
