import pytest

from others.http_response_01 import handle_response
from tests.fake_response import FakeResponse


class TestHttpResponse:
    status_codes = [200, 201, 202, 204, 301, 302, 400, 401, 403, 404, 405, 418, 500, 501, 503]

    @pytest.mark.parametrize("status_code", status_codes)
    def test_http_response_01(self, status_code):
        response = FakeResponse(status_code=status_code)

        result = handle_response(response)

        date = response.headers.get("Date")
        content_length = response.headers.get("content-length")
        if status_code in [400, 404]:
            expected_result = {}
        elif status_code < 300:
            expected_result = {
                "date": {date},
                "status_code": {status_code},
                "content_length": {content_length},
                "person": response.json(),
            }
        elif status_code == 418:
            expected_result = {
                "date": {date},
                "status_code": {status_code},
                "content_length": {content_length},
                "person": "I'm a teapot",
            }

        else:
            expected_result = {
                "date": {date},
                "status_code": {status_code},
                "content_length": {content_length},
            }

        assert result == expected_result
