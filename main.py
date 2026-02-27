from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div style="direction: rtl; text-align: center; padding-top: 50px; font-family: Arial;">
        <h1>نظام تحليل فيصل الذكي</h1>
        <form action="/analyze" method="post">
            <input type="text" name="n" placeholder="اسم الحالة" required><br><br>
            <input type="text" name="d" placeholder="أدخل البيانات" required><br><br>
            <button type="submit" style="padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer;">ابدأ التحليل</button>
        </form>
    </div>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form.get('n')
    score = random.randint(75, 99)
    return f'''
    <div style="direction: rtl; text-align: center; padding-top: 100px; font-family: Arial;">
        <h1>نتائج التحليل لـ: {name}</h1>
        <h2 style="color: green; font-size: 50px;">النتيجة: {score}%</h2>
        <br>
        <a href="/" style="color: blue; text-decoration: none;">الرجوع للرئيسية</a>
    </div>
    '''

if __name__ == "__main__":
    app.run()
