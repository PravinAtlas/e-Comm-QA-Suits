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

    # Example convenience methods for reqres.in
    @staticmethod
    def get_users(page):
        return APIHelper.get("/users", params={"page": page})

    @staticmethod
    def get_user(user_id):
        return APIHelper.get(f"/users/{user_id}")

    @staticmethod
    def create_user(name, job):
        return APIHelper.post("/users", json={"name": name, "job": job})

    @staticmethod
    def update_user(user_id, name=None, job=None):
        payload = {}
        if name:
            payload["name"] = name
        if job:
            payload["job"] = job
        return APIHelper.put(f"/users/{user_id}", json=payload)

    @staticmethod
    def delete_user(user_id):
        return APIHelper.delete(f"/users/{user_id}")
