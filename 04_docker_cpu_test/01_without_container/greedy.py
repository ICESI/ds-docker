import threading
from flask import Flask
app = Flask(__name__)

def greedy():
    x = 2
    while(True):
        x = x*3

@app.route("/hi")
def hi():
    return "Hi!, I am a greedy algorithm"

@app.route("/greedy")
def test():
    t1=threading.Thread(target=greedy,args=[])
    t1.start()
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug='True')
