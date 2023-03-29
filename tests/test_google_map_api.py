from ..utils.api import GoogleMapAPI
from ..utils.cheking import Checking


class TestCreatePlace:
    """ Класс для тестирования создания, изменения и удаления локации """
    @staticmethod
    def test_create_place() -> None:
        print('\nМетод POST: создание новой локации')
        result_post = GoogleMapAPI.create_new_place()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_key(result_post, ["status", "place_id", "scope", "reference", "id"])
        place_id = result_post.json()['place_id']  # получение place_id созданной локации

        print('\nМетод GET: получение данных созданной локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get,
                                ["location", "accuracy", "name", "phone_number",
                                 "address", "types", "website", "language"])

        print('\nМетод PUT: изменение созданной локации')
        result_put = GoogleMapAPI.put_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_key(result_put, ["msg"])

        print('\nМетод GET: получение данных измененной локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get,
                                ["location", "accuracy", "name", "phone_number",
                                 "address", "types", "website", "language"])

        print('\nМетод DELETE: удаление созданной локации')
        result_delete = GoogleMapAPI.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_key(result_delete, ["status"])

        print('\nМетод GET: проверка удаления локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_key(result_get, ["msg"])

        print('Тестирование создания, изменения и удаления локации пройдено успешно!')
