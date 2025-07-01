import requests


class APIHelper:
    BASE_URL = "https://reqres.in/api"

    @staticmethod
    def get(endpoint, params=None, headers=None):
        url = f"{APIHelper.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    @staticmethod
    def post(endpoint, data=None, json=None, headers=None):
        url = f"{APIHelper.BASE_URL}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    @staticmethod
    def put(endpoint, data=None, json=None, headers=None):
        url = f"{APIHelper.BASE_URL}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers)
        return response

    @staticmethod
    def delete(endpoint, headers=None):
        url = f"{APIHelper.BASE_URL}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
