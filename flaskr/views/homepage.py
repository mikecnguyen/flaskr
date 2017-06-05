
from flaskr import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)