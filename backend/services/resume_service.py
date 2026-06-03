import json

from prompts.optimizer_prompt import (
    build_optimizer_prompt
)

from services.groq_service import (
    generate_response
)


def optimize_resume_service(
    parsed_resume,
    job_description,
    target_role
):

    prompt = build_optimizer_prompt(
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