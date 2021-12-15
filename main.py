from random import randint
import random
import json
from faker import Faker
from conf import model


def generator_book(pk=1):
    while True:

        dict_book = {
            "model": "shop_final.book",
            "pk": 1,
            "fields": {
                "title": "test_book",
                "year": 2020,
                "pages": 123,
                "isbn13": "978-1-60487-647-5",
                "rating": 5,
                "price": 123456.0,
                "author": [
                    "test_author_1",
                    "test_author_2"
                ]
            }
        }
        yield dict_book
        pk += 1







def generator_title():
    with open("books.txt", "rt", encoding="utf-8") as f:
        return random.choice(f.readlines())


def generator_year():
    return randint(2000, 2050)


def generator_pages():
    return randint(1, 1000)


def generator_fake():
    fake = Faker()
    return fake.isbn13()


def generator_raiting():
    return round(random.uniform(0.0, 5.0), 1)


def generator_price():
    return round(random.uniform(0.0, 10000.0), 1)


def generator_author():
    fake = Faker()
    list_ = []
    for _ in range(randint(1, 3)):
        list_.append(fake.name())
    return list_


if __name__ == '__main__':




