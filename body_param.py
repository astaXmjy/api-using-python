from fastapi import FastAPI, Path,Body
from pydantic import BaseModel,Field
from typing import Annotated

app = FastAPI()


class Image(BaseModel):
    url:str
    name1:str

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,title="The description of item",max_length=300
    )
    price: float=Field(gt=0,description="The price must be greater than 0(Zero)")
    tax: float | None = None
    image:Image|None=None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
                "url":"asta",
                "name1":"mjy"
            }
        }


class  User(BaseModel):
    username:str
    full_name:str|None=None

@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Annotated[Item,Body(embed=True)],user:User,importance: Annotated[int, Body()],
    q: str | None = None,):
    results={"Item_id":item_id,"Item":item,"User":user,"Importance":importance}
    if q:
        results.update({"q":q})
    print(q)
    return results
