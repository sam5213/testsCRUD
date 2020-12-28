import json
import requests
from tests.config import *


class TestCreateAlbum:

    """Класс для создания альбома"""

    def test_create_album(self, album_list_url, data_for_send):
        """
        Проверяем, что альбом успешно создался

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        assert response.status_code == 201

    def test_create_album_in_list(self, album_list_url, data_for_send):
        """
        Проверяем, что созданный альбом есть в списке альбомов

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        album = response.json()
        response = requests.get(url=album_list_url)
        assert album in response.json()

    def test_create_album_attributes(self, album_list_url, data_for_send):
        """
        Проверяем, что созданный альбом имеет все аттрибуты

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        album_expected_keys = json.loads(data_for_send).keys()
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        album = response.json()
        assert album_expected_keys == album.keys()

    def test_create_album_and_check_id(self, album_list_url, data_for_send):
        """
        Проверяем, что созданный альбом с тем, самым id, что и создавался

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        expected_id = int(json.loads(data_for_send)['id'])
        assert int(response.json()['id']) == expected_id

    def test_create_album_and_check_user_id(self, album_list_url, data_for_send):
        """
        Проверяем, что созданный альбом с тем, самым userId, что и создавался

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        expected_user_id = int(json.loads(data_for_send)['userId'])
        assert int(response.json()['userId']) == expected_user_id

    def test_create_album_and_check_title(self, album_list_url, data_for_send):
        """
        Проверяем, что созданный альбом с тем, самым title, что и создавался

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        expected_album = response.json()
        url_for_send = album_list_url + '/' + str(expected_album['id'])
        response = requests.get(url=url_for_send)
        received_album = response.json()
        assert expected_album['title'] == received_album['title']
