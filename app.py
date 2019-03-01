
from flask import Flask , render_template, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required

import subprocess
import os
import uuid


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST', 'GET'])
@app.route('/form/<tema>/<int:num_ej>', methods = ['POST', 'GET'])
def form(tema, num_ej):
    form = CodeForm(request.form)
    result = None

    cant_ejs_tema = len(os.listdir("templates/ejercicios/{}".format(tema)))

    if request.method == 'POST' and form.validate():
        result = str(runCode(form.editor.data, tema, num_ej))
    return render_template('home.html', form = form, tema = tema, num_ej = num_ej, result = result, ejs_tema = cant_ejs_tema)



@app.route('/home', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("home.html",result = result)


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

    