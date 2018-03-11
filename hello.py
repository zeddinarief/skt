#import library flask
from flask import Flask, request

#inisiasi app flask sebagai server
app = Flask("Hello App")

@app.route('/', methods=['GET'])
def handle_get():
	return "Hello World"

#jalankan server Flask
app.run(port=7777)
