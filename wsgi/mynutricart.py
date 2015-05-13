from flask import Flask
import MySQLdb
from os import environ
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calcs",methods = ["POST","GET"])
def calcs():
    try:
        db = MySQLdb.connect(environ['OPENSHIFT_MYSQL_DB_HOST'], environ['OPENSHIFT_MYSQL_DB_USERNAME'], environ['OPENSHIFT_MYSQL_DB_PASSWORD'], 'mynutricart')
        db.query("SELECT * FROM CaloriesToPortions")
    except MySQLdb.Error, e:
        return "Error %d: %s" % (e.args[0], e.args[1])
    finally:
        if db:
            db.close()
    return "success"

if __name__ == "__main__":
    app.run()
