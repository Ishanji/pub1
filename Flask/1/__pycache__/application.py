#PS D:\Playground\python\haw\pub1\Flask\1> $env:FLASK_APP = "application.py"
#PS D:\Playground\python\haw\pub1\Flask\1> $env:FLASK_ENV = "development"   
#flask run

#flask 
from flask import Flask
app = Flask(__name__) 

@app.route("/")
def index():
    return "Hello, world"
