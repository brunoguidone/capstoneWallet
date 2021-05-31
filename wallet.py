from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import secrets
import dbConstruct

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.secret_key = secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@mysql-0.mysql/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    transactiontype = db.Column(db.String(20))

    def __init__(self, name, amount,  transactiontype):
        self.name = name
        self.amount = amount
        self.transactiontype = transactiontype


@app.route('/')
def Index():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@mysql/mysql'
    all_data = Data.query.all()

    total = 0
    for x in all_data:
        total += x.amount

    return render_template("index.html", amounts=all_data, total=total)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        transaction_type = "(C) Credit"

        my_data = Data(name, amount, transaction_type)
        db.session.add(my_data)
        db.session.commit()

        flash("Amount Inserted Successfully")

        return redirect(url_for('Index'))


@app.route('/withdraw', methods=['POST'])
def withdraw():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        transaction_type = "(S) Payment"

        negative_amount = int(amount) * -1

        my_data = Data(name, negative_amount, transaction_type)
        db.session.add(my_data)
        db.session.commit()

        flash("Amount withdrawn Successfully")

        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")