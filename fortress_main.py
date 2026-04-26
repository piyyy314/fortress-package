import time
from alerts import send_alert

def main():
    send_alert("Fortress Command started.")
    try:
        while True:
            send_alert("Fortress heartbeat...")
            time.sleep(5)
    except KeyboardInterrupt:
        send_alert("Fortress Command stopped by user.")

if __name__ == "__main__":
    main()