def build_cover_letter_prompt(
    parsed_resume,
    job_description,
    target_role
):

    return f"""
You are a professional career coach and recruiter.

Target Role:
{target_role}

Job Description:
{job_description}

Candidate Resume:
{parsed_resume}

Write a professional cover letter.

Requirements:

- Tailor the letter to the job description
- Highlight relevant skills and projects
- Use information from the resume only
- Do not invent experience
- Do not invent achievements
- Sound professional and natural
- Keep it between 300 and 500 words

Return ONLY JSON.

{{
    "cover_letter": ""
}}
"""