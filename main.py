import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)