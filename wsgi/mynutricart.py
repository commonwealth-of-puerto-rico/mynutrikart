from flask import Flask , request
#import MySQLdb
import ast
from os import environ

app = Flask(__name__)

cal = [1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200]

def cal_floor(calories):
    val = 0
    for c in cal:
        if calories > c:
            val = c
        else:
            return val
    return val

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calcs",methods=["POST","GET"])
def calcs():
    data = ast.literal_eval(request.data)
    for k,v in enumerate(data):
        data[v] = cal_floor(data[v])

    query = "SELECT SUM(Grains),SUM(Vegetables),SUM(Fruit),SUM(Diary),SUM(Protein) FROM CaloriesToPortions WHERE "
    for k,v in enumerate(data):
        query = query + "Calories = " + str(data[v]) + " OR "
    try:
        db = MySQLdb.connect(environ['OPENSHIFT_MYSQL_DB_HOST'], environ['OPENSHIFT_MYSQL_DB_USERNAME'], environ['OPENSHIFT_MYSQL_DB_PASSWORD'], 'mynutricart')
        db.query(query[:-3])
    except MySQLdb.Error, e:
        return "Error %d: %s" % (e.args[0], e.args[1])
    finally:
        if db:
            db.close()
    return query[:-3]

if __name__ == "__main__":
    app.run()
