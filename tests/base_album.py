import json
import requests
from tests.config import HEADERS


class UpdateAlbum:

    """Класс для обновления альбома"""

    def create_new_album_for_update(self, album_list_url, data_for_send):
        """

        :param album_list_url:
        :param data_for_send:
        :return:
        """
        # FIXME make it compute once for class
        response = requests.post(url=album_list_url, data=data_for_send, headers=HEADERS)
        return response.json()

    def make_request(self, album_list_url, data_for_send, attribute, test_value):
        """

        :param attribute:
        :param test_value:
        :param album_list_url:
        :return:
        """
        album = self.create_new_album_for_update(album_list_url, data_for_send)
        created_album_id = album['id']
        album[attribute] = test_value
        data = json.dumps(album)
        response = requests.put(url=(album_list_url + '/' + str(created_album_id)), data=data, headers=HEADERS)
        return response
