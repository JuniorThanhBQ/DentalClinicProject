from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Dental Clinic App cua Sinh vien dai hoc Mo TP.HCM")

if __name__=="__main__":
    app.run(debug=True)