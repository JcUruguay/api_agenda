from webbrowser import parse_args

from flask import Blueprint, jsonify, request
import controllers.contactControler as contactControler

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/contactos', methods=['GET'])
def getContactos():
    parametros = request.args
    id_usuario = parametros['id']
    campo = parametros['campo']
    orden = parametros['orden']

    contactos = contactControler.seleccionar_Contactos(id_usuario, campo, orden)

    return jsonify(contactos)

@contact_api.route('/contacto', methods=['GET'])
def getContacto():
    parametros = request.args
    id_contacto = parametros['id']

    contacto = contactControler.seleccionar_Contacto(id_contacto)

    return jsonify(contacto)

@contact_api.route('/contactoStr', methods=['GET'])
def getContactoStr():
    parametros = request.args
    id_usuario = parametros['id']
    texto = parametros['texto']

    contacto = contactControler.busqueda_contactos(id_usuario,texto)

    return jsonify(contacto)

@contact_api.route('/contacto', methods=['POST'])
def insertContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']

    resultado = contactControler.insertar_contacto(id_usuario, nombre, apellidos, direccion, email, telefono)

    return jsonify(resultado)

@contact_api.route('/contacto', methods=['PUT'])
def actualizarContacto():
    parametros = request.args
    id_contacto = parametros['id_contacto']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']

    resultado = contactControler.actualizar_contacto(id_contacto, nombre, apellidos, direccion, email, telefono)

    return jsonify(resultado)

@contact_api.route('/contacto', methods=['DELETE'])
def eliminarContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    id_contacto = parametros['id_contacto']

    resultado = contactControler.eliminar_contacto(id_usuario, id_contacto)

    return jsonify(resultado)