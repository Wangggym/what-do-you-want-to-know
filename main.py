from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/')
async def root():
    return {"message": "Hello World"}

# Optional parameters
# The same way, you can declare optional query parameters, by setting their default to None:
@app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"})
    return item


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {"model_name": model_name, 'message': 'LeCNN all the images'}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{'item_name': 'Foo'}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items')
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]
