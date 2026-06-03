def build_parser_prompt(
    resume_text: str
):

    return f"""
Extract resume information.

Resume:

{resume_text}

Return ONLY JSON.

{{
    "name": "",
    "education": [],
    "projects": [],
    "skills": [],
    "experience": []
}}
"""