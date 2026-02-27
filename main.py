from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # هذا السطر هو اللي بيعطيك نسبة عشوائية في كل مرة
    score = random.randint(75, 98) 
    return f"تم التحليل بنجاح! النتيجة هي: {score}%"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
