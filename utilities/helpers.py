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
    if method not in HttpMethod:
        raise ValueError("Invalid HTTP method")
    try:
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
            raise ValueError("Invalid HTTP method")
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

