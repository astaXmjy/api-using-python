from fastapi import FastAPI
from .import models
from .database import engine
from fastapi.responses import HTMLResponse
from .routers import user,post,auth,vote
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)    


def generate_html_response():
    html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My Api</title>
<style>
      .button {
        background-color: #0000;
        border: none;
        color: #E7EBF9;
        padding: 20px 34px;
        text-align: center;
        
        text-decoration: none;
        display: inline-block;
        font-size: 40px;
        margin: 4px 2px;
        cursor: pointer;
      }
h1 {
color: #E7EBF9;
text-align: center;
}
  body {
    background-image: url('https://media.giphy.com/media/xT8qBhrlNooHBYR9f2/giphy.gif');
    background-repeat: repeat;
  }
</style>
</head>
<body>
<h1>Hii Konan Welcome❤️‍🔥 </h1>
<div style="text-align:center;">
   <a href="http://localhost:8000/docs" class="button">See My Api</a>
</div>
</body>
</html>

    """
    return HTMLResponse(content=html_content, status_code=200)
     
# origins=["https://www.google.com"] ___to restrict api

origins=["*"] #api is public


app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)    
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/",response_class=HTMLResponse)
def root():
    return generate_html_response()
 
                       

    
    
