from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my Render-hosted API!"}

@app.get("/music", response_class=RedirectResponse, status_code=302)
async def get_music():
    redirect_url = "https://music.apple.com/es/album/in-dream/1016488205"
    return redirect_url

discs_list = [
    "https://embed.music.apple.com/es/album/s%C3%BAbete-la-radio/1722256361",
    "https://embed.music.apple.com/es/album/in-dream/1016488205",
]

@app.get("/music_iframe")
def get_music_iframe():
    import random
    disc_url = random.choice(discs_list)

    html_content = f"""
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tu disco para hoy</title>
      <style>
        body {{
          margin: 0;
          font-family: Arial, sans-serif;
        }}
        .container {{
          text-align: center;
          padding: 20px;
        }}
        .responsive-iframe {{
          width: 100%;
          max-width: 660px;
          height: 1000px;
          overflow: hidden;
          background: transparent;
          border: none;
        }}
        @media (max-width: 480px) {{
          .responsive-iframe {{
            height: 110px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Recomendación de hoy</h1>
        <br></br>
        <iframe
          class="responsive-iframe"
          allow="autoplay *; encrypted-media *;"
          sandbox="allow-scripts allow-same-origin allow-popups"
          src="{disc_url}">
        </iframe>
      </div>
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
