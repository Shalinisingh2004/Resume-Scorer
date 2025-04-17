# main.py
import os
from resume_collector.fetch_resumes import fetch_resumes
from resume_parser.extract_data import extract_text, extract_info
from scoring_engine.score_resume import score_resume
from email_sender.send_feedback import send_email

def main():
    fetch_resumes()
    resume_dir = "resumes/"

    for filename in os.listdir(resume_dir):
        filepath = os.path.join(resume_dir, filename)
        print(f"\n📄 Processing: {filename}")

        try:
            text = extract_text(filepath)
            info = extract_info(text)
            email = info.get("email")
            name = info.get("masked_name", "Candidate")

            if not email:
                print("❌ Skipped: No valid email found in the resume.")
                continue

            score, breakdown = score_resume(text, info)

            print(f"📬 Sending email to: {email}")
            send_email(email, name, score, breakdown)
            print("✅ Email sent successfully!")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
