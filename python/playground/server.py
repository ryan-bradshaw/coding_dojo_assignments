from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/play/3')

@app.route('/play/<int:num>')
def boxes(num):
    return render_template('index.html', num = num, color="cyan")

@app.route('/play/<int:num>/<string:color>')
def color_and_boxes(num, color):
    return render_template('index.html', num = num, color = color)

@app.errorhandler(404)
def invalid_url(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug = True, port = 8080)