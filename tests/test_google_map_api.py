from ..utils.api import GoogleMapAPI
from ..utils.cheking import Checking


class TestCreatePlace:
    """ Класс для тестирования создания, изменения и удаления локации """
    @staticmethod
    def test_create_place() -> None:
        print('\nМетод POST: проверка создания новой локации')
        result_post = GoogleMapAPI.create_new_place()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_key(result_post, ["status", "place_id", "scope", "reference", "id"])
        Checking.check_json_value(result_post, 'status', 'OK')
        place_id = result_post.json()['place_id']  # получение place_id созданной локации

        print('\nМетод GET: проверка получения данных созданной локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get,
                                ["location", "accuracy", "name", "phone_number",
                                 "address", "types", "website", "language"])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('\nМетод PUT: проверка изменения данных созданной локации')
        result_put = GoogleMapAPI.put_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_key(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", 'Address successfully updated')

        print('\nМетод GET: проверка получения данных измененной локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get,
                                ["location", "accuracy", "name", "phone_number",
                                 "address", "types", "website", "language"])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('\nМетод DELETE: проверка удаления созданной локации')
        result_delete = GoogleMapAPI.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_key(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('\nМетод GET: проверка получения данных удаленной(несуществующей) локации')
        result_get = GoogleMapAPI.get_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_key(result_get, ["msg"])
        Checking.check_json_value(result_get, 'msg',
                                  "Get operation failed, looks like place_id  doesn't exists")

        print('\nМетод PUT: проверка изменения данных несуществующей локации')
        result_put = GoogleMapAPI.put_place(place_id)
        Checking.check_status_code(result_put, 404)
        Checking.check_json_key(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg",
                                  "Update address operation failed, looks like the data doesn't exists")

        print('\nМетод DELETE: проверка удаления несуществующей локации')
        result_delete = GoogleMapAPI.delete_place(place_id)
        Checking.check_status_code(result_delete, 404)
        Checking.check_json_key(result_delete, ['msg'])
        Checking.check_json_value(result_delete, 'msg',
                                  "Delete operation failed, looks like the data doesn't exists")

        print('Тестирование создания, изменения и удаления локации пройдено успешно!')
