from quart import Quart, g, request
from quart.helpers import make_response
from quart import render_template
from bulbInterface import lightbulb
import asyncio
import nest_asyncio
nest_asyncio.apply()


app = Quart(__name__, template_folder='templates', static_folder='static')
@app.route('/', methods=['GET', 'POST'])
@app.route('/playground', methods=['GET', 'POST'])
async def playground():
    light1 = lightbulb("192.168.137.105",(255,0,0),0)
    light1.turnOn()
    return await render_template('playground.html', title='Playground')
    
@app.route('/stream', methods=['GET', 'POST'])
async def setup():
    values = {"x1": request.args.get('x1'), "y1": request.args.get('y1'), "x2": request.args.get('x2'), "y2": request.args.get('y2')}

    return await render_template('stream.html', title='Stream')

if __name__ == '__main__':
    app.run(debug=True)
    loop = asyncio.get_event_loop()
