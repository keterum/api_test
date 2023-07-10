from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time():
    x = 5
    time = http_bin_api.time_out(x)
    assert time.status_code == HTTPStatus.OK
