# Django Word Counter

A simple and responsive Django web application that allows users to input text into a form and immediately see the total word count upon submission. 

---

## 🚀 Features
* Clean, user-friendly interface.
* Instant server-side word processing.
* Built using Django's Model-View-Template (MVT) architecture.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Django 5.x
* **Frontend:** HTML5, CSS3

----

## 💻 How to Setup and Run Locally

Follow these steps to get the project running on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/django-word-counter.git
cd django-word-counter
### 2.Create and Activate a Virtual Environment
 * **For Windows:**
   ```bash 
       python -m venv myproject 
       myproject\Scripts\activate
 * **For Mac/Linux:**
  ```bash
       python3 -m venv myproject
       source myproject/bin/activate
### 3.Install Requirement Packages
  pip install -r requirements.txt
### 4.Run Database Migration
 python manage.py migrate
### 5.Start the Development Server
   python manage.py runserver
Once the server is running,open web browser and go to http://127.0.0.1:8000/