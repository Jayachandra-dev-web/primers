"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse
from config import Config
from FlaskWebProject import app, db
from FlaskWebProject.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from FlaskWebProject.models import User, Post
import msal
import uuid

# ✅ Build image source URL using connection string account name
# Extract account name from the connection string
import re
conn_str = app.config['BLOB_CONNECTION_STRING']
match = re.search(r'AccountName=([^;]+)', conn_str)
account_name = match.group(1) if match else "youraccount"

imageSourceUrl = f"https://{account_name}.blob.core.windows.net/{app.config['BLOB_CONTAINER']}/"
