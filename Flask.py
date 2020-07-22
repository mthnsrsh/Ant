from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"







#ERROR-( from flask import Flask ModuleNotFoundError: No module named 'flask'
    )