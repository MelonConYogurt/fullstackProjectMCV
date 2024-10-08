from fastapi import  HTTPException, APIRouter
from pydantic import BaseModel
from conexion_db_crud import *



clientes = APIRouter(
    prefix="/clientes",
    tags=["Funciones apartado clientes"]
)

# Modelo de Cliente para validar datos de entrada
class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: str

# Modelo de Cliente para actualizar (permite campos opcionales)
class ClienteUpdate(BaseModel):
    nombre: str = None
    email: str = None
    telefono: str = None

# Crear cliente
@clientes.post("/clientes/", response_model=Cliente)
def crear_cliente_api(cliente: Cliente):
    resultado = crear_cliente(cliente.nombre, cliente.email, cliente.telefono)
    if not resultado["success"]:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return {**cliente.dict(), "id_cliente": resultado["id_cliente"]}

# Leer todos los clientes
@clientes.get("/clientes/")
def obtener_clientes():
    resultado = leer_clientes()
    if not resultado["success"]:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return resultado["clientes"]

# Actualizar cliente
@clientes.put("/clientes/{id_cliente}")
def actualizar_cliente_api(id_cliente: int, cliente: ClienteUpdate):
    # Leemos todos los clientes para encontrar al cliente actual
    resultado_leer = leer_clientes()
    if not resultado_leer["success"]:
        raise HTTPException(status_code=400, detail=resultado_leer["error"])

    cliente_datos = next((c for c in resultado_leer["clientes"] if c["id_cliente"] == id_cliente), None)
    if cliente_datos is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Aplicamos los cambios solo a los campos actualizados
    nombre = cliente.nombre if cliente.nombre else cliente_datos["nombre"]
    email = cliente.email if cliente.email else cliente_datos["email"]
    telefono = cliente.telefono if cliente.telefono else cliente_datos["telefono"]

    resultado_actualizar = actualizar_cliente(id_cliente, nombre, email, telefono)
    if not resultado_actualizar["success"]:
        raise HTTPException(status_code=400, detail=resultado_actualizar["error"])
    return {"message": f"Cliente con ID {id_cliente} actualizado correctamente"}

# Eliminar cliente
@clientes.delete("/clientes/{id_cliente}")
def eliminar_cliente_api(id_cliente: int):
    resultado = eliminar_cliente(id_cliente)
    if not resultado["success"]:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return {"message": f"Cliente con ID {id_cliente} eliminado correctamente"}