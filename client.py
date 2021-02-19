import socket
import json


def decoding(data):
    my_result = json.loads(data.decode(CODE))
    print(my_result)


def client_inquiry(client, client_input):
    client.send(json.dumps(client_input).encode(CODE))
    data = client.recv(2048)
    decoding(data)




HOST = "localhost"
PORT = 3567
CODE = "utf-8"


client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((HOST, PORT))
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((HOST, PORT))
client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client3.connect((HOST, PORT))
client4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client4.connect((HOST, PORT))
client5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client5.connect((HOST, PORT))
client6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client6.connect((HOST, PORT))
client7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client7.connect((HOST, PORT))
client8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client8.connect((HOST, PORT))
client9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client9.connect((HOST, PORT))
client10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client10.connect((HOST, PORT))
client11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client11.connect((HOST, PORT))
client12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client12.connect((HOST, PORT))
client13 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client13.connect((HOST, PORT))
client14 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client14.connect((HOST, PORT))
client15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client15.connect((HOST, PORT))
client16 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client16.connect((HOST, PORT))
client17 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client17.connect((HOST, PORT))



client_input1 = (input("input your N:"))
client_input2 = (input("input your N:"))
client_input3 = (input("input your N:"))
client_input4 = (input("input your N:"))
client_input5 = (input("input your N:"))
client_input6 = (input("input your N:"))
client_input7 = (input("input your N:"))
client_input8 = (input("input your N:"))
client_input9 = (input("input your N:"))
client_input10 = (input("input your N:"))
client_input11 = (input("input your N:"))
client_input12 = (input("input your N:"))
client_input13 = (input("input your N:"))
client_input14 = (input("input your N:"))
client_input15 = (input("input your N:"))
client_input16 = (input("input your N:"))
client_input17 = (input("input your N:"))

client_inquiry(client1, client_input1)
client_inquiry(client2, client_input2)
client_inquiry(client3, client_input3)
client_inquiry(client4, client_input4)
client_inquiry(client5, client_input5)
client_inquiry(client6, client_input6)
client_inquiry(client7, client_input7)
client_inquiry(client8, client_input8)
client_inquiry(client9, client_input9)
client_inquiry(client10, client_input10)
client_inquiry(client11, client_input11)
client_inquiry(client12, client_input12)
client_inquiry(client13, client_input13)
client_inquiry(client14, client_input14)
client_inquiry(client15, client_input15)
client_inquiry(client16, client_input16)
client_inquiry(client17, client_input17)









