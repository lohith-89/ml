

```markdown
# 🎯 Student Exam Performance Predictor

A Flask-based machine learning application that predicts student math scores based on user input including demographic data and test scores. This project is hosted on: [lohith-89/ml](https://github.com/lohith-89/ml)

---



---

## 🚀 Features

- User inputs student attributes via a web form
- Pre-trained regression model predicts math scores
- Flask backend + HTML frontend
- Modular Python code for scalability

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/lohith-89/ml.git
cd ml
````

### 2. Create Virtual Environment & Install Requirements

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

### 3. Run the Application

```bash
python application.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧠 Input Parameters

| Field                       | Type     | Description             |
| --------------------------- | -------- | ----------------------- |
| Gender                      | Dropdown | Male / Female           |
| Race or Ethnicity           | Dropdown | Group A–E               |
| Parental Level of Education | Dropdown | Various degrees         |
| Lunch                       | Dropdown | Standard / Free-reduced |
| Test Preparation Course     | Dropdown | None / Completed        |
| Writing Score               | Number   | 0–100                   |
| Reading Score               | Number   | 0–100                   |



## 📌 .gitignore

Make sure to include:

```gitignore
venv/
__pycache__/
*.pyc
*.pkl
artifacts/
.env
```

---

## 📈 Future Improvements

* [ ] Add training pipeline script
* [ ] Add Dockerfile for containerization
* [ ] Integrate model retraining with CI/CD
* [ ] UI improvements (charts, validations)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Maintainer

Made by [Lohith](https://github.com/lohith-89) — feel free to fork, suggest improvements, or raise issues.

```



