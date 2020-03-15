from flask import Flask
from flask import render_template  

app = Flask(__name__)

@app.route('/')
def index():

	list_data=[
		{'description' : 'Todo 1'}, 
		{'description' : 'Todo 2'}, 
		{'description' : 'Todo 3'}, 
		{'description' : 'Todo 4'}, 
	]

	return render_template('index.html', data=list_data)
	
