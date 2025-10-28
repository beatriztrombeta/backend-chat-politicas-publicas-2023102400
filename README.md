# Chat – Public Policies and Affirmative Actions (FAPESP 2023/10240-0)

This repository contains the **backend system** for the chat and question interface of the research project funded by **FAPESP (Grant No. 2023/10240-0)** titled:
**“Public Policies and Affirmative Actions in the Public University: defining an algorithm to alert for dropout risk among university entrants through quota and reservation systems.”**

---

## 🎯 Project Goal

The main goal of this system is to provide an **interactive chat interface** that integrates **natural language understanding** and **data-driven decision support**.
Through this backend, users can interact with a chatbot powered by **Gemini AI**, which interprets questions, queries a **PostgreSQL** database, and returns relevant **BI reports** to support university managers and educators.

This tool combines artificial intelligence, educational data analysis, and machine learning insights to strengthen institutional policies for **student permanence and inclusion**.

---

## 🧠 Core Research Themes

This project explores the following interdisciplinary research areas:

* **University Dropout:** Understanding and predicting factors that influence student retention and dropout risk.
* **Artificial Intelligence in Education:** Applying machine learning and natural language models to identify behavioral and academic patterns.
* **Affirmative Actions:** Supporting inclusion and equity for quota students in higher education.
* **Public Policy and Educational Management:** Using data to enhance institutional strategies for student success.

This research connects specialists in **education, mathematics, and information technology** to develop tools that promote more inclusive higher education environments.

---

## 🧩 Repository Structure

```
backend-chat-politicas-publicas-2023102400/
│
├── app/
│   ├── controllers/
│   ├── services/
│   ├── utils/
│   ├── views/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
|   ├── routes.py
│   └── schemas.py
│
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md 
└── requirements.txt
```

---

## ⚙️ Technologies Used

* **Python 3.11**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Pydantic v2 + pydantic-settings**
* **JWT Authentication**
* **SMTP Email Service**
* **Docker & Docker Compose**
* **Gemini API**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/backend-chat-politicas-publicas-2023102400.git
cd backend-chat-politicas-publicas-2023102400
```

### 2. Configure the environment

Create a `.env` file based on `.env.example` and fill in your credentials:

```
DATABASE_URL=postgresql://postgres:password@db:5432/chatdb
JWT_SECRET_KEY=changeme
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=example@example.com
SMTP_PASS=changeme
```

### 3. Build and run the containers

```bash
docker-compose build
docker-compose up
```

The backend will be available at:

```
http://localhost:8000
```

You can access the **interactive API documentation** at:

```
http://localhost:8000/docs
```

---

## 🧪 Authentication Flow

The system implements a **passwordless login** mechanism:

1. The user enters their email address.
2. If the email exists in the database, the backend generates a **numeric verification code** and sends it via **SMTP**.
3. The user submits the code to verify their identity.
4. Upon successful validation, the backend issues a **JWT token** for session management.

---

## 🧩 Chat Logic

When a user asks a question:

1. The backend forwards the question to the **Gemini API**.
2. Gemini interprets the question and returns both an **answer** and a **numeric identifier**.
3. The backend uses this identifier to fetch a **corresponding BI report link** from the database (`Report` table).
4. Both the response and the BI link are returned to the frontend for display.

---

## 📚 License and Research Context

This software is part of an academic research project funded by **FAPESP** and is intended **for research and educational purposes only**.
All rights reserved to the project team and affiliated institutions.
