import requests
from requests import Response

from ..utils.logger import Logger


class HttpMethods:
    """ Класс http методов для доcтупа к API """

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url: str) -> Response:
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url: str, body: dict) -> Response:
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url: str, body: dict) -> Response:
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url: str, body: dict) -> Response:
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
