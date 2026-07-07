from fastapi import APIRouter, HTTPException, status
from ..modelos.cliente import cliente, clientecrear, clienteeditar
from ..listas import lista_clientes
from ..conexion_BD import Sesion_dependencia
from sqlmodel import select
from ..modelos.factura import Factura


ruta_cliente = APIRouter () 



@ruta_cliente.get ("/lista de clientes", response_model=list [cliente])
async def listar_clientes (sesion: Sesion_dependencia):
    lista_cli = sesion.exec ( select(cliente) ).all ()
    return lista_cli 

#endpoint listar un cliente
@ruta_cliente.get("/clientes/{cliente_id}", 
                    response_model=cliente,
)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(cliente, cliente_id) 
    if not cliente_bd:
         raise HTTPException(
        status_code=status. HTTP_400_BAD_REQUEST,
          detail=f"El cliente con id {cliente_id}, no existe."
    )
    return cliente_bd

#endpoint para crear un cliente, y agregarlo a al lista 
@ruta_cliente.post("/crear cliente", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear, mi_sesion: Sesion_dependencia):
    cliente_val = cliente.model_validate(datos_cliente.model_dump()) 
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh (cliente_val)
    return cliente_val


@ruta_cliente.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteeditar, mi_sesion: Sesion_dependencia
):
    cliente_bd = mi_sesion.get(cliente, cliente_id) 
    if not cliente_bd:
        raise HTTPException(
            status_code=status. HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )   
    cliente_dic = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dic)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh (cliente_bd)
    return cliente_bd


   

# endpoint eliminar cliente
@ruta_cliente.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    facturas_cliente = mi_sesion.exec(
        select(Factura).where(Factura.cliente_id == cliente_id)
    ).all()

    if facturas_cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede eliminar el cliente con id {cliente_id} porque tiene facturas asociadas."
        )

    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()

    return cliente_bd