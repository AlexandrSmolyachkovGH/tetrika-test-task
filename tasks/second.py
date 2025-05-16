import csv

import requests
from bs4 import BeautifulSoup
import time


class Config:
    BASE_URL = "https://ru.wikipedia.org"
    PATH_URL = "/wiki/Категория:Животные_по_алфавиту"


conf = Config()


def fetch_html(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.encoding = 'utf-8'
    return response.text


def parse_animals_from_html(html: str, result: dict) -> BeautifulSoup:
    soup = BeautifulSoup(html, 'html.parser')
    for li in soup.select('#mw-pages .mw-content-ltr li a'):
        letter = li.text[:1].upper()
        if letter.isalpha() and 'А' <= letter <= 'Я':
            result[letter] = result.get(letter, 0) + 1
    return soup


def parse_all_pages(start_url: str, result: dict) -> None:
    next_url = start_url
    while next_url:
        print(f"Парсинг: {next_url}")

        html = fetch_html(next_url)
        soup = parse_animals_from_html(html, result)

        next_link = soup.find('a', string="Следующая страница")
        if next_link:
            next_url = conf.BASE_URL + next_link['href']
            time.sleep(0.5)
        else:
            next_url = None


if __name__ == "__main__":
    result = {}
    parse_all_pages(start_url=conf.BASE_URL + conf.PATH_URL, result=result)

    with open(file='beasts.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Буква', 'Количество'])
        for letter in sorted(result):
            writer.writerow([letter, result.get(letter)])
