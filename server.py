from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def hello_world():
	return render_template("index.html")


@app.route('/setcolor/rgb', methods=["POST"])
def setColor():
	r = request.args.get("R")
	g = request.args.get("B")
	b = request.args.get("G")
	return(str([r,g,b]))