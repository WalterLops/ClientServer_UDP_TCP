import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'servers')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'clients')))

from client_tcp import TCPClient
from client_udp import UDPClient
from server_tcp import TCPServer
from server_udp import UDPServer

class ClientFactory:
    PROTOCOL_MAP = {
        "tcp": TCPClient,
        "udp": UDPClient
    }

    @staticmethod
    def create_client(protocol, host, port):
        if protocol not in ClientFactory.PROTOCOL_MAP:
            raise ValueError(f"Protocolo {protocol} não é suportado.")
        
        client_class = ClientFactory.PROTOCOL_MAP[protocol]
        return client_class(host, port)

class ServerFactory:
    PROTOCOL_MAP = {
        "tcp": TCPServer,
        "udp": UDPServer
    }

    @staticmethod
    def create_server(protocol, host, port):
        if protocol not in ServerFactory.PROTOCOL_MAP:
            raise ValueError(f"Protocolo {protocol} não é suportado.")
        
        server_class = ServerFactory.PROTOCOL_MAP[protocol]
        return server_class(host, port)
