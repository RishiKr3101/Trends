from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") 
def landingpage():
	return render_template("LogIn.html")

@app.route("/signup") 
def signup():
	return render_template("SignUP.html")

@app.route("/about") 
def about():
	return render_template("about.html")

@app.route("/home") 
def home():
	return render_template("home.html")

@app.route("/menfashion") 
def menf():
	return render_template("men_fashion.html")

@app.route("/womenfashion") 
def wmenf():
	return render_template("women_fashion.html")


@app.route("/kidfashion") 
def kidf():
	return render_template("kids_fashion.html")

@app.route("/Offers") 
def offer():
	return render_template("offers.html")


if __name__ == "__main__" :
    app.run(debug=True)
