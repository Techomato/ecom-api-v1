import json
from typing import Union, Optional
import requests
from requests import Response

from ecom_exceptions.ecom_exceptions import ECOMRequestsError


class ECOMRequests:
    def __init__(
        self,
        host: str,
        headers: Optional[dict] = None,
        content_type: str = "application/json",
        with_ssl: bool = True,
    ):
        if with_ssl:
            self.host = f"https://{host}/"
        else:
            self.host = f"http://{host}/"
        self.headers = headers if headers else {}
        self.content_type = content_type
        self.payload = None
        self.path = None

    def post(
        self,
        path: str,
        payload: Union[dict, str],
        headers: Optional[dict] = None,
        content_type: str = "application/json",
    ) -> Response:
        if payload:
            if isinstance(payload, dict):
                self.payload = json.dumps(payload)
        if not path:
            raise ECOMRequestsError(msg="Path is required")
        if content_type:
            self.content_type = content_type
        if headers:
            self.headers = headers
        self.path = path
        self.headers.update({"Content-Type": self.content_type})
        response = requests.post(
            url=f"{self.host}{self.path}",
            data=self.payload,
            headers=self.headers,
        )
        return response

    def get(
        self,
        path: str,
        payload: Optional[Union[dict, str]] = None,
        headers: Optional[dict] = None,
        content_type: str = "application/json",
    ) -> Response:
        if payload:
            if isinstance(payload, dict):
                self.payload = json.dumps(payload)
        if not path:
            raise ECOMRequestsError(msg="Path is required")
        if content_type:
            self.content_type = content_type
        if headers:
            self.headers = headers
        self.path = path
        self.headers.update({"Content-Type": self.content_type})
        response = requests.get(
            url=f"{self.host}{self.path}",
            data=self.payload,
            headers=self.headers,
        )
        return response
