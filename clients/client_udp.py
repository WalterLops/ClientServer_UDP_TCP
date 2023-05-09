# Trabalho em grupo feito por discentes da disciplina de redes II
# Rafael Lucas Fernandes Soares
# Renata Cristina Araújo
# Igor Miranda da Silva
# Walter Magno Lopes

# Docente 
# Alessandro Vivas Andrade

from iclient import IClient    # importa a interface IClient e utiliza ela como base para a implementação da classe
import socket                  

class UDPClient(IClient):       # define a classe UDPClient que implementa a interface IClient
    def __init__(self, host, port):   # construtor que recebe as informações de host e porta para a conexão
        self.host = host                # armazena o host recebido como atributo da classe
        self.port = port                # armazena a porta recebida como atributo da classe
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # cria um objeto socket para conexão UDP

    def request_stock_quote(self, symbol):    # método para fazer a requisição da cotação da ação
        message = symbol.encode()             # converte a mensagem para bytes
        while True:                           # loop para tentar enviar a mensagem e receber a resposta do servidor
            self.sock.sendto(message, (self.host, self.port))    # envia a mensagem para o servidor
            self.sock.settimeout(5)                              # define um timeout de 5 segundos
            try:
                data, server = self.sock.recvfrom(1024)          # tenta receber a resposta do servidor
            except socket.timeout:                                # caso ocorra um timeout, tenta enviar novamente
                continue
            else:                                                # caso receba a resposta, retorna a mensagem decodificada
                return data.decode()
