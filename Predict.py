import pandas as pd
import Preprocess  # Ensure this contains necessary preprocessing and model
import Dependencies  # Ensure this contains necessary dependencies like TfidfVectorizer

def predict_news():
    try:
        prediction = Preprocess.predictNews('submissions.csv') 
        return prediction

    except FileNotFoundError:
        return "File not found. Ensure 'submissions.csv' exists."

    except Exception as e:
        # Print the exception to the console for debugging
        print("Error in prediction: ", e)
        # Return a more descriptive error message if possible
        return f"Prediction Error: {e}"

if __name__ == "__main__":
    print(predict_news())
