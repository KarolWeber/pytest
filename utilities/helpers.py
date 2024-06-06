from enum import Enum
import requests


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def api_call(method: HttpMethod, url, user=None, data=None):
    headers = {"Content-Type": "application/json"}
    if user:
        headers["Cookie"] = f'token={user}'
    if method not in HttpMethod:
        raise ValueError("Invalid HTTP method")
    if method == HttpMethod.GET:
        response = requests.get(url=url, headers=headers)
    elif method == HttpMethod.POST:
        response = requests.post(url=url, headers=headers, json=data)
    elif method == HttpMethod.PUT:
        response = requests.put(url=url, headers=headers, json=data)
    elif method == HttpMethod.PATCH:
        response = requests.patch(url=url, headers=headers, json=data)
    elif method == HttpMethod.DELETE:
        response = requests.delete(url=url, headers=headers, json=data)
    else:
        response = "Invalid HTTP method"
    return response

