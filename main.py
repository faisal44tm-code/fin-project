from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # عرض الصفحة الرئيسية
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check_similarity():
    # هنا تضع منطق فحص التشابه مستقبلاً
    # حالياً سنرسل نتيجة تجريبية كما في صورتك
    result_text = "شبه مشابه"
    return render_template('index.html', result=result_text)


if __name__ == "__main__":
    # تشغيل السيرفر على منفذ 8080 المتوافق مع Replit
    app.run(host='0.0.0.0', port=8080, debug=True)
