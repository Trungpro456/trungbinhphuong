import requests, datetime, time, random, pytz

API_KEY = "$2a$10$ww0CuGrDvR5WOSkIhQRmceM4an9Z3BDQp/xoBE7iJDbPXbKt3m49G" 
BIN_ID = "689fe65c43b1c97be91f6b1d"
URL = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
headers = {"X-Master-Key": API_KEY}

# Giờ Việt Nam
tz_vn = pytz.timezone("Asia/Ho_Chi_Minh")

while True:
    try:
        now = datetime.datetime.now(tz_vn)   # luôn giờ VN

        data = {
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(40, 80), 2)
        }

        res = requests.put(URL, json=data, headers=headers)
        print("Status:", res.status_code, "->", res.text)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
