from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/playground', methods=['GET', 'POST'])
def playground():
    params = {"address": request.args.get('address'), "color": request.args.get('color'), "bright": request.args.get('bright'), "cold": request.args.get('cold'), "warmth": request.args.get('warmth')}
    return render_template('playground.html', title='Playground')


@app.route('/streaming', methods=['GET', 'POST'])
def streaming():
    return render_template('streaming.html', title='Streaming')


if __name__ == '__main__':
    app.run(debug=True)