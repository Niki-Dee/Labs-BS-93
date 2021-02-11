import socket
import json


HOST = "localhost"
PORT = 1234
CODE = "utf-8"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

while True:
    data = client.recv(2048)
    print(data.decode(CODE))

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


    dictionary = {
        "Запит №1": client_input1,
        "Запит №2": client_input2,
        "Запит №3": client_input3,
        "Запит №4": client_input4,
        "Запит №5": client_input5,
        "Запит №6": client_input6,
        "Запит №7": client_input7,
        "Запит №8": client_input8,
        "Запит №9": client_input9,
        "Запит №10": client_input10,
        "Запит №11": client_input11,
        "Запит №12": client_input12,
        "Запит №13": client_input13,
        "Запит №14": client_input14,
        "Запит №15": client_input15,
        "Запит №16": client_input16,
        "Запит №17": client_input17,
    }

    my_json = json.dumps(dictionary)
    client.send(my_json.encode(CODE))



