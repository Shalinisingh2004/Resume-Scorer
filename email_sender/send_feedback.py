import smtplib
from email.message import EmailMessage
import yaml
import os
import traceback
import time
from datetime import datetime

# Load credentials from config.yaml
def load_email_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config["email"]["address"], config["email"]["app_password"]

def log_email(to_email, status, reason=""):
    log_path = os.path.join(os.path.dirname(__file__), "email_log.txt")
    with open(log_path, "a") as log:
        log.write(f"{datetime.now()} - Email to {to_email} - Status: {status} - {reason}\n")

def prettify(key):
    return key.replace('_', ' ').title()

def send_email(to_email, name, score, breakdown, max_retries=3):
    from_email, app_password = load_email_config()

    strengths = [prettify(k) for k, v in breakdown.items() if v >= 10]
    improvements = [prettify(k) for k, v in breakdown.items() if v < 10]

    # Plaintext fallback
    plain_body = f"""
Hi {name},

Thank you for submitting your resume. Here are your results:

CV Score: {score}/100

Work Experience: {breakdown.get('experience_score', 0)}
Education: {breakdown.get('education_score', 0)}
AI Keywords: {breakdown.get('keyword_score', 0)}
Formatting: {breakdown.get('formatting_score', 0)}
Clarity: {breakdown.get('clarity_score', 0)}

Strengths: {', '.join(strengths) or 'None'}
Areas to Improve: {', '.join(improvements) or 'None'}

All the best,
CV Evaluation Team
"""

    # HTML email version
    html_body = f"""
    <html>
    <body>
        <p>Hi <strong>{name}</strong>,</p>
        <p>Thank you for submitting your resume. We’ve carefully evaluated it and here are your results:</p>
        <h3>📊 Overall CV Score: {score}/100</h3>
        <ul>
            <li><strong>📌 Work Experience</strong>: {breakdown.get('experience_score', 0)}</li>
            <li><strong>🎓 Education</strong>: {breakdown.get('education_score', 0)}</li>
            <li><strong>🤖 AI Keywords</strong>: {breakdown.get('keyword_score', 0)}</li>
            <li><strong>🗂️ Formatting</strong>: {breakdown.get('formatting_score', 0)}</li>
            <li><strong>🧠 Clarity</strong>: {breakdown.get('clarity_score', 0)}</li>
        </ul>
        <p><strong>✅ Strengths:</strong><br>{', '.join(strengths) or 'No strong areas detected yet — keep improving!'}</p>
        <p><strong>🔧 Areas to Improve:</strong><br>{', '.join(improvements) or 'None — great work!'}</p>
        <p>We encourage you to continue enhancing your resume. Good luck with your career journey!</p>
        <p>Warm regards,<br><em>CV Evaluation Team</em></p>
    </body>
    </html>
    """

    # Prepare email message
    msg = EmailMessage()
    msg["Subject"] = "Your Resume Evaluation Feedback"
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype="html")

    # Retry logic
    for attempt in range(max_retries):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(from_email, app_password)
                smtp.send_message(msg)
            print(f"[INFO] Email sent to {to_email}")
            log_email(to_email, "Success")
            break
        except Exception as e:
            print(f"[WARN] Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print(f"[ERROR] Failed to send email after {max_retries} attempts.")
                log_email(to_email, "Failed", reason=str(e))
                traceback.print_exc()
