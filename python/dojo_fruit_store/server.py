from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    return redirect("/order")

@app.route('/order')
def order_summary():
    print(request.form)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True, port = 8080)