````markdown
# 🎯 Student Exam Performance Predictor

A Flask-based machine learning web application that predicts student math scores using demographic features and test scores. This project demonstrates end-to-end ML deployment, user input handling, data transformation, and prediction logic.

🔗 **GitHub Repo:** [lohith-89/ml](https://github.com/lohith-89/ml)

---

## 🛠️ Tools & Technologies Used

- **Python 3.8+**
- **Flask** – Web framework
- **scikit-learn** – Model training & preprocessing
- **pandas**, **numpy** – Data manipulation
- **joblib** – Model serialization
- **HTML/CSS** – Web frontend
- **Modular Python Project Structure**

---

## 🚀 Features

- User inputs student info via a web form:
  - Gender, Ethnicity, Parental Education
  - Lunch type, Test prep course
  - Reading and Writing Scores
- Flask backend:
  - Loads pre-trained model and transformer
  - Preprocesses input data
  - Predicts math score
- Displays prediction on the same page

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/lohith-89/ml.git
cd ml
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Ensure Artifacts Exist

Ensure the following files are in the `artifacts/` folder:

* `model.pkl` – Trained ML model (regressor)
* `preprocessor.pkl` – Transformer object (e.g., OneHotEncoder + Scaler)

> If you don't have these, retrain your model pipeline and save them accordingly.

### 5. Run the Flask App

```bash
python application.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the web app.

---

## 📊 Input Fields

| Field                    | Type    | Example             |
| ------------------------ | ------- | ------------------- |
| Gender                   | String  | `male`              |
| Race/Ethnicity           | String  | `group B`           |
| Parental Education Level | String  | `bachelor's degree` |
| Lunch                    | String  | `standard`          |
| Test Prep Course         | String  | `completed`         |
| Reading Score            | Integer | `76`                |
| Writing Score            | Integer | `70`                |

---

## ✅ Output

After form submission, the app displays the **predicted Math Score** (out of 100) based on the input data.



### 📷 Web Form Example
![Student Info Form](images\Screenshot 2025-05-11 182330.png)

### 📷  Form Inputs
![Form Inputs](images\Screenshot 2025-05-11 182521.png)

### 📷 Sample Inputs
![Sample Inputs](images\Screenshot 2025-05-11 182735.png)

### 📷 Prediction Result Example
![Predicted Math Score Output](images\Screenshot 2025-05-11 182758.png)


---

## 📈 Future Improvements

* Add model training pipeline with version control
* Implement error logging and better exception handling
* Add Dockerfile for containerization
* Connect with a database to store predictions
* Deploy on cloud (Heroku, AWS, or Render)

---

## 📄 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, fork the repo, and submit pull requests.

```