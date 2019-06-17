from flask import Blueprint, render_template
import os

guia_blueprint = Blueprint('guia', __name__)


@guia_blueprint.route('/guia', methods = ['POST', 'GET'])
def guia():
    guia = os.listdir("./templates/ejercicios") 
    return render_template("guia.html", guia = guia)