from pydantic import BaseModel


class ATSReport(BaseModel):
    ats_score: int
    missing_keywords: list[str]
    strengths: list[str]
    weaknesses: list[str]
    optimized_resume: str