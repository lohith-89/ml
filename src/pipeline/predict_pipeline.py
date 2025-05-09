import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Define the paths for the model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading Model and Preprocessor")
            
            # Load the model and preprocessor from disk
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            print("After Loading Model and Preprocessor")
            
            # Transform the input features using the preprocessor
            data_scaled = preprocessor.transform(features)
            print("Data after Scaling:")
            print(data_scaled)

            # Make predictions using the trained model
            preds = model.predict(data_scaled)
            print("Predictions:", preds)

            return preds

        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            # Create a dictionary from the input data
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }

            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(custom_data_input_dict)

            print("Custom Data DataFrame:")
            print(df)

            return df

        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)
