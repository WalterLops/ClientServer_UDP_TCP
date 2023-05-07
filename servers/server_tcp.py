from iserver import IServer  # Importa a classe IServer do módulo iserver
import socket  # Importa o módulo socket do Python

class TCPServer(IServer):  # Cria uma nova classe chamada TCPServer que herda da classe IServer
    def __init__(self, host, port):  # Define um método construtor que recebe os parâmetros "host" e "port"
        self.host = host  # Atribui o valor de "host" ao atributo "self.host"
        self.port = port  # Atribui o valor de "port" ao atributo "self.port"

    def run(self):  # Define um método chamado "run" sem parâmetros
        print("O servidor iniciou!")  # Imprime uma mensagem indicando que o servidor iniciou
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Cria um objeto de socket com o protocolo AF_INET e o tipo SOCK_STREAM
            s.bind((self.host, self.port))  # Associa o socket ao endereço e porta especificados pelo construtor
            s.listen()  # Coloca o socket em modo de escuta
            conn, addr = s.accept()  # Aceita a conexão do cliente e retorna um objeto de conexão e o endereço do cliente
            with conn:  # Cria um bloco de código para lidar com a conexão do cliente
                print('Conexão estabelecida por', addr)  # Imprime o endereço do cliente que estabeleceu a conexão
                while True:  # Cria um loop infinito para lidar com as mensagens do cliente
                    data = conn.recv(1024)  # Recebe uma mensagem do cliente com um tamanho máximo de 1024 bytes
                    if not data:  # Verifica se a mensagem está vazia
                        break  # Sai do loop se a mensagem estiver vazia
                    stock_quote = self.get_stock_quote(data.decode())  # Chama o método "get_stock_quote" para obter a cotação da ação solicitada pelo cliente
                    conn.sendall(stock_quote.encode())  # Envia a cotação da ação de volta para o cliente

    def get_stock_quote(self, symbol):  # Define um método chamado "get_stock_quote" que recebe um parâmetro "symbol"
        print(f"Mensagem recebida do cliente: {symbol}")  
        # Aqui iria a lógica para obter a cotação da ação do servidor
        return f"Oi cliente, tudo bem? Obrigado pela mensagem. Segue a cotação da ação solicitada."  # Retorna uma mensagem de resposta ao cliente com a cotação da ação solicitada
