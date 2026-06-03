from fastapi import APIRouter
from pydantic import BaseModel

from services.groq_service import (
    generate_response
)

router = APIRouter()


class ChatRequest(BaseModel):

    message: str

    resume_context: dict | None = None


@router.post("/")
def chat(
    data: ChatRequest
):

    prompt = f"""
You are Hustle Hive AI.

Candidate Resume:

{data.resume_context}

User Question:

{data.message}

Provide career advice based on
the candidate's actual resume.

Focus on:

- ATS optimization
- Internships
- Software Engineering
- AI Engineering
- Projects
- Resume Improvement
- Interview Preparation
"""

    result = generate_response(
        prompt
    )

    return {
        "response": result
    }