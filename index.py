from flask import Blueprint, render_template
import os

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route("/")
def index():
    opciones = os.listdir("templates/ejercicios")
    return render_template('index.html', opciones = opciones)

    