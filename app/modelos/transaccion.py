from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class transaccionbase (SQLModel):
    cantidad: int = Field(default=0)
    val_unitario: float = Field (default= 0.0)
    descripcion:  str  = Field (default=None)
    
    

class transaccioncrear(transaccionbase):
    pass

class transaccioneditar(SQLModel):
    cantidad: int | None = None
    val_unitario: float | None = None
    descripcion: str | None = None

class Transaccion (transaccionbase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field (default=None, foreign_key="factura.id")
    #aqui va la relacion virtual con el modelo factura (solo un campo)
    factura: list["Factura"] = Relationship (back_populates="transacciones")
    
#craer modelo para mostrar usuario o cliente
class transaccionleer (transaccionbase):
    id: int 