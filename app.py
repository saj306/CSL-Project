#Import necessary libraries
import threading

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/activate', methods=['GET'])
def activate():
    if 'cam1' in request.args:
        f = open("activation.txt","r")
        if f.read() == "active":
            f.close()
            f = open("activation.txt","w")
            f.write("not active")
            f.close()
        else:
            f.close()
            f = open("activation.txt","w")
            f.write("active")
            f.close()

    # else:
    #     print("cam2 activated")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
