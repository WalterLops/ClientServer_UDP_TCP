from factory import ServerFactory as sf

if __name__ == "__main__":
    
    typeProtocol = input("Digite o tipo de protocolo (TCP ou UDP): ").lower()

    # Criando o servidor TCP
    server = sf.create_server(typeProtocol, "localhost", 8000)

    # Iniciando o servidor TCP
    server.run()

