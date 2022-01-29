"""
status_codes = [200, 201, 202, 204, 301, 302, 400, 401, 403, 404, 405, 500, 501, 503]

200 - 299 -> return dict with keys: {date, status_code, content_length, person with value from response.json()}
300 - 499 (excluding 401, 403, 418)-> return empty dict
100-199, 401, 403 and 500 - 599 -> return dict with keys: {date, status_code, content_length }
418 -> return dict with keys: {date, status_code, content_length + person with value `I'm a teapot` }
"""
from typing import Dict

from tests.fake_response import FakeResponse


def handle_response(response: FakeResponse) -> Dict:
    # put your code here:

    # don't remove line bellow
    return {}


if __name__ == "__main__":
    res = FakeResponse(200)
    print(res)
    print(vars(res))
    print(handle_response(res))
