from typing import Optional, Any

from pydantic import BaseModel


class ResponseData(BaseModel):
    data: Any = None
    errorMessage: Optional[str] = None
    successMessage: Optional[str] = None
