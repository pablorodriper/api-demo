from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my Render-hosted API!"}

@app.get("/music/")
def get_music_page():
    redirect_url = "music.apple.com/es/album/in-dream/1016488205"
    return RedirectResponse(redirect_url)
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/create-item/")
def create_item(name: str, description: str):
    return {"name": name, "description": description}
