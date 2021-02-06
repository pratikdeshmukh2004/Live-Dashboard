from flask import current_app, render_template, url_for, flash, redirect, request

import os
import secrets

from app import database
from . import main
from .models import Meals

@main.route("/")
def home_page():
    return render_template('home.html')

@main.route("/dashboard")
def dashboard():
    meals = Meals.query.order_by(Meals.id.desc()).all()
    print(meals)
    return render_template('dashboard.html', meals = meals)

@main.route('/delete_chat/<int:id>')
def deleteMsg(id):
    message = Message.query.get(id)
    database.session.delete(message)
    database.session.commit()
    return redirect(url_for('main.dashboard'))


@main.route('/delete_all')
def deleteAll():
    messages = Meals.query.all()
    for m in messages:
        database.session.delete(m)
    database.session.commit()
    return redirect(url_for('main.dashboard'))
