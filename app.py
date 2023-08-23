from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "klsadjfl_asdflkj_afds"

@app.route("/hello")
def index():
    flash("kijan ou rele?")
    return render_template("index.html")

@app.route("/greet", methods = ["POST", "GET"])
def greet():
    flash("Bonjou " + str(request.form['nom_input']) + ", mwen kontan rekonet ou!")
    

    return render_template("index.html")
    
