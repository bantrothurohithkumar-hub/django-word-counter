# 📝 Django Word Counter

A simple and responsive Django web application that allows users to enter text in a text box on the home page and immediately displays the total number of words upon submission.

---

## 🛠️ Features
* Clean, user-friendly home page with a text input box.
* Fast server-side word processing and counting logic.
* Built using Django's Model-View-Template (MVT) architecture.

## 💻 Tech Stack
* **Backend:** Python, Django
* **Frontend:** HTML, CSS

---

## 🚀 How to Setup and Run This Project Locally

Follow these continuous steps in your terminal to get the project running:

```bash
# Step 1: Clone the Repository and enter the folder
git clone https://github.com/bantrothurohithkumar-hub/django-word-counter.git
cd django-word-counter

# Step 2: Create and Activate the Virtual Environment (Windows)
python -m venv myproject
myproject\Scripts\activate
#Create and Activate the Virtual Environment(Mac/Linux)
 python 3 venv myproject
 source myproject/bin/activate

# Step 3: Install Required Packages
pip install -r requirements.txt

# Step 4: Run Database Migrations
python manage.py migrate

# Step 5: Start the Development Server
python manage.py runserver