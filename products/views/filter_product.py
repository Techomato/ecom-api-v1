import logging
from pydantic import ValidationError

from psycopg2 import DatabaseError
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from ecom_exceptions.base_exception import ECOMBaseException
from products.models.export_models.export_category import ExportECOMCategoryList
from products.utils.interfaces.types.request_and_response_types.response_types.all_category_subcategory_response_type import (
    AllCategorySubcategoryResponseData,
)
from products.services.product_services.product_services import ProductServices
from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class FilterProduct(APIView):
    renderer_classes = [JSONRenderer]

    # @extend_schema(
    #     responses={200: ExportECOMProductList},
    # )
    def get(self, _):
        try:
            # all_cat_subCat = (
            #     ProductServices().get_all_categories_subcategories_service()
            # )
            # if all_cat_subCat and isinstance(all_cat_subCat, ExportECOMCategoryList):
            #     data = AllCategorySubcategoryResponseData(data=all_cat_subCat)
            #     return Response(
            #         data=data.model_dump(),
            #         status=status.HTTP_200_OK,
            #         content_type="application/json",
            #     )
            return Response(
                data={},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
            # else:
            #     raise Exception()
        except ECOMBaseException as e:
            return Response(
                data=ResponseData(errorMessage=f"{e.name}: {e.msg}").model_dump(),
                status=e.status,
                content_type="application/json",
            )
        except DatabaseError as e:
            logging.error(
                f"DatabaseError: Error Occurred While Fetching all users details: {e}"
            )
            response_data = ResponseData(
                errorMessage=f"DatabaseError: Error Occurred While Fetching all users details: {e}"
            )
            return Response(
                data=response_data.model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except ValidationError as e:
            logging.error(
                f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
            )
            response_data = ResponseData(
                errorMessage=f"PydanticValidationError: Error Occurred while converting to Pydantic object: {e}"
            )
            return Response(
                data=response_data.model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except NotImplementedError as e:
            logging.warning(f"NotImplementedError: {e}")
            response_data = ResponseData(errorMessage=f"NotImplementedError: {e}")
            return Response(
                data=response_data.model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except Exception as e:
            logging.error(f"InternalServerError: {e}")
            response_data = ResponseData(errorMessage=f"InternalServerError: {e}")
            return Response(
                data=response_data.model_dump(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
