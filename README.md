# 🤖 Resume Scoring Agent

This project is a Resume Scoring Agent that processes candidate resumes, extracts relevant information using NLP techniques, and assigns a score based on predefined criteria like AI-related experience and education. It can be used to automate resume screening in hiring workflows.

---

## 🛠 Features

- 📄 **Supports PDF and DOCX resumes**
- 📥 **Bulk resume parsing from a folder**
- 🔍 **Extracts key data like Name, Email, Batch Year, AI Skills**
- 🧠 **Identifies AI-related experience**
- 📊 **Returns scores with breakdowns**
- 📧 **Sends email notifications to candidates**

---

## 📂 Project Structure

cv_scoring_agent/ │ ├── main.py # Entry point ├── resume_collector/ │ └── fetch_resumes.py # Scans and processes resumes from directory ├── resume_parser/ │ └── extract_data.py # Contains text and info extraction logic ├── utils/ │ └── email_sender.py # Email utility to send results ├── config.yaml # Stores sender email and app password └── resumes/ # Folder to drop all input resumes

---

## ⚙️ Setup Instructions

git clone https://github.com/your-username/resume-scoring-agent.git
cd resume-scoring-agent
2. Install dependencies
pip install -r requirements.txt
Requirements:
•	PyPDF2
•	python-docx
•	pyyaml
3. Configure your email credentials
Create or edit the config.yaml file in the root directory with your own Gmail address and App Password like so:
email:
  sender: your_email@gmail.com
  app_password: your_generated_app_password
⚠️ Note: Do not use your regular Gmail password. Use an App Password created from your Google Account.
4. Place resumes
Put all your .pdf and .docx resumes inside the resumes/ folder.
5. Run the agent
python main.py
________________________________________
🧠 Example Output
[INFO] Scanning folder: resumes/ for existing resumes...
[INFO] Processing resume: resumes/Shalini_resume.pdf
[INFO] Resume processed successfully.
You are sending email to: shalinisinghapdj@gmail.com
[INFO] Completed processing 1 resumes.
________________________________________
✅ To-Do
•	Add a scoring engine based on skills and education
•	Web interface for uploading resumes
•	Integrate with job portals
•	Mask email for privacy logs
________________________________________
🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.
________________________________________
📝 License
This project is licensed under the MIT License.
________________________________________
📧 Contact
Created by Your Name – feel free to reach out!

---

Let me know if you’d like a sample `config.yaml`, a `.gitignore` for it, or want to convert it into a website-friendly `README` with visuals.


![image](https://github.com/user-attachments/assets/496939e1-c6fb-4961-8406-11f4c350d7a1)

![image](https://github.com/user-attachments/assets/62ec0d40-e315-448b-bea2-bf66bc2241d9)



