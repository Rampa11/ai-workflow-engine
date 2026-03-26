# ⚙️ AI Workflow Engine

A dynamic automation system that evaluates conditions and executes actions (like email notifications) in real time based on incoming events.

---

## 🌍 Live Demo

* 🔗 API: https://ai-workflow-engine-q9nd.onrender.com
* 📘 Swagger UI: https://ai-workflow-engine-q9nd.onrender.com/docs

---

## 🧠 Overview

The AI Workflow Engine allows users to define workflows consisting of:

* Triggers (events)
* Conditions (logic rules)
* Actions (execution like sending emails or logging)

Workflows are stored in a database and executed dynamically when events occur.

---

## ⚙️ Features

* Dynamic workflow creation via API
* Conditional evaluation engine
* Multi-workflow execution
* Real-time action execution (SendGrid email + logging)
* Event-driven architecture
* Modular and scalable backend design

---

## 🏗️ Architecture

Event → Load Workflows → Evaluate Conditions → Execute Actions

---

## 🔧 Tech Stack

* FastAPI (Backend API)
* SQLAlchemy (Database ORM)
* SendGrid API (Email automation)
* Python

---

## 📡 API Usage

### ➤ Create Workflow

POST /workflows/

Example Request:

{
"trigger": "lead_created",
"condition": "status == HOT",
"actions": ["send_email", "log"]
}

---

### ➤ Trigger Workflow

POST /trigger/

Example Request:

{
"status": "HOT",
"email": "[aunukogbon@gmail.com](mailto:aunukogbon@gmail.com)"
}

---

## 🎯 Example Flow

1. Create a workflow
2. Trigger an event
3. System evaluates condition
4. Executes actions (email + logging)

---

## 🎯 Use Cases

* Business process automation
* CRM workflows
* Notification systems
* AI-driven decision pipelines

---

## ▶️ Run Locally

Start backend:

python -m uvicorn app.main:app --reload

---

## 🚀 Deployment

* Backend deployed on Render
* Environment variables securely managed

---

## 👤 Author

Akpor Unukogbon

* GitHub: https://github.com/Rampa11
* LinkedIn: https://www.linkedin.com/in/akpor-unukogbon-104532b8

---

## ⭐️ If you like this project

Give it a ⭐️ — it helps!
