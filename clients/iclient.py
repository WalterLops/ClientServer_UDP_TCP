import abc  

class IClient(abc.ABC):  # Cria uma nova classe chamada IClient que herda de abc.ABC
    @abc.abstractmethod  # Indica que o método abaixo é abstrato e deve ser implementado nas classes filhas
    def request_stock_quote(self, symbol):  # Define um método chamado "request_stock_quote" que recebe um parâmetro "symbol"
        pass  # Indica que o método não tem corpo e não faz nada
