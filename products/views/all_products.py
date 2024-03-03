from psycopg2 import DatabaseError
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema
from products.models.export_models.export_product import ExportECOMProductList
from products.utils.interfaces.types.request_and_response_types.response_types.all_product_response_type import (
    AllProductResponseData,
)
from products.services.product_services.product_services import ProductServices


class AllProduct(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        responses={200: ExportECOMProductList},
    )
    def get(self, _):
        # try:
        all_products = ProductServices().get_all_products_service()
        if all_products and isinstance(all_products, ExportECOMProductList):
            data = AllProductResponseData(data=all_products)
            return Response(
                data=data.model_dump(),
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            raise DatabaseError()
        # except DatabaseError as e:
        #     logging.error(
        #         f"DatabaseError: Error Occurred While Fetching all users details: {e}"
        #     )
        #     response_data = ResponseData(
        #         errorMessage=f"DatabaseError: Error Occurred While Fetching all users details: {e}"
        #     )
        #     return Response(
        #         data=response_data.model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        # except ValidationError as e:
        #     logging.error(
        #         f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
        #     )
        #     response_data = ResponseData(
        #         errorMessage=f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
        #     )
        #     return Response(
        #         data=response_data.model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        # except NotImplementedError as e:
        #     logging.warning(f"NotImplementedError: {e}")
        #     response_data = ResponseData(errorMessage=f"NotImplementedError: {e}")
        #     return Response(
        #         data=response_data.model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
        # except Exception as e:
        #     logging.error(f"InternalServerError: {e}")
        #     response_data = ResponseData(errorMessage=f"InternalServerError: {e}")
        #     return Response(
        #         data=response_data.model_dump(),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content_type="application/json",
        #     )
