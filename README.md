🎯 Student Exam Performance Predictor
A Flask-based machine learning web application that predicts student math scores using demographic features and reading/writing test scores. This project demonstrates end-to-end ML model deployment with user input handling, data transformation, prediction logic, and result display.

🔗 GitHub Repo: lohith-89/ml

🛠️ Tools & Technologies Used
Python 3.8+

Flask – Web framework

scikit-learn – Model training & preprocessing

pandas, numpy – Data manipulation

HTML/CSS – Web frontend

joblib – Model serialization

Modular Project Structure

🚀 Features
User submits a form with student data:

Gender, Ethnicity, Parental Education, Lunch, Test Prep

Reading & Writing Scores

The backend:

Loads a pre-trained model and preprocessor

Transforms input using the saved pipeline

Predicts the student’s Math score

Displays the predicted result on the same page


🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/lohith-89/ml.git
cd ml
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
3. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
4. Ensure Artifacts Are in Place
Make sure the following files exist in the artifacts/ directory:

model.pkl – Trained regression model

preprocessor.pkl – Fitted data transformer (like a pipeline)

These are generated during the training phase. If not present, retrain and dump the files accordingly.

5. Run the Application
bash
Copy
Edit
python application.py
Open your browser and navigate to http://127.0.0.1:5000/ to access the app.

📊 Inputs Expected
Field	Type	Example
Gender	String	male
Race/Ethnicity	String	group B
Parental Level of Education	String	bachelor's degree
Lunch	String	standard
Test Preparation Course	String	completed
Reading Score	Integer	76
Writing Score	Integer	70

📌 Result
The predicted Math Score will be shown below the form upon submission.

📈 Future Improvements
Add model training pipeline (train_pipeline.py) for full automation

Add logging and error handling for production

Integrate with a database to store predictions

Dockerize for container-based deployment

🤝 Contributing
Feel free to fork the repo and submit pull requests. Feedback and suggestions are always welcome!

📄 License
This project is open-source and available under the MIT License.