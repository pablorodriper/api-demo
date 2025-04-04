from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my Render-hosted API!"}

@app.get("/music/")
def get_music_page():
    redirect_url = "https://music.apple.com/es/album/in-dream/1016488205"
    return RedirectResponse(redirect_url)

@app.get("/music_iframe/", response_class=HTMLResponse)
def get_music_iframe():
    html_content = """
    <html>
      <head>
        <title>Your Random Disc</title>
      </head>
      <body>
        <iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0" height="450" style="width:100%;max-width:660px;overflow:hidden;border-radius:10px;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.music.apple.com/es/album/in-dream/1016488205"></iframe>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/create-item/")
def create_item(name: str, description: str):
    return {"name": name, "description": description}
