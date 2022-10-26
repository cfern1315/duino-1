from flask import Flask
import os

app = Flask(__main__)
@app.route('/')
def return_root_message():
  return "I'm alive. Surprising right? Anyway ill start duino.py now."

if __name__ == '__main__':
  app.run(port=3000)
  os.system("duino.py")
