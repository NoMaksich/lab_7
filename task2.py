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

with socket.socket(type=socket.SOCK_DGRAM) as serversocket:
    serversocket.bind(('', 7777))
    print("Сервер запущен на порту 7777")

    while True:
        data, address = serversocket.recvfrom(1024)
        data = data.decode('utf-8').strip()

        print(f"Адрес клиента: {address}")
        print(f"Клиент прислал: {data}")

        if data in students:
            answer = f"Привет, {students[data]}"
        else:
            answer = "Ошибка: Фамилия не найдена в списке студентов"

        serversocket.sendto(response.encode('utf-8'), address)
