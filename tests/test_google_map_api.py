from ..utils.api import GoogleMapAPI


class TestCreatePlace:

    def test_create_place(self):
        print('\nМетод POST')
        result_post = GoogleMapAPI.create_new_place()
        place_id = result_post.json()['place_id']
        print(result_post.text)

        print('\nМетод GET')
        result_get = GoogleMapAPI.get_place(place_id)
        print(result_get.text)

        print('\nМетод PUT')
        result_put = GoogleMapAPI.put_place(place_id)
        print(result_put.text)

        print('\nМетод GET (PUT)')
        result_get = GoogleMapAPI.get_place(place_id)
        print(result_get.text)
