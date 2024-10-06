from fastapi import  HTTPException
from pydantic import BaseModel
from conexion_db_crud import *  # Importamos las funciones CRUD que ya tenemos
from fastapi import APIRouter

categorias = APIRouter(
    prefix= "/categorias",
    tags=["Funciones apartado categorias"]
)

# Modelo de Categoría para validar datos de entrada
class Categoria(BaseModel):
    nombre: str

# Modelo de Categoría para actualizar
class CategoriaUpdate(BaseModel):
    nombre: str = None

# Crear categoría
@categorias.post("/categorias/")
def crear_categoria_api(categoria: Categoria):
    resultado = crear_categoria(categoria.nombre)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"id_categoria": resultado['id_categoria'], "nombre": categoria.nombre}

# Leer todas las categorías
@categorias.get("/categorias/")
def obtener_categorias():
    resultado = leer_categorias()
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return resultado['categorias']

# Actualizar categoría
@categorias.put("/categorias/{id_categoria}")
def actualizar_categoria_api(id_categoria: int, categoria: CategoriaUpdate):
    resultado = actualizar_categoria(id_categoria, categoria.nombre)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Categoría actualizada correctamente"}

# Eliminar categoría
@categorias.delete("/categorias/{id_categoria}")
def eliminar_categoria_api(id_categoria: int):
    resultado = eliminar_categoria(id_categoria)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Categoría eliminada correctamente"}
