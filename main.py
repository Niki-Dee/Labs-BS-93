import socket
import json
from threading import Thread


def function (N, my_dict):
    number = int(N)
    for key, elem in my_dict.items():
       if elem == N:
            print(f'{key}: {number*number}')

HOST = "localhost"
PORT = 1234
CODE = "utf-8"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))

server.listen(5)
print("Server is listening !")

while True:
    user_socket, address = server.accept()
    print(f"User {address} connected !")

    user_socket.send("You are connected !".encode(CODE))
    data = user_socket.recv(2048)
    my_json = data.decode(CODE)
    my_dict = json.loads(my_json)

    t1 = Thread(target=function, args=(my_dict["Запит №1"], my_dict) )
    t2 = Thread(target=function, args=(my_dict["Запит №2"], my_dict))
    t3 = Thread(target=function, args=(my_dict["Запит №3"], my_dict))
    t4 = Thread(target=function, args=(my_dict["Запит №4"], my_dict))
    t5 = Thread(target=function, args=(my_dict["Запит №5"], my_dict))
    t6 = Thread(target=function, args=(my_dict["Запит №6"], my_dict))
    t7 = Thread(target=function, args=(my_dict["Запит №7"], my_dict))
    t8 = Thread(target=function, args=(my_dict["Запит №8"], my_dict))
    t9 = Thread(target=function, args=(my_dict["Запит №9"], my_dict))
    t10 = Thread(target=function, args=(my_dict["Запит №10"], my_dict))
    t11 = Thread(target=function, args=(my_dict["Запит №11"], my_dict))
    t12 = Thread(target=function, args=(my_dict["Запит №12"], my_dict))
    t13 = Thread(target=function, args=(my_dict["Запит №13"], my_dict))
    t14 = Thread(target=function, args=(my_dict["Запит №14"], my_dict))
    t15 = Thread(target=function, args=(my_dict["Запит №15"], my_dict))
    t16 = Thread(target=function, args=(my_dict["Запит №16"], my_dict))
    t17 = Thread(target=function, args=(my_dict["Запит №17"], my_dict))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()











