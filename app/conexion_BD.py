from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = "bd_clientes.sqlite3" 
url_bd = f"sqlite:///{nombre_bd}"  


#motor de base de datos 

motor_base_d = create_engine (url_bd) 

#definir el metodo para crear las tablas
def crear_tablas (app: FastAPI):
    SQLModel.metadata.create_all (motor_base_d)
    yield #no hay nada pararetornar o ejecutar


#definir el metodo para la sesion 
def obtener_sesion ():
    with Session (motor_base_d) as mi_sesion:
        yield mi_sesion #retorna la sesion 

    
#denominacion inyeccion de dependencias.
#registrar la sesion como dependencia, utilizada en nuestros endpoint
Sesion_dependencia = Annotated [Session, Depends(obtener_sesion)]