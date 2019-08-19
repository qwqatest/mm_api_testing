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
    response = api.photo_upload()
    # assert response.status_code == 200
    print(response.url)
    print(response.json())
