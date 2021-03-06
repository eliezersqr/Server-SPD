import socket
from notebook.notebookapp import raw_input

HOST = '127.0.0.1'     # Server ip adress
PORT = 5556            # Server port

def startConnection(self):
    createConnection()

def createConnection():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = (HOST, PORT)
    tcp.connect(server)
    print('Para sair digite exit\n')
    SynchronizationMessage(tcp)


def SynchronizationMessage(tcp):
    message = raw_input("Digite uma frase: ")

    while message != 'exit':
        channel = raw_input("Digite um canal para comunicação: ")
        message = (message + "-").encode()
        tcp.send(message)
        channel = channel.encode()
        tcp.send(channel)
        message = raw_input("Digite uma frase: ")
    tcp.close()