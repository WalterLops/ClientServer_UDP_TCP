
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'servers')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'clients')))

from client_tcp import TCPClient
from client_udp import UDPClient
from server_tcp import TCPServer
from server_udp import UDPServer

class ClientFactory:
    @staticmethod
    def create_client(protocol, host, port):
        if protocol == "tcp":
            return TCPClient(host, port)
        elif protocol == "udp":
            return UDPClient(host, port)
        else:
            raise ValueError(f"Protocolo {protocol} não é suportado.")

class ServerFactory:
    @staticmethod
    def create_server(protocol, host, port):
        if protocol == "tcp":
            return TCPServer(host, port)
        elif protocol == "udp":
            return UDPServer(host, port)
        else:
            raise ValueError(f"Protocolo {protocol} não é suportado.")

