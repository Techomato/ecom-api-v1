import json

from rest_framework.request import Request

from ecom_exceptions.ecom_exceptions import UserNotAuthenticatedError
from products.services.auth_services.definitions import AUTH_HOST, SELLER_DETAILS_PATH
from products.services.ecom_requests.ecom_requests import ECOMRequests


class SellerServices:
    def get_seller_id(self, request: Request):
        token = self._get_jwt_token_from_request(request=request)
        ecomRequest = ECOMRequests(host=AUTH_HOST, with_ssl=False)
        headers = {"Authorization": f"Bearer {token}"}
        response = ecomRequest.get(path=SELLER_DETAILS_PATH, headers=headers)
        response = json.loads(response.text)
        if response.get("errorMessage"):
            raise UserNotAuthenticatedError(msg=response.get("errorMessage"))
        if response.get("data") and response.get("data").get("id"):
            return response.get("data").get("id")

    def _get_jwt_token_from_request(self, request: Request) -> str:
        try:
            token = request.headers.get("Authorization", "").split(" ")[1]
            return token
        except IndexError:
            raise UserNotAuthenticatedError(
                msg="Authentication token is not found in headers."
            )
