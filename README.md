# 🎓 AI-Powered College Helpdesk Chatbot

## 📌 Project Overview

The **AI-Powered College Helpdesk Chatbot** is a machine learning-based application designed to automate responses to frequently asked questions by students. It provides instant, accurate, and consistent answers related to college admissions, fees, hostel facilities, academics, and other general queries.

This project aims to reduce the workload on administrative staff and improve accessibility to information for students by offering a simple and interactive chatbot interface.

---

## 🎯 Problem Statement

In most colleges, students frequently ask similar questions regarding:

* Admission procedures
* Fee structures
* Hostel availability
* Exam schedules
* General college information

Handling these repetitive queries manually is time-consuming and inefficient.

---

## 💡 Proposed Solution

This project implements an AI-based chatbot that:

* Understands user queries using Natural Language Processing (NLP)
* Matches them with the most relevant stored question
* Provides an accurate response instantly

---

## ⚙️ Features

* 🤖 AI-based chatbot using NLP techniques
* ⚡ Instant responses to user queries
* 📚 Covers multiple domains (admission, hostel, academics, etc.)
* 🧠 Uses TF-IDF and Cosine Similarity for intelligent matching
* 💬 Easy-to-use command-line interface
* 📊 Custom dataset created for real-world scenarios

---

## 🛠️ Technologies Used

* **Python** – Core programming language
* **Pandas** – Data handling
* **Scikit-learn** – Machine Learning (TF-IDF, Cosine Similarity)
* **NLP Techniques** – Text preprocessing and matching

---

## 🧠 Working Principle

1. A dataset of frequently asked questions (FAQs) is created in CSV format
2. Questions are converted into numerical vectors using **TF-IDF Vectorizer**
3. User input is processed and transformed into vector form
4. **Cosine Similarity** is used to find the closest matching question
5. The corresponding answer is returned to the user

---

## 📂 Project Structure

```
college-helpdesk-chatbot/
│── app.py                # Main chatbot application
│── faq.csv               # Dataset of questions and answers
│── requirements.txt      # Required libraries
│── README.md             # Project documentation
```

---

## 📊 Dataset Description

The dataset consists of:

* 30+ frequently asked questions
* Categories include:

  * Admission
  * Fees
  * Hostel
  * Academics
  * Facilities

Example:

```
Question,Answer
What is admission process?,Apply online through college website
What are hostel fees?,₹50000 per year
```

---

## ▶️ How to Run the Project


### Step 1: Clone the repository
git clone https://github.com/avani25bai11450-tech/college-helpdesk-chatbot.git

### Step 2: Navigate to the project folder
cd college-helpdesk-chatbot

### Step 3: Install required libraries
pip install -r requirements.txt

### Step 4: Run the chatbot
python app.py

## 💬 Sample Interaction

```
College Helpdesk Chatbot
You: What is admission process?
Bot: Apply online through college website

You: What are hostel fees?
Bot: ₹50000 per year
```

---

## 🚧 Challenges Faced

* Handling different ways of asking the same question
* Improving chatbot accuracy with limited data
* Managing file paths and GitHub integration
* Understanding Git commands and version control

---

## 📈 Future Enhancements

* 🌐 Web-based interface using Streamlit or Flask
* 🎤 Voice input and speech recognition
* 🌍 Multi-language support (Hindi + English)
* 🤖 Integration with advanced AI models
* 📱 Mobile-friendly chatbot interface
## 📸 Output Screenshot


<img width="1623" height="837" alt="output" src="https://github.com/user-attachments/assets/671e013e-1125-4af0-92a3-9e3b712ef03b" />


## 🎓 Learning Outcomes

* Understanding of Natural Language Processing (NLP)
* Hands-on experience with Machine Learning models
* Knowledge of Git and GitHub version control
* Problem-solving using real-world scenarios
* Building end-to-end AI applications

---

## 👨‍💻 Author

**Avani Khare**

---

## 📌 Conclusion

The AI College Helpdesk Chatbot successfully demonstrates how machine learning can be applied to solve real-world problems. It improves efficiency, reduces manual workload, and enhances user experience by providing quick and accurate responses.

---

⭐ If you found this project useful, feel free to star the repository!
