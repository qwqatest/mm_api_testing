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


def test_photo_upload(login_fixture):
    response, delete_url = api.photo_upload()
    assert response.status_code == 200
    print(response.text)
    print(delete_url[0])


def test_delete_photo(login_fixture):
    response = api.delete_photo()
    print(response.url)
    print(response.status_code)
    print(response.text)

def test_check_email(login_fixture):
    response, users_found = api.register_check_email()
    assert response.status_code == 200
    assert users_found[0] == 1
    print(response.text)


def test_navigator_token(login_fixture):
    response = api.register_navigator_token()
    assert response.status_code == 200
    assert response.text == '"123"'

