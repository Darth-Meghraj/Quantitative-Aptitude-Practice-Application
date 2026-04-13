# 🚀 Quantitative Aptitude Quiz App (Tkinter)

A desktop-based **Quantitative Aptitude Quiz Application** built using **Python and Tkinter**, designed to simulate a real exam environment with timer, difficulty levels, and detailed performance review.

## 📌 Features

* 🎯 **Multiple Difficulty Levels**

  * Easy → 5 questions (60 sec)
  * Medium → 10 questions (60 sec)
  * Hard → 20 questions (80 sec)

* ⏱️ **Real-Time Timer**

  * Countdown timer updates every second
  * Automatically submits quiz when time ends

* 📊 **Progress Tracking**

  * Dynamic progress bar
  * Question counter (e.g., 3/10)

* 🔁 **Navigation System**

  * Next and Previous buttons
  * Answers are saved automatically

* ✅ **Answer Selection**

  * Single-choice MCQs using radio buttons
  * Uses `StringVar()` for real-time tracking

* 📄 **Detailed Review Section**

  * Displays:

    * Your answer
    * Correct answer
    * Explanation
    * ✅ Correct / ❌ Wrong indicator

* 🔄 **Restart Quiz**

  * Restart the quiz from result screen

* 🎨 **User Interface**

  * Background image support
  * Centered and responsive layout
  * Clean white overlay for readability

---

## 🧠 Concepts Used

* Python Tkinter (GUI development)
* Event-driven programming
* File handling (reading `.txt`)
* Dictionaries for storing answers
* List comprehension & generator expressions
* Dynamic UI updates using `.config()`
* Timer using `after()`
* Scrollable UI using Canvas + Scrollbar



## 📁 File Explanations

### 🔹 1. `quiz_app.py`

This is the **main file** that runs the application.

It contains:

* GUI setup using Tkinter
* Quiz logic (question loading, navigation, scoring)
* Timer implementation using `after()`
* Answer storage using dictionary
* Scrollable review section using Canvas + Scrollbar

### 🔹 2. `questions.txt`

This file contains all quiz questions in a structured format.

#### 📌 Format Example:

```
Question: What is 2 + 2?
A: 3
B: 4
C: 5
D: 6
Answer: B
Explanation: 2 + 2 = 4
---
```

#### 🔥 Important Rules:

* Each question block ends with `---`
* Must include:

  * Question
  * 4 options (A–D)
  * Answer
  * Explanation

👉 The app reads and converts this into dictionaries.

---

### 🔹 3. `bg.jpg`

This is the **background image** used in the app.

* Displayed on the start screen
* Enhances UI appearance
* Stretches to full screen using PIL

---

## ▶️ How to Run the Project

### 1️⃣ Install required library

```bash
pip install pillow
```

---

### 2️⃣ Run the application

```bash
python quiz_app.py
```

---

## ⚙️ How It Works (Flow)

1. App starts → background + start screen
2. User selects difficulty
3. Questions are randomly selected
4. Timer starts
5. User answers questions
6. Score is calculated
7. Review screen shows detailed results

---

## 📈 Future Improvements

* Add login system
* Store score history
* Add topic-wise filtering
* Convert to web app (Flask / React)
* Add AI-based question generation

---

## 💡 Learning Outcomes

* Learned GUI development using Tkinter
* Implemented real-time timer
* Managed user input and state
* Built a complete end-to-end application
* Designed scrollable interfaces

---

## 👨‍💻 Author

**Meghraj Bhar**
BCA Student | Aspiring Machine Learning Engineer

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
