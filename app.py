from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notas = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texto = request.form.get("nota")
        if texto:
            notas.append(texto)
        return redirect("/")

    return render_template("index.html", notas=notas)

if __name__ == "__main__":
    app.run(debug=True)