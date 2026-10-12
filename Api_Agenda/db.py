from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Conexion base local
#DATABASE_URI = 'postgresql://postgres:sofia@localhost:5432/agenda'

# Conexion base Render
DATABASE_URI = 'postgresql://agenda_1wpj_user:PsXHZrTAjtMeyKoBCSCpTdR8wKXol3i1@dpg-db6lc4rrjlhs73faelcg-a.oregon-postgres.render.com/agenda_1wpj'

def conectar():
    # Crea el motor de conexion (el enlace a la base de datos)
    engine = create_engine(DATABASE_URI)
    # Se crea la fabrica de sesiones usando sessionmaker
    # Aqui se deja configurado el motor que usaran todas las futuras sesiones
    Session = sessionmaker(bind=engine)
    # Cada vez que se necesite interactuar con la base de daatos, se llama a la fabrica para obtener
    # una sesion nueva y limpia
    obj_sesion = Session()

    # Comprobar conexion
    if obj_sesion != None:
        print('Conexion a base de datos OK')
    else:
        print('Error de conexion a base de datos')

    return obj_sesion