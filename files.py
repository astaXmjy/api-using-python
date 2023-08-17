from typing import Annotated

from fastapi import FastAPI, File, UploadFile,Form

from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes|None, File()]=None):
#     if not file:
#         return {"message":"file not sent"}
#     else:
#         return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile|None=None):
#     if not file:
#         return {"message" :"file not sent"}
#     else:
#         return {"filename": file.filename}

# @app.post("/files/")
# async def create_file(files: Annotated[list[bytes], File(description="A file read as bytes")],):
#         return {"file_size": [len(file) for file in files]}


# @app.post("/uploadfile/")
# async def create_upload_file(files: Annotated[list[UploadFile],File(description="A file reas as Uploadfile")]):
#         return {"filename": [file.filename for file in files]}

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)    

@app.post("/files/")
async def create_file(
    file:Annotated[bytes,File()],
    fileb:Annotated[UploadFile,File()],
    token:Annotated[str,Form()],
):
    return{
        "file_size":len(file),
        "token":token,
        "fileb_content_type":fileb.content_type,
    }           