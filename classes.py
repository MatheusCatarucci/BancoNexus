from abc import abstractmethod, ABC
from datetime import *

# Classe abstrata que define as operações financeiras básicas
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
    def transferir(self, valor, conta_destino):
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
        return None  # Retorna None se o cliente não for encontrado


# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, nome, cpf, contas):
        self.__nome = nome  # Nome do cliente
        self.__cpf = cpf    # CPF do cliente
        self.__contas = []  # Lista de contas do cliente (pode ter mais de uma)

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


# Classe abstrata que representa uma conta bancária genérica
class Conta(OperacoesFinanceiras, ABC):
    def __init__(self, numero, saldoInicial=0):
        self.__numero = numero           # Número da conta
        self.__saldo = saldoInicial      # Saldo inicial da conta
        self.__extrato = []              # Lista para registrar operações (extrato)

    # Retorna o número da conta
    def getNumero(self):
        return self.__numero

    # Retorna o saldo atual
    def getSaldo(self):
        return self.__saldo

    # Retorna o extrato de operações
    def getExtrato(self):
        return self.__extrato


# Classe que representa o extrato de uma conta (registro das operações)
class Extrato:
    def __init__(self):
        self.__operacoes = []  # Lista de dicionários com tipo, valor e data

    # Adiciona uma operação ao extrato (saque, depósito, etc.)
    def adicionarOperacao(self, tipo, valor):
        self.__operacoes.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now()  # Registra a data e hora da operação
        })

    # Exibe o extrato formatado no console
    def mostrarExtrato(self):
        print("=== Extrato ===")
        for operacao in self.__operacoes:
            print(
                f"{operacao['data'].strftime('%d/%m/%Y %H:%M')} - {operacao['tipo']}: R${operacao['valor']:.2f}"
            )


# Classe concreta que representa uma conta corrente (implementa os métodos abstratos)
class ContaCorrente(Conta):  ## Ainda não finalizada
    def sacar(self, valor):
        # Verifica se o valor informado é válido
        if valor <= 0:
            print("Valor inválido para saque.")
            return

        # Subtrai o valor do saldo (acessando atributo privado via nome mangled)
        self._Conta__saldo -= valor

        # Registra a operação no extrato (acessando o objeto de extrato)
        self._Conta__extrato.adicionarOperacao("Saque", valor)

        # Exibe mensagem de confirmação com o saldo atualizado
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.getSaldo():.2f}")
