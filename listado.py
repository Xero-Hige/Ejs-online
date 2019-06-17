from flask import Blueprint, render_template
import os

listado_blueprint = Blueprint('listado', __name__)

# LISTA DE EJERCICIOS POR TEMA
@listado_blueprint.route('/listado/<tema>', methods = ['POST', 'GET'])
@listado_blueprint.route('/listado/<tema>/<ej>' , methods = ['POST', 'GET'])
def listado(tema, ej = None):
    secciones = ordenar_lista_directorio(list(map(lambda s: s.replace('.html','') , getListaSeccionOrdenada(tema))))
    ejercicios = None
    if (ej):
        ejercicios = ordenar_lista_directorio(list(map(lambda s: s.replace('.html','') , getListaEjerciciosOrdenada(tema, ej))))
        print(ej)
    return render_template("listado.html", secciones = secciones, tema = tema, ejercicios = ejercicios, ej = ej)


def getListaSeccionOrdenada(tema):
    return os.listdir("templates/ejercicios/{}".format(tema))[::-1]

def getListaEjerciciosOrdenada(tema, ejs):
    return os.listdir("templates/ejercicios/{}/{}".format(tema, ejs))[::-1]

def ordenar_lista_directorio(lista):
    return sorted(lista, key = lambda nombre: nombre[0])