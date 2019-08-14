import json
import requests
import jsonpath
import datetime
from datetime import timedelta
from urls import *
from keys import *


def login():
    global token_value
    global user_id
    resp = requests.post(BASE_URL + api_version_slug + login_slug, MMDev_user_credentials)
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')
    user_id = jsonpath.jsonpath(resp.json(), 'profile.user_id')
    return resp, user_id, token_value


# ---------------------------------------------UserProfile------------------------------------------------------
def user_profiles_with_id():
    global next_appointment
    # auth = {'Authorization': 'Bearer ' + token_value[0]}
    params = {"expand": "Qw1", "access-token": token_value[0]}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), params=params)
    next_appointment = jsonpath.jsonpath(resp.json(), 'next_appointment')
    return resp, next_appointment


def put_user_profiles():

    # data = json.loads(y)
    datetime_str = next_appointment[0]
    datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    new_appointment_datetime = datetime_object + datetime.timedelta(days=1)
    new_appointment = datetime.datetime.strftime(new_appointment_datetime, '%y-%m-%d')
    params = {"access-token": token_value[0]}
    data = {
        "achievements_score": 0,
        "avatar_base_url": "",
        "avatar_path": "",
        "condition_id": 1,
        "date_of_birth": new_appointment,
        "default": "",
        "device_token": "",
        "device_type": "apns",
        "doctor_id": 1735,
        "firstname": "Qw1",
        "gender": 1,
        "lastname": "Qw1Dev",
        "locale": "en-US",
        "middlename": "",
        "next_appointment": "",
        "notification_time": "",
        "picture": "",
        "user_id": 1398,
        "latitude": 49.996924489242,
        "longitude": 36.22787423917
    }
    resp = requests.put(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), data, params=params)
    return resp


def user_profiles_trackers():
    # auth = {'Authorization': 'Bearer ' + token_value[0]}
    params = {"days": "100", "day": "2018-12-31", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_trackers_slug, params=params)
    return resp
