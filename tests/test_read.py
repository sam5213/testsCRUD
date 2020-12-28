import pytest
import requests
from tests.config import *


class TestReadAlbum:

    """Класс для получения альбома"""

    def test_get_albums_check_status_code_equals_200(self, album_list_url):
        """
        Проверяем, что можем просмотреть альбомы
        :param album_list_url:
        :return:
        """
        response = requests.get(url=album_list_url)
        assert response.status_code == 200

    def test_get_album_list(self, album_list_url):
        """
        Проверяем, что есть список альбомов
        :param album_list_url:
        :return:
        """
        response = requests.get(url=album_list_url)
        assert type(response.json()) == list

    def test_get_album_check_content_type_equals_json_and_utf_8(self, album_list_url):
        """
        Проверяем, что content-type верный
        :param album_list_url:
        :return:
        """
        response = requests.get(album_list_url)
        assert response.headers['Content-type'].lower() == HEADERS['Content-type'].lower()

    def test_get_album_by_id(self, album_list_url, album_dict, data_for_send):
        """
        Проверяем, что можно получить альбом по его id
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = requests.post(album_list_url, data=data_for_send, headers=HEADERS)
        response = requests.get(url=album_list_url + '/' + str(response.json()['id']))
        assert response.status_code == 200

    @pytest.mark.parametrize('id', [MIN_ID_ALBUM - 1, 0, MAX_ID_ALBUM + 1, 'a'])
    def test_get_album_by_not_valid_id(self, album_list_url, id):
        """
        Проверяем, что при отправке невалидного id ресурс будет не найден
        :param album_list_url:
        :param id:
        :return:
        """
        url_to_send = album_list_url + '/' + str(id)
        response = requests.get(url=url_to_send)
        assert response.status_code == 404

    @pytest.mark.parametrize('id', [MIN_ID_USER - 1, 0, MAX_ID_USER + 1, 'a'])
    def test_get_album_by_not_valid_user_id(self, user_list_url, id):
        """
        Проверяем, что при отправке невалидного userId ресурс будет не найден
        :param user_list_url:
        :param id:
        :return:
        """
        url_to_send = user_list_url + '/' + str(id)
        response = requests.get(url=url_to_send)
        assert response.status_code == 404


