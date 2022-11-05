from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    params = {"address": request.args.get('address'), "color": request.args.get('color'), "bright": request.args.get('bright'), "cold": request.args.get('cold'), "warmth": request.args.get('warmth')}
    return render_template('settings.html', title='Settings')


if __name__ == '__main__':
    app.run(debug=True)