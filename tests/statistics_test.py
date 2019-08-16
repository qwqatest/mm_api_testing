import pytest
import api
import json


@pytest.fixture(scope="module")
def login_fixture():
    resp, user_id, token_value = api.login()
    # assert resp.status_code == 200
    # assert user_id[0] == 1398
    # print(token_value[0])
    # print(user_id[0])
    # print(response.json())
    # print(resp.status_code)


def test_get_statistics_all_stats(login_fixture):
    response, total_days = api.statistics_all_stats()
    assert response.status_code == 200
    assert total_days[0] == 151
    # print(json.dumps(response.json(), indent=4))
    print(total_days[0])


def test_get_statistics_charts(login_fixture):
    response, total_headaches = api.statistics_charts()
    assert response.status_code == 200
    assert total_headaches[0] == 8
    print(total_headaches[0])


def test_get_statistics_for_doctor(login_fixture):
    response = api.statistics_for_doctor()
    assert response.status_code == 200


def test_get_statistics_weather_charts(login_fixture):
    response = api.statistics_weather_charts()
    assert response.status_code == 200


def test_get_statistics_day(login_fixture):
    response, patient_id = api.statistics_day()
    assert response.status_code == 200
    assert patient_id[0] == 1398
    print(patient_id[0])
    # print(json.dumps(response.json(), indent=4))