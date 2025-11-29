from flask import Flask, render_template,request, url_for
from markupsafe import escape #Ép buộc định dạng chuỗi để tránh hackers
app = Flask(__name__)
@app.route("/")
def index():
    name = request.args.get("name", "Van Trung Thanh va Nguyen Thanh Phong")
    return render_template("index.html", name=escape(name))

with app.test_request_context():
    print("Liet ke danh sach dia chi router cua web: ")
    print(url_for('index'))

if __name__ =='__main__': #App ket thuc tai day
    app.run(debug=True)
