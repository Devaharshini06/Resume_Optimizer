import json

from prompts.cover_letter_prompt import (
    build_cover_letter_prompt
)

from services.groq_service import (
    generate_response
)


def generate_cover_letter_service(
    parsed_resume,
    job_description,
    target_role
):

    prompt = build_cover_letter_prompt(
        parsed_resume,
        job_description,
        target_role
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