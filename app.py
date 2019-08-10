from flask import Flask , render_template, request, redirect, url_for, send_file, after_this_request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required


from index import index_blueprint
from about import about_blueprint
from guia import guia_blueprint
from listado import listado_blueprint
from ejercicios import form_blueprint


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.register_blueprint(index_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(guia_blueprint)
app.register_blueprint(listado_blueprint)
app.register_blueprint(form_blueprint)


# 404 PAGINA NO ENCONTRADA
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# # CARGAR UN NUEVO EJERCICIO

# @app.route('/subir')
# def subir():
#     return render_template("subir.html")


