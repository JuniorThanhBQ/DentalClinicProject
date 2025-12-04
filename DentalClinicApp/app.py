from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

@app.route('/about')
def about():
    return "About page"

# Lưu ý quan trọng:
# Không dùng app.run() ở đây vì Vercel sẽ tự quản lý việc chạy app.
# Nếu bạn cần test local, hãy dùng khối if __name__ == '__main__':
if __name__ == '__main__':
    app.run(debug=True)