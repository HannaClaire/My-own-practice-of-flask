from app import app
from flask import render_template
from models.tickets import tickets


@app.route('/')
def index():
    return render_template('index.jinja', title='Ticket Orders', tickets = tickets)
