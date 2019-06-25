from flask import Blueprint, render_template
import os

listado_blueprint = Blueprint('listado', __name__)

# LISTA DE EJERCICIOS POR TEMA
@listado_blueprint.route('/listado/<tema>', methods = ['POST', 'GET'])
@listado_blueprint.route('/listado/<tema>/<ej>' , methods = ['POST', 'GET'])
def listado(tema, ej = None):
    secciones = list(map(lambda s: s.replace('.html','') , getListaSeccionOrdenada(tema)))
    ejercicios = None
    if (ej):
        ejercicios = ordenar_lista_directorio(list(map(lambda s: s.replace('.html','') , getListaEjerciciosOrdenada(tema, ej))))
        print(ej)
    return render_template("listado.html", secciones = secciones, tema = tema, ejercicios = ejercicios, ej = ej)


def getListaSeccionOrdenada(tema):
    list_secciones = []
    with open('info/carpetas.csv') as carpetas:
        for seccion in carpetas:
            list_secciones.append(seccion)
    return list_secciones

def getListaEjerciciosOrdenada(tema, ejs):
    list_secciones = []
    with open(f"info/{ejs}.csv") as carpetas:
        for seccion in carpetas:
            list_secciones.append(seccion)
    return list_secciones

def ordenar_lista_directorio(lista):
    return sorted(lista, key = lambda nombre: nombre[0])