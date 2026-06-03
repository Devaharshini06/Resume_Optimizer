def build_optimizer_prompt(
    parsed_resume,
    job_description,
    target_role
):

    return f"""
You are a Senior ATS Resume Optimization Expert.

Target Role:
{target_role}

Job Description:
{job_description}

Parsed Resume:
{parsed_resume}

Rules:

- Never invent experience.
- Never invent projects.
- Never invent certifications.
- Never invent education.
- Never invent achievements.
- Only use information already present in the resume.
- Rewrite content to improve ATS compatibility.
- Prioritize keywords from the job description where applicable.
- Extract skills exactly as they appear.
- Do not add technologies that are not present in either the resume or job description.

Return ONLY valid JSON.

Required Output Format:

{{
    "ats_score": 0,

    "resume_skills": [],

    "jd_skills": [],

    "matched_skills": [],

    "missing_skills": [],

    "skill_match_percentage": 0,

    "skill_gap_analysis": [
        {{
            "skill": "",
            "importance": "",
            "recommendation": ""
        }}
    ],

    "missing_keywords": [],

    "strengths": [],

    "weaknesses": [],

    "improvement_recommendations": [],

    "optimized_resume": ""
}}

Instructions:

1. Extract all technical skills from the resume.

2. Extract all technical skills from the job description.

3. Identify:
   - matched_skills
   - missing_skills

4. Calculate skill_match_percentage:
   (matched skills / total JD skills) * 100

5. Generate skill_gap_analysis.

For each missing skill provide:

- skill
- importance (High / Medium / Low)
- recommendation

Example:

{{
    "skill": "AWS",
    "importance": "High",
    "recommendation": "Add AWS deployment projects or cloud certifications if applicable."
}}

6. Calculate ATS score (0-100) based on:
   - Skill match
   - Keyword match
   - Resume completeness
   - Project relevance
   - Experience relevance

7. List missing ATS keywords.

8. List resume strengths.

9. List resume weaknesses.

10. Generate improvement_recommendations.

Example:

[
    "Add cloud deployment experience.",
    "Highlight API development more prominently.",
    "Include CI/CD workflows if applicable."
]

11. Generate a complete ATS-optimized resume.

optimized_resume must be a complete markdown resume containing:

# Full Name

Contact Information

## Professional Summary

## Technical Skills

## Projects

## Experience

## Education

## Certifications

Resume Requirements:

- Professional Summary must be tailored to the target role.
- Avoid generic phrases like:
  - Highly motivated
  - Passionate
  - Hardworking
  - Detail-oriented

- Project bullets should emphasize impact and technologies.
- Skills should be grouped into categories.
- Maintain ATS-friendly formatting.

Do not return markdown outside the JSON.
Do not return explanations.
Do not wrap JSON inside ```json.
The response must start with {{ and end with }}.
"""