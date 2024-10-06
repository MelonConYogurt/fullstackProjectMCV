from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from conexion_db_crud import *  # Importamos las funciones CRUD que ya tenemos
from fastapi import APIRouter

# Modelo de Producto para validar datos de entrada
class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    id_categoria: int

# Modelo de Producto para actualizar
class ProductoUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None
    precio: float = None
    id_categoria: int = None

productos = APIRouter(
    prefix= "/productos",
    tags=["Funciones apartado productos"]
)
    
# Crear producto
@productos.post("/productos/")
def crear_producto_api(producto: Producto):
    resultado = crear_producto(producto.nombre, producto.descripcion, producto.precio, producto.id_categoria)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"id_producto": resultado['id_producto'], "nombre": producto.nombre}

# Leer todos los productos
@productos.get("/productos/")
def obtener_productos():
    resultado = leer_productos()
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return resultado['productos']

# Actualizar producto
@productos.put("/productos/{id_producto}")
def actualizar_producto_api(id_producto: int, producto: ProductoUpdate):
    producto_actual = leer_productos()
    producto_datos = next((p for p in producto_actual['productos'] if p["id_producto"] == id_producto), None)
    
    if producto_datos is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Mantener los valores actuales si los campos no son proporcionados
    nombre = producto.nombre if producto.nombre else producto_datos["nombre"]
    descripcion = producto.descripcion if producto.descripcion else producto_datos["descripcion"]
    precio = producto.precio if producto.precio else producto_datos["precio"]
    id_categoria = producto.id_categoria if producto.id_categoria else producto_datos["id_categoria"]
    
    resultado = actualizar_producto(id_producto, nombre, descripcion, precio, id_categoria)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Producto actualizado correctamente"}

# Eliminar producto
@productos.delete("/productos/{id_producto}")
def eliminar_producto_api(id_producto: int):
    resultado = eliminar_producto(id_producto)
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['error'])
    return {"message": "Producto eliminado correctamente"}
