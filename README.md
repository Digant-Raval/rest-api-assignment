# REST API Assignment

This program demonstrates how to interact with a RESTful API using Python.  
It allows you to submit your student information (via **POST**) and retrieve it back (via **GET**).  

---

## 📌 Features
- Collects student information from the user (UCID, name, GitHub, Discord, favorites, etc.)
- Submits the information to the given API endpoint using a **POST** request
- Retrieves saved records using a **GET** request
- Handles errors such as:
  - Missing required fields
  - Server connection issues
  - Invalid responses

---

## 🛠 Requirements
- Python 3 (check with `python --version`)
- [requests](https://pypi.org/project/requests/) library

📡 API Endpoint
https://student-info-api.netlify.app/.netlify/functions/submit_student_info
