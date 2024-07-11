# API Documentation

## Software Overview

This project is made for a PyQt application that fetches and displays random facts from a Flask API.

## PyQt Application

### Setup

To set up the PyQt application, ensure you have Python and PyQt5 installed. You can install PyQt5 using pip:

```bash
pip install PyQt5 requests
```

### Usage

Run the PyQt application using the following command:

```bash
python pyqt_app.py
```


The application will display a window with a label that updates with random facts every 5 seconds.

## Flask API

### Setup

To set up the Flask API, ensure you have Python and Flask installed. You can install Flask using pip:

```bash
pip install Flask gunicorn
```

### Running Locally

Run the Flask application using the following command:

```bash
python backend.py
```

The Flask API will be available at http://127.0.0.1:5000.

### Deploying to Render

To deploy the Flask API to Render, follow these steps:

- Push your code to a GitHub repository.
- Create a new Web Service on Render and connect your GitHub repository.
- Render will automatically detect your Flask app and deploy it.
- The API will be available at https://your-app-name.onrender.com.

## API Endpoint

The API provides the following endpoint:

```bash
GET /random_fact - Returns a random fact in JSON format.
```

Example response:

```json
{
    "fact": "Fact 1"
}
```

## Example PyQt Application Code

```python
import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class FactFetcher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_fact)
        self.timer.start(5000)  # Update every 5 seconds

    def update_fact(self):
        try:
            response = requests.get('https://your-app-name.onrender.com/random_fact')
            if response.status_code == 200:
                fact = response.json().get('fact')
                self.fact_label.setText(fact)
            else:
                self.fact_label.setText('Failed to fetch fact')
        except Exception as e:
            self.fact_label.setText(f'Error: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fetcher = FactFetcher()
    fetcher.show()
    sys.exit(app.exec_())

```

## Example Flask API Code

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

facts = [
    "Fact 1",
    "Fact 2",
    "Fact 3",
    "Fact 4",
    "Fact 5"
]

@app.route('/random_fact', methods=['GET'])
def random_fact():
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run()
```
