import socket

students = {
    "Андрееви": "Иван",
    "Марасакин": "Гришка",
    "Маркина": "Ксения",
    "Метальников": "Максим",
    "Никитина": "Маргарита",
    "Пегов": "Александр",
    "Подмарькова": "Виктория",
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    serversocket.bind(('', 7777))
    serversocket.listen(5)
    print("Сервер запущен на порту 7777")

    while True:
        connect, address = serversocket.accept()
        print(f"Подключение от {address}")

        data = connect.recv(1024).decode('utf-8').strip()
        print(f"Клиент прислал: {data}")

        if data in students:
            response = f"Привет, {students[data]}"
        else:
            response = "Ошибка: Фамилия не найдена в списке студентов"

        connect.send(response.encode('utf-8'))
        connect.close()
        print("Сервер закрыл соединение")