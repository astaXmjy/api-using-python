from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import BaseModel,Required


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict=item.dict()
    price_with_tax=item.price+item.tax
    item_dict.update({"price_with_tax ": price_with_tax})
    return item_dict


@app.post("/items/{item_id}")
async def create_item(item_id:int,item:Item,q:str|None=None):
    result={"item_id": item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result    

@app.get("/items/")
async def read_item(q:Annotated[str|None ,Query(min_length=3,max_length=50)]=Required):
    results={"items ":[{"item_id":"Foo"},{"item_id": "Bar"}]}
    if q:
         results.update({"q":q})
    return results

@app.get("/items1/")
async def read_item(q:Annotated[list[str]|None ,Query()]=["Hi","Konan"]):
    query_items={"q":q}
    return query_items
 
        
