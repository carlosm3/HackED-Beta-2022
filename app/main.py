from flask import Flask, render_template, request
# import avgRGBv2
# from bulbInterface import lightbulb as lb

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/playground', methods=['GET', 'POST'])
def playground():
    values = {"color": request.args.get('color'), "bright": request.args.get('bright'), "cold": request.args.get('cold'), "warmth": request.args.get('warmth')}
    print(values)
    # rgb = avgRGBv2.convertHEXtoRGB(values['color'])
    # lb.changeRGB(rgb)
    # lb.changeBright(values['bright']*255)
    # lb.changeCold(values['cold'])
    # lb.changeBright(values['bright'])
    return render_template('playground.html', title='Playground')


@app.route('/streaming', methods=['GET', 'POST'])
def streaming():
    return render_template('streaming.html', title='Streaming')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    values = {"ip": request.args.get('address'), "x1": request.args.get('x1'), "y1": request.args.get('y1'), "x2": request.args.get('x2'), "y2": request.args.get('y2')}
    print(values)
    return render_template('setup.html', title='Setup')


if __name__ == '__main__':
    app.run(debug=True)