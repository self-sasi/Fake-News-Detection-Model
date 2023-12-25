#### Fake News Detection Model

## About Files in the Repository

### `Dependencies.py`
- Contains all the necessary imports for the project.

### `Preprocess.py`
- Handles preprocessing of data including:
  - Data munging
  - Removal of stopwords
  - Stemming of text to its base form
  - Factorizing using TfidfVectorizer
  - Splitting data into 80:20 ratio for training and testing
  - Fitting the training data into a logistic regression model from scikit-learn

### `Evaluate.py`
- Runs the model and tests its accuracy over training and testing data.

### `Predict.py`
- Uses the trained model to make predictions.
- Contains the `predict_news()` function responsible for making predictions.

### `app.py`
- Contains the code for the frontend, utilizing Flask to create a user interface.
- Calls `Predict.predict_news()` to make predictions and display output.
- Contains a string variable `HTML_TEMPLATE` for the structure of the web page.

### `structure.html`
- Contains HTML and CSS code for the `HTML_TEMPLATE` in `app.py`.
- Serves no direct functionality; created for testing the web page's appearance.

### `train.csv`
- Contains over 20,000 entries used for training and testing the model.

### `test.csv`
- Sample file with multiple entries of news for testing purposes, not used in training.

### `LICENSE`
- The project is licensed under the MIT License. This license permits reuse, distribution, modification, private use, and licensing, provided that the original authorship is credited and the license notice and warranty disclaimer are preserved with the distribution.

## How to Run the Model on Your Local Computer

### 1) Cloning the Repository:

The initial step involves cloning the repository into a local directory on your machine. To accomplish this, execute the following command in your command prompt or Git Bash:

```bash
pip install numpy pandas nltk scikit-learn
```

### 2) Installing Necessary Tools:

Ensure that Python is installed on your system. Then install the following libraries using the terminal or command prompt:

```bash
git clone https://github.com/your-username/repository-name.git
```

After installing the main packages, you may need to download specific resources from NLTK:

```python
import nltk
nltk.download('stopwords')
```

### 3) Ensuring File Organization:

Make sure every single file is saved in the same directory to avoid file-not-found errors.

### 4) Running the Application:

Execute the `app.py` file by running the following command in your terminal:

```bash
python app.py
```

This should open a web page in your preferred browser. Once loaded, you can directly use the tool for prediction.

### Note:

The running of `app.py` can take time as a huge dataset is used for training. Once the model is formed and displayed completely on the webpage, it should be quick in processing.

## Contributions

Feel free to fork the project, submit issues and pull requests to enhance the functionalities or fix problems.

---
