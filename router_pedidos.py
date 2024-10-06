from fastapi import HTTPException
from pydantic import BaseModel
from conexion_db_crud import *  # Importamos las funciones CRUD que ya tenemos
from fastapi import APIRouter


# Modelo de Pedido para validar datos de entrada
class Pedido(BaseModel):
    id_cliente: int
    total: float
    
pedidos = APIRouter()
    
pedidos = APIRouter(
prefix= "/pedidos",
tags=["Funciones apartadopedidos"]
)

# Crear pedido
@pedidos.post("/pedidos/")
def crear_pedido_api(pedido: Pedido):
    resultado = crear_pedido(pedido.id_cliente, pedido.total)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"id_pedido": resultado['id_pedido'], "id_cliente": pedido.id_cliente, "total": pedido.total}

# Leer todos los pedidos
@pedidos.get("/pedidos/")
def obtener_pedidos():
    resultado = leer_pedidos()
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return resultado['pedidos']

# Actualizar pedido
@pedidos.put("/pedidos/{id_pedido}")
def actualizar_pedido_api(id_pedido: int, pedido: Pedido):
    resultado = actualizar_pedido(id_pedido, pedido.id_cliente, pedido.total)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Pedido actualizado correctamente"}

# Eliminar pedido
@pedidos.delete("/pedidos/{id_pedido}")
def eliminar_pedido_api(id_pedido: int):
    resultado = eliminar_pedido(id_pedido)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Pedido eliminado correctamente"}
