import json
import pdfplumber

from prompts.parser_prompt import (
    build_parser_prompt
)

from services.groq_service import (
    generate_response
)


def extract_resume_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def parse_resume(resume_text):

    prompt = build_parser_prompt(
        resume_text
    )

    result = generate_response(
        prompt
    )

    result = result.replace(
        "```json",
        ""
    )

    result = result.replace(
        "```",
        ""
    )

    result = result.strip()

    return json.loads(result)