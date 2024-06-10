from enum import Enum
import requests


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def api_call(method: HttpMethod, url, user=None, data=None):
    """
    Make an HTTP request to the specified URL.

    :param method: The HTTP method to use (GET, POST, PUT, PATCH, DELETE).
    :param url: The URL to make the request to.
    :param user: (Optional) The user token for authentication (default is None).
    :param data: (Optional) The JSON data to send in the request body (default is None).
    :return: The response object.
    :raises ValueError: If an invalid HTTP method is provided.
    """
    headers = {"Content-Type": "application/json"}
    if user:
        headers["Cookie"] = f'token={user}'
    if method not in HttpMethod:
        raise ValueError("Invalid HTTP method")
    response = requests.request(method=method.value, url=url, headers=headers, json=data)
    return response

