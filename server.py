import re
from jinja2 import StrictUndefined

from flask import Flask, render_template, session, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

from frame import connect_to_db, db, User, Collective, Post, Link, SQLAlchemy

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined