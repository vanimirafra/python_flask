from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route("/home")

def home():
    return "hello world"
@app.route("/about")
def about():
    return "hi"



if __name__ == '__main__':
    app.run(debug=True)
