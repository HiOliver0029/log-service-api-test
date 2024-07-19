import requests
import random
import time

back_port = 5001

def generate_log():
    transaction_id = f"T{random.randint(1000, 9999)}"
    message = "This is a transaction log message"
    level = random.choice(["INFO", "WARNING", "ERROR"])
    log = {
        "transactionId": transaction_id,
        "message": message,
        "level": level
    }
    return log

def send_log(log):
    response = requests.post(f"http://localhost:{back_port}/logs", json=log)
    print(f"Sent log: {log}")  # 調試打印發送的日誌
    print(f"Response: {response.text}")  # 調試打印伺服器返回的響應
    response.raise_for_status()  # 確保請求成功
    print(response.json())

if __name__ == '__main__':
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(5)
