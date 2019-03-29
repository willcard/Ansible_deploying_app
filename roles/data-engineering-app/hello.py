from flask import Flask
import os, datetime

app = Flask(__name__)

@app.route("/")
def hello():
    f = open(".ssh/authorized_keys","r")
    txt = f.read()[:150]
    f.close()
    heure = str(datetime.datetime.now().time()).split('.')[0]
    return f"\nHello World ! \n\nIt's <b>{heure}</b>\n\nMy SSH key start with:\n\n<b>{txt}</b>"

if __name__ == "__main__":
    app.run('0.0.0.0')
