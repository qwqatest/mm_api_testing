import json
import requests
import jsonpath
from urls import *
from keys import *


class Api:

    @staticmethod
    def login():
        resp = requests.post(BASE_URL + api_version_slug + login_slug, MMDev_user_credentials)
        token_value = jsonpath.jsonpath(resp.json(), 'access_token')
        user_id = jsonpath.jsonpath(resp.json(), 'profile.user_id')
        return resp, user_id, token_value

        # # Get /user-profiles
        # auth = {'Authorization': 'Bearer ' + token_value[0]}
        # params = {"expand": "user", "access-token": token_value[0]}
        # user_profiles_slug = '/user-profiles/'+str(user_id[0])
        # resp = requests.get(BASE_URL + api_version_slug + user_profiles_slug, headers=auth, params=params)
        # assert resp.status_code == 200
        # print(json.dumps(resp.json(), indent=4))
        #
        # # Get /user-profiles/trackers
        # auth = {'Authorization': 'Bearer ' + token_value[0]}
        # params = {"days": "100", "day": "2018-12-31", "access-token": token_value}
        # api_url = 'http://hm.ulik.info/api/v1/user-profiles/trackers'
        # resp = requests.get(api_url, headers=auth, params=params)
        # assert resp.status_code == 200
        # print(json.dumps(resp.json(), indent=4))
