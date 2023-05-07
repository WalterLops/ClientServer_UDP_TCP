from abc import ABC, abstractmethod

class IServer(ABC):
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def get_stock_quote(self, symbol):
        pass
