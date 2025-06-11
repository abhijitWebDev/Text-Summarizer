from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from fastapi.responses import Response  # Add this line
import os

app = FastAPI()

#API routes
app.include_router(router)

@app.get("/favicon.ico")
async def get_favicon():
    with open("static/favicon.ico", "rb") as f:
        favicon = f.read()
    return Response(favicon, media_type="image/x-icon")

# Serve static frontend files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
