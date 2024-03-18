import logging

from pydantic import ValidationError
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from psycopg2 import DatabaseError

from ecom_exceptions.base_exception import ECOMBaseException
from products.services.product_services.product_services import ProductServices
from products.utils.interfaces.types.request_and_response_types.request_types.add_subCategory_request_type import \
    AddSubCategoryRequestType

from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class UpdateProductView(APIView):
    renderer_classes = [JSONRenderer]

    # @extend_schema(
    #     request=CreateUserRequestType,
    #     responses={200: ResponseData},
    # )
    def post(self, request: Request):
        try:
            result: ResponseData = ProductServices().add_subCategory_service(
                request_data=AddSubCategoryRequestType(**request.data), request=request
            )

            return Response(
                data=result.model_dump(),
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except ECOMBaseException as e:
            return Response(
                data=ResponseData(errorMessage=f"{e.name}: {e.msg}").model_dump(),
                status=e.status,
                content_type="application/json",
            )
        except DatabaseError as e:
            logging.error(
                f"DatabaseError: Error Occurred While saving product details: {e}"
            )
            return Response(
                data=ResponseData(
                    errorMessagee=f"DatabaseError: Error Occurred While saving product details: {e}",
                ).model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except ValidationError as e:
            logging.error(
                f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
            )
            return Response(
                data=ResponseData(
                    errorMessage=f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
                ).model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except NotImplementedError as e:
            logging.warning(f"Internal Server Error: {e}")
            return Response(
                data={
                    "successMessage": None,
                    "errorMessage": f"NotImplementedError: {e}",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except Exception as e:
            logging.warning(f"InternalServerError: {e}")
            return Response(
                data={
                    "successMessage": None,
                    "errorMessage": f"InternalServerError: {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json",
            )
