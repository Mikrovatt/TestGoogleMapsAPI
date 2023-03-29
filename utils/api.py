from requests import Response
from .http_methods import HttpMethods


class GoogleMapAPI:
    """ Класс для создания, изменения и удаления локации """

    base_url = 'https://rahulshettyacademy.com'  # базовый URL для запроса
    key = '?key=qaclick123'  # общий параметр для запроса

    @staticmethod
    def create_new_place() -> Response:
        """ Метод для создания локации """

        # json запрос для создания локации
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'
        post_url = f'{GoogleMapAPI.base_url}{post_resource}{GoogleMapAPI.key}'
        print(f'POST URL = {post_url}')
        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_place(place_id: str) -> Response:
        """ Метод для получения данных локации """

        get_resource = '/maps/api/place/get/json'
        get_url = f'{GoogleMapAPI.base_url}{get_resource}{GoogleMapAPI.key}&place_id={place_id}'
        print(f'GET URL = {get_url}')
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_place(place_id: str) -> Response:
        """ Метод изменения данных локации """

        # json запрос для изменения данных локации
        json_for_change_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_resource = '/maps/api/place/update/json'
        put_url = f'{GoogleMapAPI.base_url}{put_resource}{GoogleMapAPI.key}'
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_change_place)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_place(place_id: str) -> Response:
        """ Метод удаления локации """

        # json запрос для удаления локации
        json_for_delete_place = {
            "place_id": place_id
        }

        delete_resource = '/maps/api/place/delete/json'
        delete_url = f'{GoogleMapAPI.base_url}{delete_resource}{GoogleMapAPI.key}'
        result_delete = HttpMethods.delete(delete_url, json_for_delete_place)
        print(result_delete.text)
        return result_delete
