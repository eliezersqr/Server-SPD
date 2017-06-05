import socket
import os
import sys
HOST = '127.0.0.1'            # Endereco IP do Servidor
PORT = 5556           # Porta que o Servidor esta

def startConnectionServer(self):

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = (HOST, PORT)

    try:
        tcp.bind(server)
    except socket.error as msg:
        print("Erro ao abrir o servidor!", msg)
        sys.exit(1)
        tcp.close()

    tcp.listen(1)
    print("Servidor iniciado")
    while True:
        receiveConnection(tcp)
    tcp.close()

def receiveConnection(tcp):
    con, cliente = tcp.accept()
    pid = os.fork()
    print("numero do PID do processo criado", pid)
    if pid == 0:
        tcp.close()
        print('Conectado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            print(cliente, msg.decode())
        print('Finalizando conexao do cliente', cliente)
        con.close()
        sys.exit(0)
    else:
        con.close()
