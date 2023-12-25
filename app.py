from flask import Flask, request, render_template_string, redirect, url_for
import csv
import os
import webbrowser
from threading import Timer
import Predict  # Ensure this is the Predict module you've created

app = Flask(__name__)

# Define your HTML template with Jinja2 placeholders for prediction
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Input</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #000;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: left;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: #333;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            padding: 30px;
            width: 400px;
            box-sizing: border-box;
            margin-left: 15%;
        }

        h1 {
            text-align: center;
            color: #4CAF50;
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-size: 14px;
            color: #ddd;
        }

        input, textarea {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            box-sizing: border-box;
            border: 1px solid #666;
            border-radius: 6px;
            font-size: 16px;
            background-color: #444;
            color: #fff;
        }

        button {
            padding: 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 18px;
            border-radius: 6px;
        }

        button:hover {
            background-color: #45a049;
        }
        #prediction_result {
            color: #F0DB4F; /* a yellow color; change as you prefer */
            margin-top: 20px;
            text-align: center;
            margin-left: 15%;
        }
        .true {
            color: green;
            font-size: 22px;
        }

        .false {
            color: red;
            font-size: 22px
        }

    </style>
</head>
<body>
    <form action="/submit" method="post">
        <h1>Fake News Detection Model</h1>

        <label for="headline">News Headline:</label>
        <input type="text" id="headline" name="headline" required>

        <label for="author">News Author:</label>
        <input type="text" id="author" name="author" required>

        <label for="content">News Content:</label>
        <textarea id="content" name="content" rows="6" required></textarea>

        <button type="submit">Submit</button>
    </form>

    <!-- Section to display prediction result -->
    {% if prediction %}
            <div id="prediction_result">
                {% if prediction == '1' %}
                    <p class="true">The news is likely to be true</p>
                {% else %}
                    <p class="false">The news is likely to be false</p>
                {% endif %}
            </div>
        {% endif %}
</body>
</html>
"""

@app.route('/')
def form():
    prediction_result = request.args.get('prediction', '')
    return render_template_string(HTML_TEMPLATE, prediction=prediction_result)

@app.route('/submit', methods=['POST'])
def submit():
    headline = request.form['headline']
    author = request.form['author']
    content = request.form['content']

    # Save the data to submissions.csv
    with open('submissions.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['serial number', 'Title', 'Author', 'Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'serial number': 1,
            'Title': headline,
            'Author': author,
            'Text': content
        })

    # Predict the nature of the news using Predict.py
    prediction_result = Predict.predict_news()

    # Redirect back to the home page and display the result
    return redirect(url_for('form', prediction=prediction_result))

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)