from fastapi import FastAPI
import uvicorn
from conexion_db_crud import *
from fastapi.responses import RedirectResponse
from router_categorias import categorias
from router_producto import productos
from router_pedidos import pedidos
from router_cliente import clientes

app = FastAPI()

app.include_router(categorias)
app.include_router(productos)
app.include_router(pedidos)
app.include_router(clientes)

# Endpoints CRUD para clientes
@app.get("/",tags=["Funciones varias"])
def read_root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) 