from requests import Response


class Checking:
    """ Класс методов для проверки API """
    @staticmethod
    def check_status_code(result: Response, status_code: int) -> None:
        """ Метод проверки статус кода операции """

        assert status_code == result.status_code
        print(f'Успешно! Статус-код {status_code} соответствует')

    @staticmethod
    def check_json_key(result: Response, expected_key: list) -> None:
        """ Метод проверки обязательных полей запроса """

        key = result.json()
        assert list(key) == expected_key
        print('Все необходимые поля присутствуют')

    @staticmethod
    def check_json_value(result: Response, field_name: str, expected_value: str) -> None:
        """ Метод проверки значений полей запроса """
        value = result.json()
        check_value = value[field_name]
        assert expected_value == check_value
        print(f'Значение поля {field_name}: {check_value}. Верно!')
