from flask import Flask , render_template, request, redirect, url_for, send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required

import subprocess
from subprocess import PIPE
import os, uuid, re, tempfile
import time

app = Flask(__name__)

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
    num_ej = int(ej[0])
    if not form.editor.data:
        form.editor.data = formato_funcion(tema, num_ej)

    lista_ejs = os.listdir("templates/ejercicios/{}".format(tema))[::-1]
    prox_ej = lista_ejs[( num_ej) % len(lista_ejs)].replace('.html','')

    if request.method == 'POST' and form.validate():
        if request.form['submit'] == 'Print':
            filename = str(uuid.uuid4().hex) + '.py'
            with open(filename,'w') as file:
                file.write(form.editor.data)
            return send_file(filename,  attachment_filename='ej.py', as_attachment=True)
        result = str(runCode(form.editor.data, tema, num_ej))
    return render_template('home.html', 
                            form = form, tema = tema, ej = ej, num_ej = num_ej, result = result, 
                            ejs_tema = len(lista_ejs), prox_ej = prox_ej
                            )

# LISTA DE EJERCICIOS POR TEMA
@app.route('/listado/<tema>', methods = ['POST', 'GET'])
def listado(tema):
    ejercicios = list(map(lambda s: s.replace('.html','') , getListaEjerciciosOrdenada(tema)))
    return render_template("listado.html", ejercicios = ejercicios, tema = tema)

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
    command = f"rm -rf ./{folder_name} && ./CleanContainers.sh"
    command = command.split()
    subprocess.Popen(command) #Python remove dir does not allow remove a non empty folder

    print(errs)
    return errs

def formato_funcion(tema, num_ej):
    with open('pruebas/{}/{}.py'.format(tema,num_ej)) as pruebas:
        nombre_funcion = pruebas.readline()
        regex = re.compile('#\s*')
        return regex.sub('',nombre_funcion).rstrip() 

def getListaEjerciciosOrdenada(tema):
    return os.listdir("templates/ejercicios/{}".format(tema))[::-1]
