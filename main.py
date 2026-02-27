from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    score = random.randint(75, 99)
    return f"<h1>Nezam Faisal Al-Zaki</h1><h2>Result: {score}%</h2><p>Refresh for new result!</p>"

if __name__ == "__main__":
    app.run()
