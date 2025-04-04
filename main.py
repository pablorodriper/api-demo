from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my Render-hosted API!"}

@app.get("/music/")
def read_root():
    redirect_url = "https://music.apple.com/es/album/in-dream/1016488205"
    return RedirectResponse(redirect_url)
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/create-item/")
def create_item(name: str, description: str):
    return {"name": name, "description": description}
