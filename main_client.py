from factory import ClientFactory as cf

if __name__ == "__main__":
    
    typeProtocol = input("Digite o tipo de protocolo (TCP ou UDP): ").lower()
    
    # Criando o cliente
    client = cf.create_client(typeProtocol, "localhost", 8000)

    # Solicitando a cotação da ação PETR4.SA para o servidor
    response = client.request_stock_quote("Oi servidor, tudo bem? Solicito a cotação da Ação PETR4.SA")

    # Exibindo a cotação da ação PETR4.SA recebida do servidor
    print(response)

    