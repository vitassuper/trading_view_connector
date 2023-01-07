from typing import Literal
from pydantic import BaseModel

class OpenSignal(BaseModel):
    type_of_signal: Literal['open']
    pair: str
    amount: float

class CloseSignal(BaseModel):
    type_of_signal: Literal['close']
    pair: str

class AddSignal(BaseModel):
    type_of_signal: Literal['add']
    pair: str
    amount: float
