import json
import requests
import jsonpath
import datetime

from urls import *
from keys import *


# ---------------------------------------------Register---------------------------------------------------------

def photo_upload():
    global base_url
    global path
    global delete_url

    with open('Plato.jpg', 'rb') as f:
        params = {"access-token": token_value}
        resp = requests.post(BASE_URL + api_version_slug + photo_upload_slug, files={'avatar': ("Plato.jpg", f, "image/jpg")}, params=params,)
    # f = open('/Users/srsh/Desktop/Plato.jpg', 'rb')
    # params = {"access-token": token_value}
    # files = {'avatar': ("Plato.jpg", f, "image/jpg")}
    # resp = requests.post(BASE_URL + api_version_slug + photo_upload_slug, files=files, params=params)
    base_url = jsonpath.jsonpath(resp.json(), 'files[0].base_url')
    path = jsonpath.jsonpath(resp.json(), 'files[0].path')
    delete_url = jsonpath.jsonpath(resp.json(), 'files[0].delete_url')

    return resp, base_url, path, delete_url


def delete_photo():
    global delete_url
    params = {"access-token": token_value}
    resp = requests.delete(BASE_URL + delete_url, params=params)
    return resp


def register_check_email():
    params = {"email": "qwqatest+1@gmail.com", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + register_check_email_slug, params=params)
    # Getting number of total days from response
    json_response = json.loads(resp.text)
    users_found = jsonpath.jsonpath(json_response, 'users_found')
    return resp, users_found


def login():
    global token_value
    global user_id
    resp = requests.post(BASE_URL + api_version_slug + login_slug, MMDev_user_credentials)
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')
    user_id = jsonpath.jsonpath(resp.json(), 'profile.user_id')
    return resp, user_id, token_value


def register_navigator_token():
    params = {"email": "qwqatest+1@gmail.com", "access-token": token_value}
    resp = requests.get(BASE_URL + api_version_slug + register_navigator_token_slug, params=params)
    # Getting number of total days from response
    # json_response = json.loads(resp.text)
    # users_found = jsonpath.jsonpath(json_response, 'users_found')
    return resp


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
    global user_profile_resp
    params = {"expand": "Qw1", "access-token": token_value[0]}
    user_profile_resp = requests.get(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), params=params)
    next_appointment = jsonpath.jsonpath(user_profile_resp.json(), 'next_appointment')
    return user_profile_resp, next_appointment


def put_user_profiles():
    # user_profile_data = json.loads(user_profile_resp.text)
    # Changing appointment string to datetime format
    datetime_str = next_appointment[0]
    datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    # Adding 1 day to initial date
    new_appointment_datetime = datetime_object + datetime.timedelta(days=1)
    # Changing datetime format back to string
    new_appointment = datetime.datetime.strftime(new_appointment_datetime, '%Y-%m-%d')
    # Inserting new appointment date to the dictionary
    # print(user_profile_data)
    print(type(path[0]))
    print(type(base_url[0]))
    data = ({"avatar_base_url": base_url[0], "avatar_path": path[0], "next_appointment": new_appointment})
    # user_profile_data.update({"next_appointment": new_appointment})
    # user_profile_data.update({"avatar_base_url": base_url[0]})
    print(data)

    params = {"access-token": token_value[0]}
    resp = requests.put(BASE_URL + api_version_slug + user_profiles_slug + str(user_id[0]), data, params=params)
    print(resp.url)
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
