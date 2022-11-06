from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
@app.route('/playground', methods=['GET', 'POST'])
def playground():
    # light1 = lightbulb("192.168.137.105",(request.args.get('r'),request.args.get('g'),request.args.get('b')),request.args.get('bright'),request.args.get('cold'),request.args.get('warmth'))

    return render_template('playground.html', title='Playground')

@app.route('/stream', methods=['GET', 'POST'])
def setup():
    values = {"x1": request.args.get('x1'), "y1": request.args.get('y1'), "x2": request.args.get('x2'), "y2": request.args.get('y2')}

    return render_template('stream.html', title='Stream')


if __name__ == '__main__':
    app.run(debug=True)