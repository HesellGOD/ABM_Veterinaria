import os
import webbrowser
import threading

def run_server():
    os.system("python manage.py runserver 127.0.0.1:8000")

if __name__ == "__main__":
    threading.Timer(2, lambda: webbrowser.open("http://127.0.0.1:8000")).start()
    run_server()
