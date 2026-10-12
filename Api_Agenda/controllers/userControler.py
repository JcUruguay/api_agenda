from sqlalchemy.orm import Session
from db import conectar
from models import Usuario

def seleccionarUsuario(email, password):
    id = 0
    session = Session()
    try:
        session = conectar()
        filtro = Usuario.email == email and Usuario.password == password
        # Devuelvo una lista donde emial y pass coincida con la busqueda en la BD
        usuarios = session.query(Usuario).filter(filtro).all()
        print(f'usuarios en seleccionarUsuario {usuarios}')
        if len(usuarios) > 0:
            id = usuarios[0].id

    except Exception as e:
        print(f'{e}')

    finally:
        session.close()

    return id

