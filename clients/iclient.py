# Trabalho em grupo feito por discentes da disciplina de redes II
# Rafael Lucas Fernandes Soares
# Renata Cristina Araújo
# Igor Miranda da Silva
# Walter Magno Lopes

# Docente 
# Alessandro Vivas Andrade

import abc  

class IClient(abc.ABC):  # Cria uma nova classe chamada IClient que herda de abc.ABC
    @abc.abstractmethod  # Indica que o método abaixo é abstrato e deve ser implementado nas classes filhas
    def request_stock_quote(self, symbol):  # Define um método chamado "request_stock_quote" que recebe um parâmetro "symbol"
        pass  # Indica que o método não tem corpo e não faz nada
