import socket
import os
import sys
HOST = '127.0.0.1'             # Endereco IP do Servidor
PORT = 5556           # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    print (pid)
    if pid == 0:
        tcp.close()
        print ('Conectado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            print (cliente, msg.decode())
        print ('Finalizando conexao do cliente', cliente)
        con.close()
        sys.exit(0)
    else:
        con.close()
