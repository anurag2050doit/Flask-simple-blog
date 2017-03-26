import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_blog import app
import sqlalchemy

try:
    db_uri = 'sqlite:///blog.sqlite3'
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE Blog")
    conn.close()
except:
    print "Database exists"

from flask_blog import db

#add model here
from user.models import *
from blog.models import *

db.create_all()
