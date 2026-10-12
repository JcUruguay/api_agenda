from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

@dataclass
class Usuario(Base):
    id: int
    nombre: str
    apellidos: str
    email: str
    password: str

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self) -> str:
        return (f'Usuario(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos},'
                f'email={self.email}, password={self.password})')

@dataclass
class Contacto(Base):
    id: int
    nombre: str
    apellidos: str
    direccion: str
    email: str
    telefono: str
    fechaCreacion: datetime

    __tablename__ = 'contacto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaCreacion = Column(DateTime, default=datetime.today())

    def __repr__(self) -> str:
        return (f'Contacto(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos},'
                f'direccion={self.direccion}, email={self.email}, telefono={self.telefono},'
                f'fechaCreacion={self.fechaCreacion})')

@dataclass
class Pertenece(Base):
    id: int
    id_usuario: int
    id_contacto: int

    __tablename__ = 'pertenece'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_contacto = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return (f'Pertenece(id={self.id}, id_usuario={self.id_usuario},'
                f' id_contacto={self.id_contacto})')