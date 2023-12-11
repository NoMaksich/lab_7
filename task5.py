from html.parser import HTMLParser
import urllib.request
from urllib.parse import urljoin

start_url = 'https://beda.pnzgu.ru/anatoly/'

class ImageParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.img_urls = []
        self.link_urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr, value in attrs:
                if attr == 'src':
                    img_url = urljoin(self.base_url, value)
                    self.img_urls.append(img_url)
        elif tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    link_url = urljoin(self.base_url, value)
                    self.link_urls.append(link_url)

def download_images(url):
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    parser = ImageParser(url)
    parser.feed(html_content)

    for img_url in parser.img_urls:
        img_name = img_url.split('/')[-1]

        if img_name.endswith('.webp') or '.' not in img_name:
            img_response = urllib.request.urlopen(img_url)
            with open(f'images/{img_name}', 'wb') as img_file:
                img_file.write(img_response.read())
            print(f"Сохранено изображение: {img_name}")

    for link_url in parser.link_urls:
        download_images(link_url)

download_images(start_url)
print("Загрузка изображений завершена.")
