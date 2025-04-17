import re
from PyPDF2 import PdfReader
from docx import Document

def extract_text(filepath):
    """
    Extract text content from PDF or DOCX files.

    Args:
        filepath (str): Path to the resume file.

    Returns:
        str: Combined text content of all pages/paragraphs.
    """
    try:
        if filepath.endswith(".pdf"):
            reader = PdfReader(filepath)
            return "\n".join(
                page.extract_text() for page in reader.pages if page.extract_text()
            )
        elif filepath.endswith(".docx"):
            doc = Document(filepath)
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception as e:
        print(f"[Error] Failed to extract text from {filepath}: {e}")
    return ""

def extract_info(text):
    """
    Extract key resume information from raw text.

    Args:
        text (str): Text content of the resume.

    Returns:
        dict: Dictionary with extracted name, email, batch years, and AI experience.
    """
    # Extract email using regex
    email_matches = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text
    )
    email = email_matches[0] if email_matches else None
    masked_email = email  # Currently not masking email

    # Extract name: assuming the first non-empty line
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
    name = lines[0] if lines else "Unknown"
    masked_name = name[:5] + "*****" if len(name) >= 5 else name + "*****"

    # Extract batch years
    batch_years = sorted(set(re.findall(r"\b20\d{2}\b", text)))

    # Detect AI-related keywords
    ai_keywords = ["machine learning", "deep learning", "AI", "NLP", "computer vision"]
    ai_experience = [
        kw for kw in ai_keywords if re.search(rf"\b{re.escape(kw)}\b", text, re.IGNORECASE)
    ]

    return {
        "name": name,
        "masked_name": masked_name,
        "email": email,
        "masked_email": masked_email,
        "batch_years": batch_years,
        "ai_experience": ai_experience
    }
