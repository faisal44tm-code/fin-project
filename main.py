from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    # صفحة الإدخال (الخانات)
    return '''
    <div style="text-align:center; padding-top:50px; font-family:Arial; direction:rtl;">
        <h1 style="color:#2c3e50;">نظام كشف التشابه الذكي</h1>
        <p>أدخل الأسماء أو البيانات للمقارنة:</p>
        <form action="/result" method="post">
            <input type="text" name="name1" placeholder="الاسم الأول" required style="padding:10px; margin:5px; width:200px;"><br>
            <input type="text" name="name2" placeholder="الاسم الثاني" required style="padding:10px; margin:5px; width:200px;"><br>
            <button type="submit" style="padding:10px 20px; background:#3498db; color:white; border:none; cursor:pointer; border-radius:5px;">تحليل نسبة التشابه</button>
        </form>
    </div>
    '''

@app.route('/result', methods=['POST'])
def result():
    n1 = request.form.get('name1')
    n2 = request.form.get('name2')
    score = random.randint(75, 99)
    # النتيجة بنفس شكل "كشف التشابه" اللي تحبه
    return f'''
    <div style="text-align:center; padding-top:100px; font-family:Arial;">
        <h1 style="font-size:35px; color:#34495e;">{n1} & {n2}</h1>
        <h2 style="font-size:60px; font-weight:bold;">Result: {score}%</h2>
        <p style="font-size:20px; color:green;">الحالة: تشابه مرتفع جداً</p>
        <br>
        <a href="/" style="text-decoration:none; color:#3498db;">إجراء فحص آخر</a>
    </div>
    '''

if __name__ == "__main__":
    app.run()
