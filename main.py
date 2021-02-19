import socket
import json
from threading import Thread
import time


def function(N, user_socket, CODE, index):
    number = int(N)
    result = f"Відповідь на запит {index}: {number*number}"
    user_socket.send(json.dumps(result).encode(CODE))


HOST = "localhost"
PORT = 3567
CODE = "utf-8"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))

server.listen()
print("Server is listening !")
index = 1
while True:
    user_socket, address = server.accept()

    data = user_socket.recv(2048)
    number = json.loads(data.decode(CODE))

    t1 = Thread(target=function, args=(number, user_socket, CODE,index))
    t1.start()
   # time.sleep(1)
    index += 1











