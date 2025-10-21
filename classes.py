from abc import abstractmethod, ABC

class Conta(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass
    
class Conta_Corrente(Conta):
    def sacar(self, valor):
        pass
    
class Conta_Poupança(Conta):
    def sacar(self, valor):
        pass
    
class Banco():
    