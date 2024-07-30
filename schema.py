from typing import Optional

from pydantic import BaseModel


class RowBasedInputItem(BaseModel):
    id: int 
    text: str
    columns: list[str]
    column_names: list[str]


class RowBasedOutputItem(BaseModel):
    id: int
    label: str
    confidence_score: Optional[float] = None
