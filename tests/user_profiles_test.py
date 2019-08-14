import pytest
import api
import json


@pytest.fixture(scope="module")
def login_fixture():
    resp, user_id, token_value = api.login()
    # assert resp.status_code == 200
    # assert user_id[0] == 1398
    print(token_value[0])
    # print(user_id[0])
    # print(response.json())
    # print(resp.status_code)


# Get /user-profiles
def test_get_user_profiles_with_id(login_fixture):
    response, last_visit_time = api.user_profiles_with_id()
    print(response.url)
    assert response.status_code == 200
    # print(json.dumps(response.json(), indent=4))


# # Get /user-profiles/trackers
def test_get_user_profiles_trackers(login_fixture):
    response = api.user_profiles_trackers()
    print(response.url)
    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))