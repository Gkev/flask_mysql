from flask import Flask, render_template, request, redirect, session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'fb1')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

@app.route('/')
def users():
	query = "SELECT * FROM users"
	mysql.query_db(query)
	users = mysql.query_db(query)
	print users

app.run(debug=True)