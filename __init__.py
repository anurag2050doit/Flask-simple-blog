from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.ext.markdown import Markdown
app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
Migrate = Migrate(app, db)

# Markdown
md = Markdown(app,extensions=['fenced_code','tables'])

from blog import views
from user import views
