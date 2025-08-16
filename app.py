from flask import Flask
import threading, time

app = Flask(__name__)

# Job nền
def background_job():
    while True:
        print("Đang chạy job và đẩy dữ liệu...")
        # Ví dụ: push dữ liệu qua SQL hoặc API
        time.sleep(10)  # chạy mỗi 10 giây

@app.route("/")
def home():
    return "App đang chạy nền trên Render (Free Plan)!"

if __name__ == "__main__":
    # Chạy job nền song song với Flask server
    threading.Thread(target=background_job, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
