import json
import pytest
from random import randint
from tests import AlbumFactory

from tests.config import *


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def album_list_url(base_url):
    return base_url + ALBUMS


@pytest.fixture
def user_list_url(base_url):
    return base_url + USERS


@pytest.fixture
def album_dict():
    return AlbumFactory().__dict__


@pytest.fixture
def data_for_send(album_dict):
    album_dict['id'] = randint(MIN_ID_ALBUM, MAX_ID_ALBUM)
    return json.dumps(album_dict)


@pytest.fixture
def data_for_update(album_dict):
    album_dict['id'] = randint(MIN_ID_ALBUM, MAX_ID_ALBUM)
    return json.dumps(album_dict)
