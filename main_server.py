# Trabalho em grupo feito por discentes da disciplina de redes II
# Rafael Lucas Fernandes Soares
# Renata Cristina Araújo
# Igor Miranda da Silva
# Walter Magno Lopes

# Docente 
# Alessandro Vivas Andrade

from factory import ServerFactory as sf

if __name__ == "__main__":
    
    typeProtocol = input("Digite o tipo de protocolo (TCP ou UDP): ").lower()

    # Criando o servidor
    server = sf.create_server(typeProtocol, "localhost", 8000)

    # Iniciando o servidor
    server.run()

