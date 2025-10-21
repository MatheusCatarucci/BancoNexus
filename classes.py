import abc

class Conta(ABS):
    @abstractmethod
    def sacar():
        pass
    
class Conta_Corrente(Conta):
    def sacar():
        pass
    
class Conta_Poupança(Conta):
    def sacar():
        pass
    
class Banco(ABS):
    