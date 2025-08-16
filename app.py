import requests, datetime, time, random, threading
from flask import Flask

app = Flask(__name__)

API_KEY = "$2a$10$ww0CuGrDvR5WOSkIhQRmceM4an9Z3BDQp/xoBE7iJDbPXbKt3m49G"
BIN_ID = "689fe65c43b1c97be91f6b1d"   # BIN mutable
URL = f"https://api.jsonbin.io/v3/b/{BIN_ID}"

headers = {
    "Content-Type": "application/json",
    "X-Master-Key": API_KEY
}

# job chạy nền
def background_job():
    while True:
        now = datetime.datetime.now()
        data = {
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(40, 80), 2)
        }

        try:
            res = requests.put(URL, json=data, headers=headers)
            print("Status:", res.status_code)
            print("Response:", res.text)
        except Exception as e:
            print("Error:", e)

        time.sleep(5)  # mỗi 5 giây gửi 1 lần

@app.route("/")
def home():
    return "Background job is running and pushing data to JSONBin!"

if __name__ == "__main__":
    threading.Thread(target=background_job, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
