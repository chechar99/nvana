from unittest.mock import call

from src.script_sync import data_consolidator, DataHelper


def test_data_helper(mocker):
    endpoints = ['endpoint1', 'endpoint2']
    requests_mock = mocker.patch('src.script_sync.requests')
    requests_mock.get.return_value.json.return_value = {'expected': 'response'}

    helper = DataHelper(endpoints)
    responses = helper.get_member_data(9999)

    assert 2 == len(responses)
    assert {'expected': 'response'} == responses[0]
    assert {'expected': 'response'} == responses[1]

    assert 2 == requests_mock.get.call_count
    requests_mock.get.assert_has_calls([
        call('http://localhost:8000/endpoint1?member_id=9999'),
        call().json(),
        call('http://localhost:8000/endpoint2?member_id=9999'),
        call().json(),
    ])


def test_data_consolidator():

    data_to_consolidate = [
        {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000},
        {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000},
        {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 6000},
    ]
    data = data_consolidator(data_to_consolidate)

    expected_result = {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000}
    assert expected_result == data
