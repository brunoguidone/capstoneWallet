from flask import Flask, render_template
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from model import Base

#engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

app = Flask(__name__)

#Base.metadata.bind = engine

#DBSession = sessionmaker(bind=engine)
#session = DBSession()


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/v1/wallet/balance")
def balance():
    return "Hello, World! Balance"


@app.route("/v1/wallet/addfunds")
def addfunds():
    return "Hello, World! Funds"


@app.route("/v1/wallet/transactions")
def transactions():
    return "Hello, World! Transactions"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
