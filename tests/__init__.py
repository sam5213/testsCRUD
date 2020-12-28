from faker import Faker
from random import randint
from tests.config import *


fake = Faker()


class AlbumFactory():
    def __init__(self):
        self.userId = randint(MIN_ID_USER, MAX_ID_USER)
        self.id = randint(MIN_ID_ALBUM, MAX_ID_ALBUM)
        self.title = fake.sentence()
