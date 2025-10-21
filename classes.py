from abc import abstractmethod, ABC
from datetime import *


class OperacoesFinanceiras(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def transferir(self, valor, conta_destino):
        pass


class Banco:
    def __init__(self):
        self.__clientes = []

    def addCliente(self, cliente):
        self.__clientes.append(cliente)

    def buscarCliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None


class Cliente:
    def __init__(self, nome, cpf, contas):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getContas(self):
        return self.__contas

    def abrirConta(self, conta):
        self.__contas.append(conta)


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
