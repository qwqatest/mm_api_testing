import pytest
from api import Api


def test_login():
    resp, user_id, token_value = Api.login()
    assert resp.status_code == 200
    assert user_id[0] == 1378
    print(token_value[0])
    print(user_id[0])
    # print(response.json())
    print(resp.status_code)
