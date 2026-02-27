from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>نظام تحليل البيانات</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding-top: 50px; }
            .container { background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
            input { padding: 10px; width: 80%; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; text-align: center; }
            button { padding: 10px 25px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>نظام تحليل البيانات الذكي</h1>
            <p>أدخل البيانات المطلوبة للتحليل:</p>
            <form action="/analyze" method="post">
                <input type="text" name="name" placeholder="اسم الحالة أو المشروع" required><br>
                <input type="text" name="data" placeholder="أدخل البيانات الرقمية" required><br>
                <button type="submit">بدء التحليل</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/analyze", methods=["POST"])
def analyze():
    user_name = request.form.get("name")
    score = random.randint(75, 99)

    return f"""
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>النتيجة</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding-top: 100px; }}
            .result-box {{ background: white; padding: 40px; border-radius: 15px; display: inline-block; box-shadow: 0px 4px 15px rgba(0,0,0,0.2); border-top: 5px solid #28a745; }}
            .percentage {{ font-size: 60px; color: #28a745; font-weight: bold; margin: 20px 0; }}
            a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="result-box">
            <h2>تحليل الحالة: {user_name}</h2>
            <div class="percentage">{score}%</div>
            <p>تم التحليل بنجاح.</p>
            <br>
            <a href="/">تحليل جديد</a>
        </div>
    </body>
    </html>
    """

# هذا السطر فقط للتشغيل المحلي
if__ name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
