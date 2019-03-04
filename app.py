
from flask import Flask , render_template, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required

import subprocess
import os
import uuid
import re


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST', 'GET'])
@app.route('/form/<tema>/<int:num_ej>', methods = ['POST', 'GET'])
def form(tema, num_ej):
    form = CodeForm(request.form)
    result = None
    if not form.editor.data:
        form.editor.data = formato_funcion(tema, num_ej)

    lista_ejs = os.listdir("templates/ejercicios/{}".format(tema))

    if request.method == 'POST' and form.validate():
        result = str(runCode(form.editor.data, tema, num_ej))
        if result == '':
            result = "Pasaste todas las pruebas!" 
    return render_template('home.html', 
                            form = form, tema = tema, num_ej = num_ej, result = result, 
                            ejs_tema = len(lista_ejs)
                            )



@app.route('/home', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("home.html",result = result)

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
# Clases (i will refactor this later)

class CodeForm(Form):
    editor = TextAreaField('editor')
    submit = SubmitField('Submit')

def runCode(code, tema, num_ej):
    pruebas = ''
    with open('pruebas/{}/{}.py'.format(tema,num_ej)) as test:
        pruebas = test.read()
    filename = str(uuid.uuid4().hex) + '.py'
    with open(filename,'w') as file:
        file.write(code)
        file.write('\n\n')
        file.write(pruebas)
    result = subprocess.run(['python3', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.remove(filename) 
    return result.stderr.decode('UTF-8')

def formato_funcion(tema, num_ej):
    with open('pruebas/{}/{}.py'.format(tema,num_ej)) as pruebas:
        nombre_funcion = pruebas.readline()
        regex = re.compile('#\s*')
        return regex.sub('',nombre_funcion).rstrip() + '\n' + '\t'