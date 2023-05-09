from abc import ABC, abstractmethod  # importando a classe ABC e o decorador abstractmethod

class IServer(ABC):  # definindo uma classe abstrata IServer que herda de ABC
    
    @abstractmethod  # decorando um método abstrato
    def run(self):
        pass
    
    @abstractmethod  # decorando outro método abstrato
    def get_stock_quote(self, symbol):
        pass  # indicando que o corpo do método é vazio e não faz nada