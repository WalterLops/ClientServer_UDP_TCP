
from iserver import IServer # Biblioteca para criar o servidor
import socket # Biblioteca para trabalhar com sockets

# Criando a classe UDPServer e herdando da classe IServer
class UDPServer(IServer):
    def __init__(self, host, port):
        self.host = host # Armazenando o endereço do host
        self.port = port # Armazenando a porta do host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criando o socket UDP
        self.sock.bind((self.host, self.port)) # Vinculando o socket ao endereço e porta especificados

    def run(self):
        print("O servidor iniciou!") # Exibindo mensagem de início do servidor
        
        while True: # Executando indefinidamente
            data, addr = self.sock.recvfrom(1024) # Recebendo dados e endereço do cliente
            stock_quote = self.get_stock_quote(data.decode()) # Obtendo a cotação da ação solicitada
            self.sock.sendto(stock_quote.encode(), addr) # Enviando a cotação da ação para o cliente

    def get_stock_quote(self, symbol):
        print(f"Mensagem recebida do cliente: {symbol}") # Exibindo mensagem recebida do cliente
        
        # Aqui iria a lógica para obter a cotação da ação do servidor
        return f"Oi cliente, tudo bem? Obrigado pela mensagem. Segue a cotação da ação solicitada." # Retornando mensagem com a cotação da ação