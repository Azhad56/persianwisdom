from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/author",methods = ['Get','Post'])
def author():
    return render_template("author_guidelines.html")
if __name__ =='__main__':
    app.run(debug=True)
