from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi.responses import FileResponse

import os

from services.parser_service import (
    extract_resume_text,
    parse_resume
)

from services.resume_service import (
    optimize_resume_service
)

from services.docx_service import (
    generate_docx
)

router = APIRouter()


@router.post("/upload")
async def upload_resume(

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

    result = optimize_resume_service(
        parsed_resume,
        job_description,
        target_role
    )

    return result


@router.post("/download")
async def download_resume(

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

    result = optimize_resume_service(
        parsed_resume,
        job_description,
        target_role
    )

    doc_path = generate_docx(
        result["optimized_resume"],
        "optimized_resume.docx"
    )

    return FileResponse(
        doc_path,
        filename="optimized_resume.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )