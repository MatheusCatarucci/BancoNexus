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

class Banco:
    def __init__(self):
        pass

class Cliente:
    def __init__(self):
        pass

