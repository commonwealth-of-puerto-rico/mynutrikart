from flask import Flask
import MySQLdb
from os import environ
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calcs",methods = ["POST"])
def calcs():
	# Open database connection
	db = MySQLdb.connect(environ['OPENSHIFT_MYSQL_DB_HOST'], environ['OPENSHIFT_MYSQL_DB_USERNAME'], environ['OPENSHIFT_MYSQL_DB_PASSWORD'], 'krowdvision')

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute("SELECT * from CaloriesToPortions;")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchone()

	print "Database version : %s " % data
		
	# disconnect from server
	db.close()	
	return "Hello World!

if __name__ == "__main__":
    app.run()

