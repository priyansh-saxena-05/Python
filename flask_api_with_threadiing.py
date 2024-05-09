from flask import Flask
from threading import Thread
import time
import os

app = Flask(__name__)

def create_file():
    print("Creating file...")
    time.sleep(5) # Simulate a long running task
    previous_data = ""
    if os.path.exists("hello.txt"):
        with open("hello.txt", "r") as f:
            previous_data = f.read()
    with open("hello.txt", "w") as f:
        f.write(previous_data + "Hello, World!\n")
    print("File created.")

@app.route('/hello')
def hello():
    # Create a new thread to handle file creation
    file_thread = Thread(target=create_file)
    file_thread.start()
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
