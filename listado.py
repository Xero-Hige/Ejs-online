from flask import Blueprint, render_template
import os

listado_blueprint = Blueprint('listado', __name__)

# LISTA DE EJERCICIOS POR TEMA
@listado_blueprint.route('/listado/<tema>', methods = ['POST', 'GET'])
@listado_blueprint.route('/listado/<tema>/<ej>' , methods = ['POST', 'GET'])
def listado(tema, ej = None):
    secciones = getListaSeccionOrdenada(tema)
    ejercicios = None
    if (ej):
        ejercicios = getListaEjerciciosOrdenada(tema, ej)
    return render_template("listado.html", secciones = secciones, tema = tema, ejercicios = ejercicios, ej = ej)


def getListaSeccionOrdenada(tema):
    list_secciones = []
    with open('info/carpetas.csv') as carpetas:
        for seccion in carpetas:
            list_secciones.append(seccion)
    return list_secciones

def getListaEjerciciosOrdenada(tema, ej):
    list_secciones = []
    with open(f"info/{ej}.csv") as carpetas:
        for seccion in carpetas:
            list_secciones.append(seccion)
    return list_secciones