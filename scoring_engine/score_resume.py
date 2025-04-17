import re

def score_resume(text, extracted_info):
    score = 0
    detail = {}

    # Work Experience Scoring
    # Look for patterns like "3 years", "5+ years", etc.
    exp_matches = re.findall(r"\d+\+?\s+years?", text.lower())
    exp_years = len(exp_matches)
    experience_score = min(exp_years * 10, 30)  # Max 30 points
    score += experience_score
    detail['experience_score'] = experience_score

    # Education Scoring
    education_keywords = ["bachelor", "master", "ph.d", "phd"]
    if any(edu in text.lower() for edu in education_keywords):
        education_score = 20
    else:
        education_score = 0
    score += education_score
    detail['education_score'] = education_score

    # AI Keywords Scoring
    ai_keywords = extracted_info.get('ai_experience', [])
    keyword_score = min(len(ai_keywords) * 5, 25)  # Max 25 points
    score += keyword_score
    detail['keyword_score'] = keyword_score

    # Formatting Scoring
    # Heuristic: if resume has too many lines, assume poor formatting
    line_count = len(text.strip().split("\n"))
    formatting_score = 10 if line_count < 60 else 0
    score += formatting_score
    detail['formatting_score'] = formatting_score

    # Clarity Scoring
    # Heuristic: resumes with <1000 words are likely more concise
    word_count = len(text.split())
    clarity_score = 5 if word_count < 1000 else 0
    score += clarity_score
    detail['clarity_score'] = clarity_score

    return score, detail
