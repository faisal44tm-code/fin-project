from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    # هذا السطر هو اللي بيعطيك نسبة مئوية متغيرة في كل مرة تفتح الصفحة
    score = random.randint(75, 99)
    return f"""
    <html>
        <body style="text-align: center; font-family: Arial; padding-top: 100px;">
            <h1 style="color: #2c3e50;">نظام تحليل فيصل الذكي</h1>
            <div style="font-size: 50px; color: #27ae60; margin: 20px;">
                النتيجة: {score}%
            </div>
            <p>تحديث الصفحة يعطيك نتيجة جديدة</p>
            <button onclick="location.reload()" style="padding: 10px 20px; cursor: pointer;">تحليل جديد</button>
        </body>
    </html>
    """

if name == "__main__":
    app.run(host='0.0.0.0', port=10000)
