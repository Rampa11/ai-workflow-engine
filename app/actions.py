import requests
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")


def send_email_action(data):
    to_email = data.get("email", "test@email.com")

    print("📧 WORKFLOW: Sending email to", to_email)

    payload = {
        "personalizations": [
            {
                "to": [{"email": to_email}],
                "subject": "Workflow Triggered"
            }
        ],
        "from": {"email": EMAIL_USER},
        "content": [
            {
                "type": "text/plain",
                "value": "Your workflow has been triggered successfully."
            }
        ]
    }

    response = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    print("📧 SENDGRID STATUS:", response.status_code)
    return f"Email status: {response.status_code}"


def log_action(data):
    print("📝 WORKFLOW LOG:", data)
    return "Logged successfully"