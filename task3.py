import http.client

host = 'beda.pnzgu.ru'
path = '/anatoly/'
conn = http.client.HTTPSConnection(host)
conn.request('GET', path, headers={'User-Agent': 'Python program'})
response = conn.getresponse()

if response.status == 200:
    content = response.read()
    with open('index.html', 'wb') as file:
        file.write(content)
    print("Файл успешно записан")
else:
    print(f"Ошибка при запросе: {response.status}")

conn.close()
