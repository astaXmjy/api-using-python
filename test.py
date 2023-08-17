from fastapi import status, HTTPException, Cookie, responses, WebSocketException,  Depends,FastAPI,Header
from typing import Annotated

app=FastAPI()

def query_extractor(q:str|None=None):
    return q

def query_or_cookie_extractor(
    q:Annotated[str,Depends(query_extractor)],
    last_query:Annotated[str|None,Cookie()]=None
):
    if not q:
        return last_query
    return q

@app.get("/query/")
def read_query(
    query_or_default:Annotated[str,Depends(query_or_cookie_extractor)]
):
    return {"query_or_default": query_or_default}

def verify_token(x_token:Annotated[str,Header()]):
    if x_token!="Deeku":
        raise HTTPException(status_code=400,detail="X-Token header invalid")

def verify_key(x_key:Annotated[str,Header()]):
    if x_key!="Deekuawsm":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="X-Key header invalid")
    return x_key

@app.get("/keys/",dependencies=[Depends(verify_token),Depends(verify_key)])
def get_key():
    return {"Deeku u are awsm!"}