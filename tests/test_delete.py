import requests
from tests.config import MIN_ID_ALBUM, MAX_ID_ALBUM, HEADERS


class TestDeleteAlbum:

    """Класс для удаления альбома"""

    def test_delete_album(self, album_list_url, data_for_send, album_dict):
        """
        Проверям, что успешно удалили альбом
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = requests.post(album_list_url, data=data_for_send, headers=HEADERS)
        response = requests.delete(url=album_list_url + '/' + str(response.json()['id']))
        assert response.status_code == 200

    def test_delete_album_with_wrong_id(self, album_list_url, album_dict):
        """
        Проверяем, что несуществующий альбом невозможно удалить
        :param album_list_url:
        :param album_dict:
        :return:
        """
        album_dict['id'] = MIN_ID_ALBUM - MAX_ID_ALBUM
        response = requests.delete(url=album_list_url + '/' + str(album_dict['id']))
        assert response.status_code == 404
