import requests

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest

from requests.structures import CaseInsensitiveDict
from retrying import retry

from .types import ProxyResponse
from .utils import retry_if_connection_error, update_html


@retry(retry_on_exception=retry_if_connection_error, wait_fixed=2000)
def get_proxy_response(request: WSGIRequest) -> ProxyResponse:
    headers = {
        "user-agent": request.META['HTTP_USER_AGENT'],
    }
    cookies = {
        'R3ACTLB': 'f8cb235b9e4dbb76f6522827fd366ec1'
    }

    try:
        response = requests.get(settings.PROXY_URL + request.path, headers=headers, timeout=5, cookies=cookies)

        if response.status_code > 499:
            raise ConnectionError()
    except (
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError
    ):
        return ProxyResponse(
            content=b'Error',
            status_code=500,
            headers=CaseInsensitiveDict({'content-type': 'text/html'})
        )

    content = response.content

    if 'text/html' in response.headers.get('Content-type'):
        content = update_html(content)

    return ProxyResponse(
        content=content,
        status_code=response.status_code,
        headers=response.headers,
        errors=False
    )
