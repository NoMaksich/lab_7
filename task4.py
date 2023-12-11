import http.client
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr, value in attrs:
                if attr == 'src':
                    img_urls.append(value)

host = 'beda.pnzgu.ru'
path = '/anatoly/'

conn = http.client.HTTPSConnection(host)
conn.request('GET', path, headers={'User-Agent': 'Python program'})
response = conn.getresponse()

if response.status == 200:
    content = response.read().decode('utf-8')

    img_urls = []

    parser = ImageParser()
    parser.feed(content)
    parser.close()

    base_url = f'https://{host}'

    for img_url in img_urls:
        full_img_url = base_url + img_url
        conn.request('GET', full_img_url)
        img_response = conn.getresponse()
        if img_response.status == 200:
            img_content = img_response.read()
            img_filename = img_url.split('/')[-1]
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_content)
            print(f"Изображение '{img_filename}' успешно загружено")
        else:
            print(f"Ошибка при загрузке изображения: {img_response.status}")
else:
    print(f"Ошибка при запросе: {response.status}")

conn.close()
