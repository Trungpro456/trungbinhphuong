import requests, datetime, time, random, psycopg2

# Thông tin kết nối DB Aiven hoặc Supabase
DB_HOST = "your-db-host"
DB_NAME = "your-db-name"
DB_USER = "your-db-user"
DB_PASS = "your-db-pass"
DB_PORT = "5432"

def insert_data(temp, humi):
    conn = psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sensor_data (date, time, temperature, humidity) VALUES (%s, %s, %s, %s)",
        (
            datetime.datetime.now().strftime("%Y-%m-%d"),
            datetime.datetime.now().strftime("%H:%M:%S"),
            temp,
            humi,
        ),
    )
    conn.commit()
    cur.close()
    conn.close()

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)
    insert_data(temperature, humidity)
    print(f"Inserted: {temperature}°C, {humidity}%")
    time.sleep(10)
