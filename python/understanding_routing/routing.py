from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/greet/<name>')
def greet_by_name(name):
    return "Hello, " + name

@app.route('/repeat/<string:word>/<int:num>')
def repeat_url_word(word, num):
    output = ''
    for i in range (0, num):
        output += f"<p> {word} </p>"
    return output

@app.errorhandler(404)
def invalid_url(e):
    return "Woops, that page does not exist!"

if __name__ == "__main__":
    app.run(debug=True, port=8080)