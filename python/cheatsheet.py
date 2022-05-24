# #1
# cd to folder, then run 
# pipenv install flask 

# #2
# run pipenv shell

# #3
# cd to folder within the virual envrionment, then run
# python3 server.py

# #4
# project set up: server.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    #please change port as needed, default port of 5000 does not work on MacOS

#for making a 404 route
@app.errorhandler(404)
def invalid_url(e):
    return "Woops, that page does not exist!"
    #return render_template('404.html')

# <!-- linking a css style sheet -->
# <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style.css') }}">
# <!-- linking a javascript file -->
# <script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
# <!-- linking an image -->
# <img src="{{ url_for('static', filename='img/my_img.png') }}">
