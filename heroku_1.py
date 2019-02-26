from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://qxgxjhjumacgzv:f0d4df8106232bbdf33a018d9ac394d3f831edb581416d78f564a240e1021db8@ec2-54-204-41-109.compute-1.amazonaws.com:5432/dcb9mtuo2uer7g?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = "data"
	id = db.Column(db.Integer, primary_key = True)
	height = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	shoesize = db.Column(db.Integer)
	sex = db.Column(db.String)

	def __init__(self, height, weight, shoesize, sex):
		self.height = height
		self.weight = weight
		self.shoesize = shoesize
		self.sex = sex

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/success", methods = ['POST'])
def success_post():
	if(request.method == 'POST'):
		height_ = request.form["height"]
		weight_ = request.form["weight"]
		shoesize_ = request.form["shoesize"]
		sex_ = request.form["sex"]
		data = Data(height_,weight_,shoesize_,sex_)
		db.session.add(data)
		db.session.commit()
		return render_template("success.html")

@app.route("/success", methods = ['GET'])
def success_get():
	return render_template("success.html")

@app.route("/about")
def about():
	return render_template("about.html")
	
@app.route("/collector")
def collector():
	return render_template("collector.html")

if (__name__ =="__main__"):
	app.run(debug=True)