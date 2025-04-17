import os
import time
from resume_parser.extract_data import extract_text, extract_info  # Assuming these functions are implemented

# Path to the folder where resumes are stored
resume_folder_path = "C:/Users/HP/Desktop/DOCUMENT/Shalini/cv_scoring_agent/resumes"

def process_resume(file_path):
    """
    Process a single resume file with retry on file-lock errors.

    Args:
        file_path (str): Full path to the resume file.

    Returns:
        dict or None: Extracted resume information or None on failure.
    """
    print(f"[INFO] Processing resume: {file_path}")

    for attempt in range(5):  # Retry logic to handle locked files
        try:
            time.sleep(1)  # Short wait before each attempt

            # Test read access (without actually reading contents)
            with open(file_path, "rb"):
                pass

            # Extract text and structured info
            resume_text = extract_text(file_path)
            resume_info = extract_info(resume_text)

            print("[INFO] Resume processed successfully.")
            return resume_info

        except PermissionError:
            print(f"[WARN] Attempt {attempt + 1}: File is locked, retrying...")
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Unexpected error while processing {file_path}: {e}")
            return None

    print(f"[ERROR] Failed to process {file_path} after multiple attempts.")
    return None

def fetch_resumes():
    """
    Scan the folder for resumes and extract data from each.

    Returns:
        list: A list of dictionaries containing extracted resume info.
    """
    print(f"[INFO] Scanning folder: {resume_folder_path} for resumes...")
    processed_resumes = []

    if not os.path.exists(resume_folder_path):
        print(f"[ERROR] Resume folder not found: {resume_folder_path}")
        return []

    for filename in os.listdir(resume_folder_path):
        if filename.lower().endswith((".pdf", ".docx")):
            file_path = os.path.join(resume_folder_path, filename)
            resume_info = process_resume(file_path)
            if resume_info:
                processed_resumes.append(resume_info)

    print(f"[INFO] Completed processing {len(processed_resumes)} resume(s).")
    return processed_resumes

if __name__ == "__main__":
    resumes_data = fetch_resumes()
    print(resumes_data)
