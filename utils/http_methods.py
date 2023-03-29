import requests
from requests import Response


class HttpMethods:
    """ Класс http методов для доcтупа к API """

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url: str) -> Response:
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url: str, body: dict) -> Response:
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url: str, body: dict) -> Response:
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url: str, body: dict) -> Response:
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
