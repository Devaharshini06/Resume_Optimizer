from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import os

from services.parser_service import (
    extract_resume_text,
    parse_resume
)

from services.cover_letter_service import (
    generate_cover_letter_service
)

router = APIRouter()


@router.post("/generate")
async def generate_cover_letter(

    resume: UploadFile = File(...),

    job_description: str = Form(...),

    target_role: str = Form(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{resume.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await resume.read()
        )

    resume_text = extract_resume_text(
        file_path
    )

    parsed_resume = parse_resume(
        resume_text
    )

    result = generate_cover_letter_service(
        parsed_resume,
        job_description,
        target_role
    )

    return result