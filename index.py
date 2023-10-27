from flask import Flask,render_template

app = Flask("prueba_flask")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/contacto")
def contacto():
    return render_template('contactos.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port='5000')
   

