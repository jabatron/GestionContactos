from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator

class Contacto(BaseModel):
    nombre: str
    apellidos: str
    telefono: str
    mail: Optional[EmailStr] = None

    @field_validator('nombre')
    def nombre_no_vacio(cls, nombre):
        if not nombre.strip():
            raise ValueError('El nombre no puede estar vacío.')
        return nombre

    @field_validator('apellidos')
    def apellidos_no_vacios(cls, apellidos):
        if not apellidos.strip():
            raise ValueError('Los apellidos no pueden estar vacíos.')
        return apellidos

    @field_validator('telefono')
    def telefono_formato_valido(cls, telefono):
        telefono = ''.join(filter(str.isdigit, telefono))
        if not telefono:
            raise ValueError('El teléfono no puede estar vacío.')
        return telefono