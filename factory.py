# Trabalho em grupo feito por discentes da disciplina de redes II
# Rafael Lucas Fernandes Soares
# Renata Cristina Araújo
# Igor Miranda da Silva
# Walter Magno Lopes

# Docente 
# Alessandro Vivas Andrade

import os  # importando o módulo os para lidar com recursos do sistema operacional
import sys  # importando o módulo sys para ter acesso a variáveis e funções relacionadas ao Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'servers')))  # adicionando o caminho absoluto do diretório 'servers' ao caminho do sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'clients')))  # adicionando o caminho absoluto do diretório 'clients' ao caminho do sistema

from client_tcp import TCPClient  # importando a classe TCPClient do arquivo client_tcp.py
from client_udp import UDPClient  # importando a classe UDPClient do arquivo client_udp.py
from server_tcp import TCPServer  # importando a classe TCPServer do arquivo server_tcp.py
from server_udp import UDPServer  # importando a classe UDPServer do arquivo server_udp.py

class ClientFactory:
    PROTOCOL_MAP = {
        "tcp": TCPClient,  # mapeando o protocolo "tcp" à classe TCPClient
        "udp": UDPClient  # mapeando o protocolo "udp" à classe UDPClient
    }

    @staticmethod  # método estático que retorna uma instância da classe de cliente específica para um determinado protocolo
    def create_client(protocol, host, port):
        if protocol not in ClientFactory.PROTOCOL_MAP:  # verificando se o protocolo passado é suportado
            raise ValueError(f"Protocolo {protocol} não é suportado.")
        
        client_class = ClientFactory.PROTOCOL_MAP[protocol]  # recuperando a classe de cliente correspondente ao protocolo
        return client_class(host, port)  # criando e retornando uma instância da classe de cliente passando os argumentos de host e porta

class ServerFactory:
    PROTOCOL_MAP = {
        "tcp": TCPServer,  # mapeando o protocolo "tcp" à classe TCPServer
        "udp": UDPServer  # mapeando o protocolo "udp" à classe UDPServer
    }

    @staticmethod  # método estático que retorna uma instância da classe de servidor específica para um determinado protocolo
    def create_server(protocol, host, port):
        if protocol not in ServerFactory.PROTOCOL_MAP:  # verificando se o protocolo passado é suportado
            raise ValueError(f"Protocolo {protocol} não é suportado.")
        
        server_class = ServerFactory.PROTOCOL_MAP[protocol]  # recuperando a classe de servidor correspondente ao protocolo
        return server_class(host, port)  # criando e retornando uma instância da classe de servidor passando os argumentos de host e porta