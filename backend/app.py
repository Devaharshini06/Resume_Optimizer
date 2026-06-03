from fastapi import FastAPI

from routes.resume import (
    router as resume_router
)
from routes.cover_letter import (
    router as cover_letter_router
)
from routes.chat import (
    router as chat_router
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    cover_letter_router,
    prefix="/cover-letter",
    tags=["Cover Letter"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }