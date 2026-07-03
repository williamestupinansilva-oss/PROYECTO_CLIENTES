from fastapi import APIRouter, HTTPException, status
from ..modelos.factura import Factura, facturacrear, facturaeditar, FacturaLeer, facturaleercompuesta
from ..modelos.cliente import cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_BD import Sesion_dependencia
from sqlmodel import select
ruta_facturas = APIRouter ()

#lista_facturas: list [Factura] = []
#lista_clientes: list [cliente] = [] 

@ruta_facturas.get ("/facturas", response_model=list [facturaleercompuesta])
async def listar_facturas (sesion:Sesion_dependencia):
    #select * from factura
    consulta = select (Factura)
    lista_facturas = sesion.exec(consulta).all ()
    return lista_facturas


@ruta_facturas.get ("/facturas/{cliente_id}", response_model= Factura)
async def listar_facturas (factura_id: int):
    for i, obj_factura in enumerate (lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
    )


@ruta_facturas.post ("/facturas/{cliente_id}", response_model= Factura)
async def crear_factura (cliente_id: int, datos_factura: facturacrear, sesion: Sesion_dependencia):
    #buscar el cliente en bd 

    cliente_encontrado = sesion.get(cliente, cliente_id)  
    #mensaje si cliente no fue encontrado
    if not cliente_encontrado:
          raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe."
        )  


    #validar datos de la factura-json,  pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict ["cliente_id"] = cliente_id 
    factura_val = Factura.model_validate(factura_dict)
    #guaradr en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val






@ruta_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(
    factura_id: int,
    datos_factura: facturaeditar,
    mi_sesion: Sesion_dependencia
):
    factura_bd = mi_sesion.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )
    factura_dic = datos_factura.model_dump(exclude_unset=True)
    factura_bd.sqlmodel_update(factura_dic)
    mi_sesion.add(factura_bd)
    mi_sesion.commit()
    mi_sesion.refresh(factura_bd)
    return factura_bd



@ruta_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int, mi_sesion: Sesion_dependencia):
    factura_bd = mi_sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    mi_sesion.delete(factura_bd)
    mi_sesion.commit()

    return factura_bd
