import socket
import select
import json

HOST = 'localhost'
PORT = 8080
BACKLOG_SIZE = 17
SELECT_TIMEOUT = None   # None для нескінченного циклу в select
RECEIVE_BUFF_SIZE = 1024    # bytes
CODING = "utf-8"

def deparsing_header(http):
    a = json.loads(http.decode())
    Headlines, body = a.split('\n\n')
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

# Функція для обробки запиту
def work(payload):
    a = int(payload)
    result = a*a
    return result

def parsing(http):
    res = json.loads(http.decode(CODING))
    headlines, body = res.split("\n\n")
    return body


def http(message, host, port, version):
    content_type="text/html"
    http = ""

    http += f"POST HTTP/{version} .0\n"
    http += f"Host: {host}:{port}\n"
    http += f"Content-Type: {content_type}\n"
    http += f"Content-Length: {len(str(message)) + 1}"
    http += '\n\n'
    http += f"{message}\n"
    return http


def main():
    # Створення та конфігурація серверного сокету
    serverSocket = socket.socket()
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(BACKLOG_SIZE)

    readList = [serverSocket]
    writeList = []
    exceptionalList = [serverSocket]

    # Ініціалізація контейнера для відповідей
    responsesMap = {}
    # Головний цикл додатку
    while True:
        # Виконуємо select для отримання змін в відслідковуваних сокетах
        readChanges, writeChanges, exceptionalChanges = select.select(readList, writeList, exceptionalList, SELECT_TIMEOUT)

        # Обробляємо сокети які готові для вичитування інформації
        for rSocket in readChanges:

            if rSocket is serverSocket:
                # Приймаємо підключення від клієнта
                client, _ = rSocket.accept()
                # Поміщаємо клієнт в список сокетів що очікують приходу даних
                readList.append(client)
                exceptionalList.append(client)
            else:
                payload = rSocket.recv(RECEIVE_BUFF_SIZE)

                if payload is not None:
                    # Дані прийшли повнюстю, помічаємо сокет під видалення з цього списку
                    readList.remove(rSocket)
                    # Обробляємо запит
                    response =  work(parsing(payload))
                    # Зберігаємо результат запиту, щоб повернути для клієнта
                    responsesMap[rSocket] = json.dumps(http(response, HOST, PORT, "1.0")).encode(CODING)
                    # Поміщаємо сокет в список для перевірки на можливість запису
                    writeList.append(rSocket)


        # Обробляємо сокети які готові до запису інформації
        for wSocket in writeChanges:
            # Отримання збереженої відповіді для клієнта
            response = responsesMap.get(wSocket)
            if response is not None:
                # Відправляємо відповідь клієнту
                wSocket.send(response)
                # Очищаємо структури з інформацією про клієнта
                responsesMap.pop(wSocket)
                writeList.remove(wSocket)
                exceptionalList.remove(wSocket)
                # Закриваємо клієнтський сокет
                wSocket.close()

        # Обробляємо сокети що згенерували "exceptional condition"
        for eSocket in exceptionalChanges:
            # Видаляємо сокет з очікуючих на читання
            if eSocket in readList:
                readList.pop(eSocket)
            # Видаляємо відповідь згенеровану для сокету
            if eSocket in writeList:
                responsesMap.pop(eSocket)
                writeList.remove(eSocket)

            if eSocket is serverSocket:
                break
            else:
                exceptionalList.remove(eSocket)


if __name__ == '__main__':
    main()
