from pydantic import BaseModel, ConfigDict


class PlayerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    disclaimer: str
    ranking: int
    profilepicurl: str
    goat: bool
    votes: list[int]


class PlayerUpdate(BaseModel):
    name: str
    disclaimer: str
    ranking: int
    profilepicurl: str
    goat: bool
    votes: list[int]
