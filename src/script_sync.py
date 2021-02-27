import requests
from functools import reduce


API1 = 'endpoint_1'
API2 = 'endpoint_2'
API3 = 'endpoint_3'
DATA_SOURCES = [API1, API2, API3]


class DataHelper:

    BASE_URL = 'http://localhost:8000/'

    def __init__(self, data_sources):
        self._data_sources = data_sources

    def get_member_data(self, member_id: int):
        responses = []
        for endpoint in self._data_sources:
            response = requests.get(f'{self.BASE_URL}{endpoint}?member_id={member_id}')
            responses.append(response.json())

        return responses


def data_consolidator(responses: list):
    all_keys = reduce((lambda x, y: x | y), [d.keys() for d in responses])
    max_dict = {k: max(d.get(k, 0) for d in responses) for k in all_keys}
    return max_dict


def main(member_id):
    data_helper = DataHelper(DATA_SOURCES)
    responses = data_helper.get_member_data(member_id)
    result = data_consolidator(responses)
    print(result)
    return result


main(1234)
