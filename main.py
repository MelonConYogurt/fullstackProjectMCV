from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from conexion_db_crud import *
import uvicorn
from fastapi.responses import RedirectResponse

app = FastAPI()

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

# Endpoints CRUD para clientes
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Crear cliente
@app.post("/clientes/")
def crear_cliente(cliente: Cliente):
    resultado = crear_cliente(cliente.nombre, cliente.email, cliente.telefono)
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return resultado

# Leer todos los clientes
@app.get("/clientes/")
def obtener_clientes():
    resultado = leer_clientes()
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return resultado

# Actualizar cliente
@app.put("/clientes/{id_cliente}")
def actualizar_cliente(id_cliente: int, cliente: ClienteUpdate):
    # Obtenemos el cliente actual para poder aplicar solo los cambios
    cliente_actual = leer_clientes()
    cliente_datos = next((c for c in cliente_actual if c["id_cliente"] == id_cliente), None)

    if cliente_datos is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    nombre = cliente.nombre if cliente.nombre else cliente_datos["nombre"]
    email = cliente.email if cliente.email else cliente_datos["email"]
    telefono = cliente.telefono if cliente.telefono else cliente_datos["telefono"]

    resultado = actualizar_cliente(id_cliente, nombre, email, telefono)
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return resultado

# Eliminar cliente
@app.delete("/clientes/{id_cliente}")
def eliminar_cliente(id_cliente: int):
    resultado = eliminar_cliente(id_cliente)
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
    return resultado


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)