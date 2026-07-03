from fastapi import FastAPI, HTTPException, status
from .enrutadores.clintes import ruta_cliente
from .enrutadores.facturas import ruta_facturas
from .enrutadores.transacciones import ruta_transacciones
from .conexion_BD import crear_tablas

app= FastAPI (lifespan= crear_tablas)

#incluir ruta de clientes 
app.include_router(ruta_cliente, tags=["Clientes"])
app.include_router(ruta_facturas, tags=["Facturas"])
app.include_router(ruta_transacciones, tags=["Transacciones"])

