from flask import Blueprint, request, jsonify
import controllers.userControler as userControler

user_api = Blueprint('user_api', __name__)

@user_api.route('/usuario', methods=['GET'])
def getUsuario():
    parametros = request.args
    email = parametros['email']
    password = parametros['password']

    resultado = userControler.seleccionarUsuario(email, password)

    return jsonify(resultado)
