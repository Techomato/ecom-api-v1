import uuid


def is_valid_uuid(input_str):
    try:
        uuid_obj = uuid.UUID(input_str)
        return str(uuid_obj) == input_str
    except ValueError:
        return False
