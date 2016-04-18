from flask import Flask
from mysqlconnection import MySQLConnector

mod = Flask(__name__)
mysql = MySQLConnector("media_aggregator")

from app import views
