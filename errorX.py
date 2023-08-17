from fastapi import FastAPI,HTTPException

app=FastAPI()

Items={"foo":"foo the  wrestler"}

@app.get('/items/item_id')
def get_items(item_id:str):
    if item_id not in Items:
        raise HTTPException(status_code=404,detail="Item not found",
        headers={"X-ERROR":"There goes my erro"},)
    return {"item":Items[item_id]}