from flask import Flask, request, render_template
import webcolors

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def hello_world():
	return render_template("index.html")


@app.route('/changecolor', methods=["POST", "GET"])
def setColor():
	print(request.args.get("color"))
	rgb = webcolors.hex_to_rgb(request.args.get("color"))
	print("Red:", rgb[0])
	print("Green:", rgb[1])
	print("Blue:", rgb[2])
	return render_template("index.html")