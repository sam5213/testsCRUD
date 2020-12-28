from random import randint
from tests import base_album, fake
from tests.config import MIN_ID_USER, MAX_ID_USER, MIN_ID_ALBUM, MAX_ID_ALBUM


class TestUpdateAlbum(base_album.UpdateAlbum):

    """Класс для обновления альбома"""

    def test_update_user_id(self, album_list_url, data_for_send):
        """
        Проверяем, что userId успешно обновился
        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'userId', randint(MIN_ID_USER, MAX_ID_USER))
        assert response.status_code == 200

    # 200 - принимает отрицательное значение
    def test_update_on_negative_user_id(self, album_list_url, data_for_send):
        """
        Проверяем, что отрицательное значение userId не принимается
        :param album_list_url:
        :param data_for_send:
        :return:
        """
        response = self.make_request(
            album_list_url, data_for_send, 'userId', MIN_ID_USER - randint(MAX_ID_USER, MAX_ID_USER) - 1)
        assert response.status_code == 400

    # установилось отрицательное значение, хотя не должно было
    def test_update_on_value_negative_user_id(self, album_list_url, data_for_send):
        """
        Срвниваем с действительным значением в базе
        :param album_list_url:
        :param data_for_send:
        :return:
        """
        test_value = MIN_ID_USER - randint(MAX_ID_USER, MAX_ID_USER) - 1
        response = self.make_request(album_list_url, data_for_send, 'userId', test_value)
        assert response.json()['userId'] != test_value

    # 200 - принимает пустую строку
    def test_update_on_empty_user_id(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что пустое значение userId не принимается
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'userId', '')
        assert response.status_code == 400

    def test_update_on_value_empty_user_id(self, album_list_url, data_for_send, album_dict):
        """
        Срвниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'userId', '')
        assert response.json()['userId'] != ''

    # запрс возвращает ответ OK, но само значение не менятеся
    def test_update_id(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что id успешно обновился
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'id', randint(MIN_ID_ALBUM, MAX_ID_ALBUM))
        assert response.status_code == 200

    def test_update_value_id(self, album_list_url, data_for_send, album_dict):
        """
        Срвниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        test_value = randint(MIN_ID_ALBUM, MAX_ID_ALBUM)
        response = self.make_request(album_list_url, data_for_send, 'id', test_value)
        assert response.json()['id'] == test_value

    # запрс возвращает ответ OK, но само значение не менятеся
    def test_update_on_negative_id(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что отрицательное значение id не принимается
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'id', MIN_ID_ALBUM - MAX_ID_ALBUM)
        assert response.status_code == 400

    def test_update_on_value_negative_id(self, album_list_url, data_for_send, album_dict):
        """
        Сравниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        test_value = MIN_ID_ALBUM - MAX_ID_ALBUM
        response = self.make_request(album_list_url, data_for_send, 'id', test_value)
        assert response.json()['id'] != test_value

    # запрс возвращает ответ OK, но само значение не менятеся
    def test_update_on_empty_id(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что пустое значение id не принимается
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'id', '')
        assert response.status_code == 400

    def test_update_on_value_empty_id(self, album_list_url, data_for_send, album_dict):
        """
        Сравниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'id', '')
        assert response.json()['id'] != ''

    def test_update_title(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что title успешно обновился
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'title', fake.sentence())
        assert response.status_code == 200

    def test_update_value_title(self, album_list_url, data_for_send, album_dict):
        """
        Сравниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        test_value = fake.sentence()
        response = self.make_request(album_list_url, data_for_send, 'title', test_value)
        assert response.json()['title'] == test_value

    # 200 - принимает пустую строку
    def test_update_on_empty_title(self, album_list_url, data_for_send, album_dict):
        """
        Проверяем, что пустое значение title не принимается
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'title', '')
        assert response.status_code == 400

    def test_update_on_value_empty_title(self, album_list_url, data_for_send, album_dict):
        """
        Сравниваем с действительным значением в базе
        :param album_list_url:
        :param album_dict:
        :return:
        """
        response = self.make_request(album_list_url, data_for_send, 'title', '')
        assert response.json()['title'] != ''

