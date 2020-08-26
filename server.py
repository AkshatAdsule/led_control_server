from flask import Flask
from flask import request
app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/setcolor/rgb', methods=["POST"])
def setColor():
	r = request.args.get("R")
	g = request.args.get("B")
	b = request.args.get("G")
	return(str([r,g,b]))