from typing import Annotated, Optional

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


class CellMetadata(BaseModel):
    key: str
    value: str
    type: Optional[str] = None


class SpanBasedInputSentence(BaseModel):
    id: Annotated[int, "Line number of the document in zero-based index"]
    text: str
    metadata: Optional[list[CellMetadata]] = None


class SpanBasedInputDocument(BaseModel):
    id: Annotated[str, "Document id"]
    name: Annotated[str, "Document file name"]
    sentences: list[SpanBasedInputSentence]


class SpanBasedInput(BaseModel):
    id: Annotated[str, "Project id"]
    name: Annotated[str, "Project name"]
    documents: list[SpanBasedInputDocument]


class SpanBasedOutputEntity(BaseModel):
    label: str
    start_char: int
    end_char: int
    confidence_score: Optional[float] = None
    layer: int = 0


class SpanBasedOutputLabel(BaseModel):
    id: Annotated[int, "Line number of the document in zero-based index"]
    entities: list[SpanBasedOutputEntity]


class SpanBasedOutputDocument(BaseModel):
    id: Annotated[str, "Document id"]
    labels: list[SpanBasedOutputLabel]


class SpanBasedOutput(BaseModel):
    id: Annotated[str, "Project id"]
    documents: list[SpanBasedOutputDocument]
