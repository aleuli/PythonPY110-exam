import json
import re
from faker import Faker


books_file = "fake_generator_isbn13"
books_isbn_13 = r"(?P<prefix>97[8,9])?\-(?P<group_registration>[0,1])?\-" \
                r"(?P<registrant>\d{1,7})\-(?P<public>\d{1,6})\-(?P<number_control>[0-9,X])"


def generator_fake():
    fake = Faker()
    with open("fake_generator_isbn13", "w") as f:
        f.writelines([fake.isbn13() + "\n" for _ in range(1000000)])


def task():
    book_pattern = re.compile(books_isbn_13, re.DOTALL)
    with open(books_file) as f:
        for book in book_pattern.finditer(f.read()):
            print(any(json.dumps(book.groupdict(), indent=4)))


if __name__ == '__main__':
    generator_fake()
    task()
