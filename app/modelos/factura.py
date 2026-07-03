from pydantic import BaseModel, computed_field
from .transaccion import Transaccion
from sqlmodel import SQLModel, Field, Relationship
from .cliente import cliente, ClienteLeer
from datetime import datetime

class facturasbase(SQLModel):
    fecha: str = Field(default=datetime.now())

    @computed_field
    @property
    def val_total(self) -> float:
        total_factura = 0.0
        transacciones = getattr(self, "transacciones", None)

        if not transacciones:
            return total_factura

        for transaccion in transacciones:
            total_factura += transaccion.val_unitario * transaccion.cantidad

        return total_factura


class facturacrear (facturasbase):
    pass

class facturaeditar(SQLModel):
    fecha: str | None = None


class Factura (facturasbase, table= True):
    id: int | None = Field (default=None, primary_key=True) 
    cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuales NO en la BD
    clientes : cliente = Relationship(back_populates="factura")
    transacciones: list [Transaccion] = Relationship (back_populates="factura")

#craer modelo para mostrar usuario o cliente
class FacturaLeer(facturasbase):
    id: int 
    clientes: ClienteLeer

class facturaleercompuesta (FacturaLeer): 
    transacciones: list [Transaccion]= []  