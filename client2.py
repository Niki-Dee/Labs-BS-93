from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
import json
from threading import Thread
import random

HOST = "localhost"
PORT = 8080
QUEUE_LEN = 17
CODING = "utf-8"


def parsing_header(http1):
    Headlines, body = http1.split('\n\n')
    Head = Headlines.split('\n')
    head_dict = {"Metod": Head[0].split()[0],
                 "Url": Head[0].split()[1],
                 "Host": (Head[1].split()[1]).split(':')[0],
                 "Port": (Head[1].split()[1]).split(':')[1],
                 "Type": (Head[2].split()[1]).split('/')[0],
                 "Version": (Head[2].split()[1]).split('/')[1],
                 "Length": Head[3].split()[1]
                 }
    print(head_dict)
    return head_dict


def parsing(http1):
    res = http1
    headlines, body = res.split("\n\n")
    return body


def read_from_socket(sock):
    while True:
        buff_size =sock.getsockopt(SOL_SOCKET, SO_RCVBUF)
        data = json.loads((sock.recv(buff_size)).decode())
        return data


def http(message, host, port, version):
    content_type="text/html"
    http = ""

    http += f"GET HTTP/{version} .0\n"
    http += f"Host: {host}:{port}\n"
    http += f"Content-Type: {content_type}\n"
    http += f"Content-Length: {len(str(message)) + 1}"
    http += '\n\n'
    http += f"{message}\n"
    return http


def client(data_enter, index, data_exit):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(json.dumps(http(data_enter[index], HOST, PORT, "1.0")).encode(CODING))
    result = read_from_socket(client)
    data_exit[index] = parsing(result)
    parsing_header(result)
    client.close()


def create_input():
    input_mass = []
    for i in range(QUEUE_LEN):
        input_mass.append(random.randint(1,30))
    return input_mass


def print_list(lst):
    for i in range(len(lst)):
        print(f"{i+1} : {lst[i]}")


def main():
    input_list = create_input()
    print_list(input_list)
    output_list = input_list
    print("")
    task_list = []
    for i in range(QUEUE_LEN):
        t = Thread(target=client, args=(input_list, i, output_list))
        t.start()
        task_list.append(t)

    for t in task_list:
        t.join()

    print_list(output_list)

if __name__ == '__main__':
    main()