from pydantic import BaseModel
from app.models import Group, Country


class Attack(BaseModel):
    type: str
    target: str
    group: Group
    country: Country
