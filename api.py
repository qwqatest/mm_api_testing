import json
import requests
import jsonpath
import datetime

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
    # Changing appointment string to datetime format
    datetime_str = next_appointment[0]
    datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    # Adding 1 day to initial date
    new_appointment_datetime = datetime_object + datetime.timedelta(days=1)
    # Changing datetime format back to string
    new_appointment = datetime.datetime.strftime(new_appointment_datetime, '%Y-%m-%d')
    # Inserting new appointment date to dictionary in the keys.py file
    data.update({"next_appointment": new_appointment})

    params = {"access-token": token_value[0]}
    resp = requests.put(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), data, params=params)
    return resp


def user_profiles_trackers():
    params = {"days": "100", "day": "2018-12-31", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_trackers_slug, params=params)
    return resp


def user_profiles_avatars():
    params = {"access-token": token_value[0]}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_avatars_slug, params=params)
    json_response = json.loads(resp.text)
    woman_avatars = jsonpath.jsonpath(json_response, 'paths.woman')
    # Getting the first url from women's avatar list
    woman1_avatar = woman_avatars[0][0]
    return resp, woman1_avatar


def user_profiles_replies():
    params = {"access-token": token_value[0]}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_replies_slug, params=params)
    return resp


def user_profiles_reset_replies():
    params = {"access-token": token_value[0]}
    resp = requests.get(BASE_URL + api_version_slug + user_profiles_reset_replies_slug, params=params)
    return resp
