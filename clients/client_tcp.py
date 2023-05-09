# Trabalho em grupo feito por discentes da disciplina de redes II
# Rafael Lucas Fernandes Soares
# Renata Cristina Araújo
# Igor Miranda da Silva
# Walter Magno Lopes

# Docente 
# Alessandro Vivas Andrade

from iclient import IClient   
import socket  

class TCPClient(IClient):   
    def __init__(self, host, port):   # inicializa o host e a porta do servidor
        self.host = host
        self.port = port

    def request_stock_quote(self, symbol):   # implementa o método da interface para fazer uma requisição de cotação de ações
        try:   # tenta estabelecer uma conexão com o servidor
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))   # faz a conexão com o servidor
                s.sendall(symbol.encode())   # envia a requisição para o servidor
                data = s.recv(1024)   # recebe a resposta do servidor
                return data.decode()   # retorna a resposta decodificada
        except ConnectionRefusedError as e:   # trata uma possível exceção caso a conexão seja recusada pelo servidor
            print(f"Log: {e} \nExtra: possível protocolo enviado de forma incorreta")   # exibe uma mensagem de erro no console
            pass   # continua a execução do programa
