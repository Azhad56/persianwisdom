from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/author/")
def author():
    return render_template("author_guidelines.html")
@app.route("/focus/")
def focus():
    return render_template("focus.html")
@app.route("/contact/")
def contact():
    return render_template("contact.html")
if __name__ =='__main__':
    app.run(debug=True)
