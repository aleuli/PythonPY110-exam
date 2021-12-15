from random import randint
import random
import json
from faker import Faker
from conf import model


def generator_book(pk=1):
    while True:
        yield pk
        pk += 1


def title():
    with open("books.txt", "rt", encoding="utf-8") as f:
        return random.choice(f.readlines())


def year():
    return randint(2000, 2050)


def pages():
    return randint(1, 1000)


def generator_fake():
    fake = Faker()
    return fake.isbn13()

