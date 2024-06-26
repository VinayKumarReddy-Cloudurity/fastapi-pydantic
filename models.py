# models.py
from pydantic import BaseModel, Field

class ConversionRequest(BaseModel):
    value: float = Field(..., description="The value to be converted")
    unit: str = Field(..., description="The current unit of the value")
    convert_to: str = Field(..., description="The unit to convert the value to")

class ConversionResponse(BaseModel):
    value: float = Field(..., description="The converted value")
    unit: str = Field(..., description="The unit of the converted value")
