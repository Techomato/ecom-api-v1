import uuid
from typing import List

from _decimal import Decimal

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.models.db_models.category import Category
from products.models.db_models.sub_category import SubCategory


def is_valid_uuid(input_str):
    try:
        uuid_obj = uuid.UUID(input_str)
        return str(uuid_obj) == input_str
    except ValueError:
        return False


def validate_actual_price(actual_price: str):
    if isinstance(actual_price, str):
        actual_price = actual_price.strip()
    actual_price = Decimal(actual_price)
    if actual_price <= 0:
        raise ECOMValueError(msg="Actual Price can not be zero or negative")
    if actual_price >= 1000000:
        raise ECOMValueError(msg="Price can not be greater than Rs.9,99,999")


def validate_offer_price(offer_price: str, actual_price: str):
    if isinstance(offer_price, str):
        offer_price = offer_price.strip()
    offer_price = Decimal(offer_price)

    if isinstance(actual_price, str):
        actual_price = actual_price.strip()
    actual_price = Decimal(actual_price)

    if offer_price <= 0:
        raise ECOMValueError(msg="Offer Price can not be zero or negative")
    if offer_price > actual_price:
        raise ECOMValueError(msg="Offer Price can not be grater than actual price")


def validate_category_type(category_type: str):
    category_type = Category.objects.filter(name=category_type).first()
    if not category_type:
        raise ECOMValueError(msg="Category is not listed")


def validate_subcategory_type(subcategory_type: str, category_type: str):
    sub_category_type: SubCategory = SubCategory.objects.filter(
        name=subcategory_type
    ).first()
    if not sub_category_type:
        raise ECOMValueError(msg="Sub Category is not listed")
    elif sub_category_type.category.name != category_type:
        raise ECOMValueError(msg="Category & Sub Category are not matching")


def validate_product_name(product_name: str):
    if product_name == "":
        raise ECOMValueError(msg="Product name should have length more than 5")
    if product_name and len(product_name) < 5:
        raise ECOMValueError(msg="Product name should have length more than 5")


def validate_product_image(product_image: str):
    if product_image == "":
        raise ECOMValueError(msg="Product image can not be a empty string")
    if product_image and len(product_image) < 4:
        raise ECOMValueError(msg="Product image URL is invalid")


def validation_product_image_list(product_image_list: List[str]):
    if product_image_list:
        for image in product_image_list:
            validate_product_image(image)
    if product_image_list is not None and len(product_image_list) == 0:
        raise ECOMValueError(msg="Product image list can't be empty")


def validate_update_request_product_data(data: dict):
    validate_actual_price(data.get("actual_price"))
    validate_offer_price(
        offer_price=data.get("offer_price"), actual_price=data.get("actual_price")
    )
    validate_category_type(data.get("category"))
    validate_subcategory_type(
        subcategory_type=data.get("subcategory"), category_type=data.get("category")
    )
    validate_product_name(data.get("product_name"))
    validate_product_image(data.get("image"))
    validation_product_image_list(data.get("product_image_list"))


def validate_brand(brand: str):
    if brand == "":
        raise ECOMValueError(msg="Brand is required")
    if not brand:
        raise ECOMValueError(msg="Brand is required")


def validate_stock(stock: int):
    if not stock or int(stock) < 0:
        raise ECOMValueError(
            msg="Product quantity can not be zero or negative or fractional"
        )


def validate_category_name_for_add_product(category: str):
    if not category:
        raise ECOMValueError(msg="Category Name is required")
    validate_category_type(category)


def validate_subcategory_name_for_add_product(subcategory: str, category: str):
    if not subcategory:
        raise ECOMValueError(msg="Sub Category Name is required")
    validate_subcategory_type(subcategory_type=subcategory, category_type=category)


def validate_actual_price_for_add_product(actual_price: Decimal):
    if not actual_price:
        raise ECOMValueError(msg="Actual Price is required")
    validate_actual_price(str(actual_price))


def validate_offer_price_for_add_product(actual_price: Decimal, offer_price: Decimal):
    if not offer_price:
        raise ECOMValueError(msg="Offer Price is required")
    validate_offer_price(offer_price=str(offer_price), actual_price=str(actual_price))


def validate_stock_for_add_product(stock: int):
    if not stock:
        raise ECOMValueError(msg="Product stock value is required")
    if not isinstance(stock, int):
        validate_stock(stock)


def validate_image_for_add_product(image: str):
    if not image:
        raise ECOMValueError(msg="Product image is required")
    validate_product_image(image)


def validate_product_name_for_add_product(product_name: str):
    if not product_name:
        raise ECOMValueError(msg="Product name is required")
    validate_product_name(product_name)


def validate_add_request_product_data(data: dict):
    validate_product_name_for_add_product(data.get("name"))
    validate_image_for_add_product(data.get("product_image"))
    validate_brand(data.get("brand"))
    validate_category_name_for_add_product(data.get("category"))
    validate_subcategory_name_for_add_product(
        subcategory=data.get("subCategory"), category=data.get("category")
    )
    validate_description(data.get("description"))
    validate_actual_price_for_add_product(data.get("actual_price"))
    validate_offer_price_for_add_product(
        offer_price=data.get("offer_price"), actual_price=data.get("actual_price")
    )
    validate_stock_for_add_product(data.get("countInStock"))
    validation_product_image_list(data.get("product_image_list"))


def validate_category_name(category_name: str):
    if not category_name:
        raise ECOMValueError(msg="Category name is required")
    else:
        category_type = Category.objects.filter(name=category_name)
        if category_type:
            raise ECOMValueError(
                msg=f"'{category_name}' category name already available"
            )


def validate_description(description: str):
    if description == "":
        raise ECOMValueError(msg="Description can not be empty")


def validate_category(category: dict):
    validate_category_name(category.get("category_name"))

    validate_product_image(category.get("image"))

    validate_description(category.get("description"))


def validate_subCategory(data: dict):
    if not data.get("sub_category_name"):
        raise ECOMValueError(msg="Sub Category name is required")

    filtered_sub_category_type_list = SubCategory.objects.filter(
        name=data.get("sub_category_name")
    )
    if filtered_sub_category_type_list.exists():
        raise ECOMValueError(
            msg=f"Sub Category name '{filtered_sub_category_type_list.first().name}' already available in "
            f"'{filtered_sub_category_type_list.first().category.name}'"
        )

    if not data.get("category_name"):
        raise ECOMValueError(msg="Category name is required")

    validate_category_type(data.get("category_name"))

    validate_product_image(data.get("image"))

    validate_description(data.get("description"))
