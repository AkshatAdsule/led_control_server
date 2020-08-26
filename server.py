from flask import Flask, request, render_template
import webcolors
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

R = GPIO.PWM(12, 255)
G = GPIO.PWM(13, 255)
B = GPIO.PWM(18, 255)

def setColor(r,g,b):
		R.ChangeDutyCycle(int(r/2.55))
		G.ChangeDutyCycle(int(g/2.55))
		B.ChangeDutyCycle(int(b/2.55))
		print("R PWN:", int(r/2.55))
		print("B PWN:", int(g/2.55))
		print("B PWN:", int(b/2.55))

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
	return render_template("index.html")


@app.route('/changecolor', methods=["POST", "GET"])
def changeColor():
	print(request.args.get("color"))
	rgb = webcolors.hex_to_rgb(request.args.get("color"))
	print("Red:", rgb[0])
	print("Green:", rgb[1])
	print("Blue:", rgb[2])
	setColor(rgb[0], rgb[1], rgb[2])
	return render_template("index.html")