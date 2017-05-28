import socket
import _thread
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5555            # Porta que o Servidor esta

def connected(con, client):
    print ('Conectado por', client)
    while True:
        message = con.recv(1024)
        if not message: break
        print (client, message.decode())

    print ('Finalizando conexao do cliente', client)
    con.close()
    _thread.exit()

def openConnection():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = (HOST, PORT)
    tcp.bind(server)
    tcp.listen(1)
    print("servidor aberto em", server)
    createThread(tcp)

def createThread(tcp):
    while True:
        con, client = tcp.accept()
        _thread.start_new_thread(connected(con, client))
    tcp.close()

def startServer():
    openConnection()

