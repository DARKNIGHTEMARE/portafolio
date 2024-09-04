from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/pregunta")
def prehunta():
    return render_template("pregunta.html")

@app.route("/respuesta", methods=["POST"])
def respuesta():
    if request.method == "POST":
        nam = request.form ['nombre']  

        emm = request.form ['gmail']  

        return render_template("pregunta.html", res=nam, ress=emm)


if __name__ == "__main__":
    app.run()

