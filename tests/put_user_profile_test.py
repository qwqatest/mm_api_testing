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


def test_get_user_profile_with_id(login_fixture):
    response, next_appointment = api.user_profiles_with_id()
    # print("Current appointment date: " + str(next_appointment[0]))
    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))


def test_photo_upload(login_fixture):
    response, picture, delete_url = api.photo_upload()
    assert response.status_code == 200
    # print(response.text)
    # print(picture)


def test_put_user_profile(login_fixture):
    # test_get_user_profile_with_id(login_fixture)
    response = api.put_user_profiles()
    print("Response  " + json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    # test_get_user_profile_with_id(login_fixture)


def test_delete_photo(login_fixture):
    response = api.delete_photo()
    print(response.url)
    print(response.status_code)
    print(response.text)