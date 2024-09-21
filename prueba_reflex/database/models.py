# models.py
from sqlmodel import SQLModel, Session, select, Field
from .connect_db import connect

# Definir el modelo de la tabla 'datos'
class Localidades(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_estado: int
    id_municipio: int
    clave_inegi: str
    localidad: str
    

def get_all_data():
    engine = connect()  
    with Session(engine) as session:
        statement = select(Localidades)
        results = session.exec(statement).all()
        return results
