from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:super@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://foxlwcdvecalfw:9321269a08865396e887c66de20442ab696d71c159c1c6a04ec5e4cd76385964@ec2-54-246-67-245.eu-west-1.compute.amazonaws.com:5432/d8n87i8i0bo535'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
