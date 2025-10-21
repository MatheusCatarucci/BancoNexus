from abc import ABC
from abc import abstractmethod

class Conta:
    def __init__(self, numero, cliente, saldo_inicial = 0):
        self.__numero = numero
        self.__cliente = cliente 
        self.__saldo = saldo_inicial
        self.__extrato = []

    @property

    def saldo(self):
        return self.__saldo
    
    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__extrato.append (f"Foi depositado R$: {valor}")
    
    @abstractmethod

    def transferir (self, valor, destino_conta):
        destino_conta.depositar (valor)
        self.__extrato.append (f"Transferência efetuado para a conta {destino_conta.numero}")

class Cliente:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha 
        self.__contas = []


    def certificar (self, senha):
        return self.__senha == senha
    
    def adicionar_conta (self, conta):
        self.__contas.append (conta)

class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = []

    def adicionar_cliente (self):
        self.__clientes.append (cliente)

class Extrato:
    def __init__(self, conta):
        self.__conta = conta 

    def mostrar_extrato (self):
        for item in self.__conta.extrato:
            print (item)

