from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import like_op

from db import conectar
from models import Contacto, Pertenece

def seleccionar_Contactos(id_usuario, campo, orden):
    session = Session()
    contactos = []

    try:
        session = conectar()
        id_union = Contacto.id == Pertenece.id_contacto
        filtro = Pertenece.id_usuario == int(id_usuario)
        if campo == 'ID' and orden == 'ASC':
            orden = Contacto.id
        elif campo == 'ID' and orden == 'DSC':
            orden = Contacto.id.dsc()
        elif campo == 'NOMBRE' and orden == 'ASC':
            orden = Contacto.nombre
        elif campo == 'NOMBRE' and orden == 'DSC':
            orden = Contacto.nombre.dsc()

        contactos = session.query(Contacto).join(Pertenece, id_union).filter(filtro).order_by(orden).all()

    except Exception as e:
        print(f'Error: {e}')

    finally:
        session.close()

    return contactos

def seleccionar_Contacto(id_contacto):
    contacto = None
    session = Session()

    try:
        session = conectar()
        # Buscar contacto por id
        contacto = session.query(Contacto).get(id_contacto)

    except Exception as e:
        print(f'Error: {e}')
    finally:
        session.close()

    return contacto

def busqueda_contactos(id_usuario, texto):
    contactos = []
    session = Session()

    try:
        session = conectar()
        id_union = Contacto.id == Pertenece.id_contacto
        filtro_1 = Pertenece.id_usuario == int(id_usuario)
        filtro_2 = Contacto.nombre.ilike('%'+texto+'%') | Contacto.apellidos.ilike('%'+texto+'%') | Contacto.direccion.ilike('%'+texto+'%') | Contacto.email.ilike('%'+texto+'%')

        contactos = session.query(Contacto).join(Pertenece, id_union).filter(filtro_1).filter(filtro_2).all()

    except Exception as e:
        print(f'Error: {e}')
    finally:
        session.close()

    return contactos

def insertar_contacto(id_usuario, nombre, apellidos, direccion, email, telefono):
    session = Session()

    try:
        # Agregar contacto a la BD
        contacto = Contacto(
            nombre = nombre,
            apellidos = apellidos,
            direccion = direccion,
            email = email,
            telefono = telefono
        )

        session = conectar()
        session.add(contacto)       # Agrego el contacto a la BD
        session.commit()

        session.refresh(contacto)
        id_contacto = contacto.id  # Devuelvo el id de contacto que se creo

        # Agregar pertenece a la BD
        pertenece = Pertenece(
            id_usuario = id_usuario,
            id_contacto = id_contacto
        )

        session.add(pertenece)
        session.commit()

    except Exception as e:
        print(f'Error: {e}')
        return False
    finally:
        session.close()

    return True

def actualizar_contacto(id_contacto, nombre, apellidos, direccion, email, telefono):
    session = Session()

    try:
        session = conectar()

        # Obtener contacto por el id
        contacto = session.query(Contacto).get(id_contacto)

        # Editar contacto a la BD
        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono

        session.add(contacto)
        session.commit()

    except Exception as e:
        print(f'Error: {e}')
        return False
    finally:
        session.close()

    return True

def eliminar_contacto(id_usuario, id_contacto):
    session = Session()

    try:
        session = conectar()

        # Devolver registro de pertenece
        filtro = (Pertenece.id_usuario == int(id_usuario)) & (Pertenece.id_contacto == int(id_contacto))
        # Eliminar de la tabla Pertenece
        session.query(Pertenece).filter(filtro).delete()

        # Devolver registro de contacto
        contacto = session.query(Contacto).get(id_contacto)
        # Eliminar de la tabla contacto
        session.delete(contacto)
        session.commit()

    except Exception as e:
        print(f'Error: {e}')
        return False
    finally:
        session.close()

    return True