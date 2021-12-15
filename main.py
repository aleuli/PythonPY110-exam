from random import randint
import random
import json
from faker import Faker
from conf import model


def main():
    """

    :return: Записываем 100 книг в файл .txt
    """
    with open("book_dict.txt", "w", encoding="utf-8") as f:
        name_book = []
        for _ in range(100):
            name_book.append(next(generator_book()))
        json.dump(name_book, f, ensure_ascii=False, indent=4)


def generator_book(pk=1):
    """

    :param pk: Счетчик - который увеличивается с каждой книгой
    :return: возвращаем данные о книге
    """
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
    """

    :return: рандомно выбираем одну из пяти книг
    """
    with open("books.txt", "rt", encoding="utf-8") as f:
        return random.choice(f.readlines())


def generator_year():
    """

    :return: рандомно указываем год от 2000 до 2050
    """
    return randint(2000, 2050)


def generator_pages():
    """

    :return: рандомно указывает количество страниц от 1 до 1000
    """
    return randint(1, 1000)


def generator_fake():
    """

    :return: рандомно выдаем isbn13
    """
    fake = Faker()
    return fake.isbn13()


def generator_raiting():
    """

    :return: рандомно выдаем рейтинг книги и округляем до первой цифры после запятой
    """
    return round(random.uniform(0.0, 5.0), 1)


def generator_price():
    """

    :return: рандомно выдаем прайс книги и округляем до первой цифры после запятой
    """
    return round(random.uniform(0.0, 10000.0), 1)


def generator_author():
        """

        :return: Возвращаем автора. Рандомом выдается от 1 до 3 авторов книги.
        """
        fake = Faker()
        list_ = []
        for _ in range(randint(1, 3)):
            list_.append(fake.name())
        return list_


if __name__ == '__main__':
    main()
