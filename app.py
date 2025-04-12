from flask import Flask, render_template, request, jsonify
from pydantic import BaseModel, ValidationError
from Contacto import Contacto

app = Flask(__name__)

contactos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact')
def add_contact():
    return render_template('add_contact.html')

@app.route('/contact', methods=['POST'])
def crear_contacto():
    try:
        # recibo los datos del formulario HTML
        # y los convierto en un objeto Contacto
        nombre = request.form.get('name')
        apellidos = request.form.get('surname')
        telefono = request.form.get('phone')
        mail = request.form.get('email')
        contacto = Contacto(nombre=nombre, apellidos=apellidos, telefono=telefono, mail=mail)
      
        # Aquí podrías guardar el contacto en tu base de datos o hacer otras operaciones
        contactos.append(contacto)
        return render_template('contacto_creado.html', contacto=contacto)   
    except ValidationError as e:
        # Capturamos la excepción ValidationError de Pydantic
        errores = e.errors()
        return render_template('contacto_no_creado.html', errores=errores)
    

@app.route('/list_contacts', methods=['GET'])
def listar_contactos():
    return render_template('contactos.html', contactos=contactos)

@app.route('/delete_contact')
def eliminar_contacto():
    return render_template('delete_contact.html', contactos=contactos)

@app.route('/delete_contact/<int:index>')
def eliminar_contacto_post(index):
    try:
        # Eliminar el contacto de la lista
        if 0 <= index < len(contactos):
            contactos.pop(index)
            return render_template('contacto_eliminado.html')
    except Exception as e:
        return  render_template('contacto_no_eliminado.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)