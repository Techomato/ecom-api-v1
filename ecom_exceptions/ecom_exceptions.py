import logging
from typing import Optional

from rest_framework import status

from ecom_exceptions.base_exception import ECOMBaseException


class ECOMValueError(ECOMBaseException):
    def __init__(self, name: Optional[str] = None, msg: Optional[str] = None):
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        if not name:
            self.name = "ECOMValueError"
        else:
            self.name = name
        if not msg:
            self.msg = "ECOMValueError Occurred."
        else:
            self.msg = msg
        super().__init__(self.name, self.msg, self.status)
        logging.error(self.msg)


class ECOMRequestsError(ECOMBaseException):
    def __init__(self, name: Optional[str] = None, msg: Optional[str] = None):
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        if not name:
            self.name = "ECOMRequestsError"
        else:
            self.name = name
        if not msg:
            self.msg = "ECOMRequestsError Occurred."
        else:
            self.msg = msg
        super().__init__(self.name, self.msg, self.status)
        logging.error(self.msg)


class UserNotAuthenticatedError(ECOMBaseException):
    def __init__(self, name: Optional[str] = None, msg: Optional[str] = None):
        self.status = status.HTTP_401_UNAUTHORIZED
        if not name:
            self.name = "UserNotAuthenticatedError"
        else:
            self.name = name
        if not msg:
            self.msg = "User is not authenticated. Please login & try again."
        else:
            self.msg = msg
        super().__init__(self.name, self.msg, self.status)
        logging.error(self.msg)


class TokenError(ECOMBaseException):
    def __init__(self, name: Optional[str] = None, msg: Optional[str] = None):
        self.status = status.HTTP_401_UNAUTHORIZED
        if not name:
            self.name = "TokenError"
        else:
            self.name = name
        if not msg:
            self.msg = "User token may be expired."
        else:
            self.msg = msg
        super().__init__(self.name, self.msg, self.status)
        logging.error(self.msg)
