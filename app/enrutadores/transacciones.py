from fastapi import APIRouter,HTTPException, status
from ..modelos.transaccion import Transaccion, transaccioncrear, transaccioneditar
from ..modelos.factura import Factura
from ..listas import lista_facturas, lista_transacciones
from ..conexion_BD import Sesion_dependencia
from sqlmodel import select
ruta_transacciones = APIRouter ()

#lista_transacciones: list [Transaccion] = [] 
#lista_facturas: list [Factura] = []


@ruta_transacciones.get ("/transacciones", response_model=list [Transaccion])
async def listar_transacciones (sesion: Sesion_dependencia):
    consulta = select(Transaccion)
    lista_trans = sesion.exec(consulta).all()
    return lista_trans
#return sesion.exec(select (transaccion) ).all() 

@ruta_transacciones.get ("/transacciones/{transacciones_id}", response_model= Transaccion)
async def listar_transacciones (id_transacciones: int):
    for i, obj_transaccion in enumerate (lista_transacciones):
        if obj_transaccion.id == id_transacciones:
            return obj_transaccion
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La transaccion con id {id_transacciones}, no existe."
    )


@ruta_transacciones.post ("/transacciones/{factura_id}", response_model= Transaccion)
async def crear_transacciones (factura_id: int, datos_transacciones: transaccioncrear,sesion: Sesion_dependencia):
    #buscar una factura en bd
    factura_encontrada = sesion.get(Factura, factura_id)

    if not factura_encontrada:
          raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
        )  

        #validar datos de la transaccion-json y lo pasamos a dict
    transaccion_dict = datos_transacciones.model_dump()
    transaccion_dict ["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar en bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val




@ruta_transacciones.patch("/transacciones/{transacciones_id}", response_model=Transaccion)
async def editar_transacciones(
    transacciones_id: int,
    datos_transacciones: transaccioneditar,
    mi_sesion: Sesion_dependencia
):
    transaccion_bd = mi_sesion.get(Transaccion, transacciones_id)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {transacciones_id}, no existe."
        )
    transaccion_dic = datos_transacciones.model_dump(exclude_unset=True)
    transaccion_bd.sqlmodel_update(transaccion_dic)
    mi_sesion.add(transaccion_bd)
    mi_sesion.commit()
    mi_sesion.refresh(transaccion_bd)
    return transaccion_bd




@ruta_transacciones.delete("/transacciones/{transacciones_id}", response_model=Transaccion)
async def eliminar_transaccion(transacciones_id: int, mi_sesion: Sesion_dependencia):
    transaccion_bd = mi_sesion.get(Transaccion, transacciones_id)

    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {transacciones_id}, no existe."
        )

    mi_sesion.delete(transaccion_bd)
    mi_sesion.commit()

    return transaccion_bd
