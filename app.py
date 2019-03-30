from flask import Flask , render_template, request, redirect, url_for, send_file, after_this_request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required

from clases.Db import Db

import subprocess
from subprocess import PIPE
import os, uuid, re, tempfile
import time
import re

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# INDEX
@app.route('/')
def index():
    return render_template('index.html')

# CONSOLA PARA EJERCITAR
@app.route('/form', methods = ['POST', 'GET'])
@app.route('/form/<tema>/<string:ej>', methods = ['POST', 'GET'])
def form(tema, ej):
    form = CodeForm(request.form)
    result = ""
    consola_display = 'none'
    num_ej = int(ej[0])
    if not form.editor.data:
        form.editor.data = formato_funcion(tema, num_ej)

    lista_ejs = ordenar_lista_directorio(os.listdir("templates/ejercicios/{}".format(tema)))
    prox_ej = lista_ejs[( num_ej) % len(lista_ejs)].replace('.html','')

    if request.method == 'POST' and form.validate():
        consola_display = 'visible'
        if request.form['submit'] == 'Print':
            filename = str(uuid.uuid4().hex) + '.py'
            with open(filename,'w') as file:
                file.write(form.editor.data)
            # Remuevo el archivo creado para descargar el código
            @after_this_request 
            def remove_file(response): 
                os.remove(filename) 
                return response 

            return send_file(filename,  attachment_filename='ej.py', as_attachment=True)
        result = formatear_salida( str(runCode(form.editor.data, tema, num_ej)))
    return render_template('home.html', 
                            form = form, tema = tema, ej = ej, num_ej = num_ej, result = result, 
                            ejs_tema = len(lista_ejs), prox_ej = prox_ej, consola_display = consola_display
                            )

# LISTA DE EJERCICIOS POR TEMA
@app.route('/listado/<tema>', methods = ['POST', 'GET'])
def listado(tema):
    ejercicios = ordenar_lista_directorio(list(map(lambda s: s.replace('.html','') , getListaEjerciciosOrdenada(tema))))
    return render_template("listado.html", ejercicios = ejercicios, tema = tema)

@app.route('/guia', methods = ['POST', 'GET'])
def guia():
    guia = os.listdir("./templates/ejercicios") 
    return render_template("guia.html", guia = guia)

# SOBRE LA PÁGINA
@app.route('/about')
def about():
    return render_template("about.html")

# CARGAR UN NUEVO EJERCICIO
@app.route('/subir')
def subir():
    return render_template("subir.html")

# 404 PAGINA NO ENCONTRADA
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
# Clases (i will refactor this later)

class CodeForm(Form):
    editor = TextAreaField('editor')
    submit = SubmitField('Submit')

def runCode(code, tema, num_ej):
    pruebas = ''
    with open(f'pruebas/{tema}/{num_ej}.py') as test:
        pruebas = test.read()

    base_name = str(uuid.uuid4().hex)
    filename = base_name + '.py'
    folder_name = base_name

    # Create user folder
    os.mkdir(f"./{folder_name}")

    # Create the untrusted code file
    with open(f"./{folder_name}/{filename}",'w') as file:
        file.write('import unittest' + '\n' + code + '\n\n' + pruebas)

    # Command to execute
    command = (f"docker run "
                f"-v {os.getcwd()}/{folder_name}:/src"
                f" --attach STDOUT --attach STDERR "
                f" run-container python3 ./{filename} -v").split()

    # Excecute the untrusted code
    proc = subprocess.Popen(command,stdout=PIPE, stderr=PIPE)
    try:
        outs, errs = proc.communicate(timeout=4)
        errs = errs.decode('UTF-8')
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        errs = 'TimeoutExpires exception'

    # Remove the user folder and container
    command = f"rm -rf ./{folder_name}".split()
    subprocess.Popen(command) #Python remove dir does not allow remove a non empty folder

    command = f"./CleanContainers.sh".split()
    subprocess.Popen(command)

    print(errs)
    return errs

def formato_funcion(tema, num_ej):
    with open('pruebas/{}/{}.py'.format(tema,num_ej)) as pruebas:
        nombre_funcion = pruebas.readline()
        regex = re.compile('#\s*')
        return regex.sub('',nombre_funcion).rstrip() 

def getListaEjerciciosOrdenada(tema):
    return os.listdir("templates/ejercicios/{}".format(tema))[::-1]

def ordenar_lista_directorio(lista):
    return sorted(lista,key=lambda nombre: nombre[0])

def formatear_salida(salida):
    salida = salida.replace('\n','<br>')
    salida = re.sub(r'(FAIL: test_[\w\s\(\.\)]*)', '<span id="error">'+ r'\1' + '</span>', salida)
    salida = re.sub(r'(FAIL(ED)?)', '<span id="rojo">' + r'\1' + '</span>', salida)
    salida = re.sub(r'(ok|OK)', '<span id="verde">' + r'\1' + '</span>', salida)
    salida = re.sub(r'(test_\w*)', '<span id="funcion">'+ r'\1' + '</span>', salida)
    return salida
