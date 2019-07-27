from flask import Blueprint, render_template
import os

listado_blueprint = Blueprint('listado', __name__)

# LISTA DE EJERCICIOS POR TEMA
@listado_blueprint.route('/listado/<tema>', methods = ['POST', 'GET'])
@listado_blueprint.route('/listado/<tema>/<ej>' , methods = ['POST', 'GET'])
def listado(tema, ej = None):
    if (not temaValido(tema)):
        return render_template('404.html'), 404
    secciones = getListaSeccionOrdenada(tema)
    ejercicios = None
    if (ej):
        ejercicios = getListaEjerciciosOrdenada(tema, ej)
    return render_template("listado.html", secciones = secciones, tema = tema, ejercicios = ejercicios, ej = ej)


def getListaSeccionOrdenada(tema):
    list_secciones = []
    with open(f"info/{tema}/carpetas.csv") as carpetas:
        for seccion in carpetas:
            list_secciones.append(seccion)
    return list_secciones

def getListaEjerciciosOrdenada(tema, ej):
    list_ejs = []
    with open(f"info/{tema}/{ej}.csv") as seccion:
        for ej in seccion:
            list_ejs.append(ej)
    return list_ejs

def temaValido(tema):
    return tema in os.listdir("info")