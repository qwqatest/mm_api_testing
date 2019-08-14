import json
import requests
import jsonpath
from urls import *
from keys import *


auth = {'Authorization': 'Bearer ' + str()}


def login():
    global token_value
    global user_id
    resp = requests.post(BASE_URL + api_version_slug + login_slug, MMDev_user_credentials)
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')
    user_id = jsonpath.jsonpath(resp.json(), 'profile.user_id')
    return resp, user_id, token_value

#---------------------------------------------UserProfile------------------------------------------------------


def user_profiles_with_id():
    # auth = {'Authorization': 'Bearer ' + token_value[0]}
    params = {"expand": "Qw1", "access-token": token_value[0]}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), params=params)
    last_visit_time = jsonpath.jsonpath(resp.json(), 'last_visit')
    print(last_visit_time)
    return resp, last_visit_time



def user_profiles_trackers():
    # auth = {'Authorization': 'Bearer ' + token_value[0]}
    params = {"days": "100", "day": "2018-12-31", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_trackers_slug, params=params)
    return resp
