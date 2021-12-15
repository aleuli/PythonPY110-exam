from random import randint
import random
import json
from faker import Faker
from conf import model


def main():
    with open("book_dict.txt", "w", encoding="utf-8") as f:
        name_book = []
        for _ in range(100):
            name_book.append(next(generator_book()))
        j_dumps = json.dumps(name_book)
        f.write(j_dumps)


def generator_book(pk=1):
    while True:
        dict_book = {
            "model": model,
            "pk": pk,
            "fields": {
                "title": generator_title(),
                "year": generator_year(),
                "pages": generator_pages(),
                "isbn13": generator_fake(),
                "rating": generator_raiting(),
                "price": generator_price(),
                "author": [
                    generator_author()
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
    main()