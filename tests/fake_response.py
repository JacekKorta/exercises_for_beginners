import random
from typing import Dict, Optional

from tests.fake_persons import Person


class FakeResponse:
    codes = [200, 201, 202, 204, 301, 302, 400, 401, 403, 404, 405, 500, 501, 503]

    def __init__(self, status_code: Optional[int] = None):
        self.status_code = status_code if status_code else random.choice(self.codes)
        self.headers = self.get_headers()

    def get_headers(self):
        return {
            "Date": "Sun, 23 Jan 2022 14:28:05 GMT",
            "Content-Type": "application/json; charset=utf-8",
            "Transfer-Encoding": "chunked",
            "Connection": "keep-alive",
            "x-powered-by": "Express",
            "x-ratelimit-limit": "1000",
            "x-ratelimit-remaining": "999",
            "x-ratelimit-reset": "1639648932",
            "vary": "Origin, Accept-Encoding",
            "access-control-allow-credentials": "true",
            "cache-control": "max-age=43200",
            "pragma": "no-cache",
            "expires": "-1",
            "x-content-type-options": "nosniff",
            "content-length": "19373",
        }

    def json(self) -> Dict:
        if self.status_code not in [200, 201]:
            return {}
        else:
            person = Person()
            return {
                "id": random.randint(0, 9),
                "name": f"{person.first_name} {person.last_name}",
                "address": f"{person.full_address}",
            }

    def __repr__(self):
        return f"<Response [{self.status_code}]>"


if __name__ == "__main__":
    res = FakeResponse()
    print(f"{res.status_code=}")
    print(f"{res.headers=}")
    print(f"{res.json()}")
