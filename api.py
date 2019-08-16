import json
import requests
import jsonpath
import datetime

from urls import *
from keys import *


# ---------------------------------------------Register---------------------------------------------------------

def photo_upload():
    file = open('/Users/srsh/Desktop/Plato.jpg', 'r')
    # json_input = file.read()
    resp = requests.post(BASE_URL + api_version_slug + photo_upload_slug)




def login():
    global token_value
    global user_id
    resp = requests.post(BASE_URL + api_version_slug + login_slug, MMDev_user_credentials)
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')
    user_id = jsonpath.jsonpath(resp.json(), 'profile.user_id')
    return resp, user_id, token_value

# ---------------------------------------------Statistics-------------------------------------------------------


def statistics_all_stats():
    params = {"to": "2019-05-30", "from": "2018-12-31", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + statistics_all_stats_slug, params=params)
    # Getting number of total days from response
    json_response = json.loads(resp.text)
    total_days = jsonpath.jsonpath(json_response, 'summary.total_count_days')
    return resp, total_days


def statistics_charts():
    params = {"from": "2018-12-31", "to": "2019-05-30", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + statistics_charts_slug, params=params)
    # Getting number of total headaches from response
    json_response = json.loads(resp.text)
    total_headaches = jsonpath.jsonpath(json_response, 'summary.total_headaches_count')
    return resp, total_headaches


def statistics_for_doctor():
    params = {"user_id": user_id[0], "from": "2018-12-31", "day": "2019-01-31", "days": "30", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + statistics_for_doctor_slug, params=params)
    return resp


def statistics_weather_charts():
    params = {"from": "2018-12-31", "to": "2019-05-30", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + statistics_weather_charts_slug, params=params)
    return resp


def statistics_day():
    params = {"date": "2018-12-31", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + statistics_day_slug, params=params)
    # Getting patient_id from response
    json_response = json.loads(resp.text)
    patient_id = jsonpath.jsonpath(json_response, 'headaches[0].patient_id')
    return resp, patient_id

# ---------------------------------------------UserProfile------------------------------------------------------


def user_profiles_with_id():
    global next_appointment
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
