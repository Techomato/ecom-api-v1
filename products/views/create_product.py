from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ecom_exceptions.base_exception import ECOMBaseException
from products.services.product_services.product_services import ProductServices
from products.utils.interfaces.types.request_and_response_types.request_types.create_product_request_type import (
    CreateProductRequestType,
)
from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class CreatProductView(APIView):
    renderer_classes = [JSONRenderer]

    # @extend_schema(
    #     request=CreateUserRequestType,
    #     responses={200: ResponseData},
    # )
    def post(self, request: Request):
        try:
            result: ResponseData = ProductServices.create_new_product_service(
                request_data=CreateProductRequestType(**request.data), request=request
            )
            return Response(
                data=result.model_dump(),
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )
        except ECOMBaseException as e:
            return Response(
                data=ResponseData(errorMessage=f"{e.name}: {e.msg}").model_dump(),
                status=e.status,
                content_type="application/json",
            )
        # except DatabaseError as e:
        #     logging.error(
        #         f"DatabaseError: Error Occured While saving users details: {e}"
        #     )
        #     return Response(
        #         data=ResponseData(
        #             errorMessagee=f"DatabaseError: Error Occured While saving users details: {e}",
        #         ).model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        # except ValidationError as e:
        #     logging.error(
        #         f"PydanticValidationError: Error Occured while converting to Pydantic object: {e}"
        #     )
        #     return Response(
        #         data=ResponseData(
        #             errorMessage=f"PydanticValidationError: Error Occured while converting to Pydantic object: {e}"
        #         ).model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        # except NotImplementedError as e:
        #     logging.warning(f"Internal Server Error: {e}")
        #     return Response(
        #         data=ResponseData(
        #             errorMessage=f"NotImplementedError: {e}"
        #         ).model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        #
        # except AUTHBaseException as e:
        #     return Response(
        #         data=ResponseData(errorMessage=f"{e.name}: {e.msg}").model_dump(),
        #         status=e.status,
        #         content_type="application/json",
        #     )
