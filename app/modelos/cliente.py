from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class Clientebase(SQLModel):
    nombre: str = Field (default=None)
    email: str  = Field (default=None)
    descripcion: str | None = Field (default=None)

class clientecrear (Clientebase):
    pass
     

class clienteeditar (Clientebase):
    pass


class cliente (Clientebase, table= True):
    id: int | None = Field(default= None, primary_key= True)
    #relacion virtual con factura
    factura: list["Factura"] = Relationship (back_populates="clientes")

class ClienteLeer (Clientebase):
    id: int 