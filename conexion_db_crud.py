import psycopg2

# Configuración de la conexión
def conectar():
    return psycopg2.connect(
        host="localhost", 
        database="ventas_online",  
        user="postgres",  
        password="12345"  
    )

# Crear Cliente
def crear_cliente(nombre, email, telefono):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clientes (nombre, email, telefono)
            VALUES (%s, %s, %s)
            RETURNING id_cliente;
        """, (nombre, email, telefono))
        id_cliente = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id_cliente": id_cliente}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Leer Clientes
def leer_clientes():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes;")
        clientes = cursor.fetchall()
        # Convertir a diccionario para mejor manejo en la API
        clientes_dict = [
            {"id_cliente": cliente[0], "nombre": cliente[1], "email": cliente[2], "telefono": cliente[3]}
            for cliente in clientes
        ]
        return {"success": True, "clientes": clientes_dict}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Actualizar Cliente
def actualizar_cliente(id_cliente, nombre, email, telefono):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE clientes
            SET nombre = %s, email = %s, telefono = %s
            WHERE id_cliente = %s;
        """, (nombre, email, telefono, id_cliente))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Cliente no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Eliminar Cliente
def eliminar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s;", (id_cliente,))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Cliente no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


## Categorias

# Crear Categoría
def crear_categoria(nombre):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO categorias (nombre)
            VALUES (%s)
            RETURNING id_categoria;
        """, (nombre,))
        id_categoria = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id_categoria": id_categoria}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Leer Categorías
def leer_categorias():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM categorias;")
        categorias = cursor.fetchall()
        categorias_dict = [{"id_categoria": categoria[0], "nombre": categoria[1]} for categoria in categorias]
        return {"success": True, "categorias": categorias_dict}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Actualizar Categoría
def actualizar_categoria(id_categoria, nombre):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE categorias
            SET nombre = %s
            WHERE id_categoria = %s;
        """, (nombre, id_categoria))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Categoría no encontrada"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Eliminar Categoría
def eliminar_categoria(id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM categorias WHERE id_categoria = %s;", (id_categoria,))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Categoría no encontrada"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


### productos


# Crear Producto
def crear_producto(nombre, descripcion, precio, id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, precio, id_categoria)
            VALUES (%s, %s, %s, %s)
            RETURNING id_producto;
        """, (nombre, descripcion, precio, id_categoria))
        id_producto = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id_producto": id_producto}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Leer Productos
def leer_productos():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos;")
        productos = cursor.fetchall()
        productos_dict = [
            {"id_producto": producto[0], "nombre": producto[1], "descripcion": producto[2], "precio": producto[3], "id_categoria": producto[4]}
            for producto in productos
        ]
        return {"success": True, "productos": productos_dict}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Actualizar Producto
def actualizar_producto(id_producto, nombre, descripcion, precio, id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s
            WHERE id_producto = %s;
        """, (nombre, descripcion, precio, id_categoria, id_producto))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Producto no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Eliminar Producto
def eliminar_producto(id_producto):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE id_producto = %s;", (id_producto,))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Producto no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


### Pedidos:

# Crear Pedido
def crear_pedido(id_cliente, total):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pedidos (id_cliente, total)
            VALUES (%s, %s)
            RETURNING id_pedido;
        """, (id_cliente, total))
        id_pedido = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id_pedido": id_pedido}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Leer Pedidos
def leer_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM pedidos;")
        pedidos = cursor.fetchall()
        pedidos_dict = [
            {"id_pedido": pedido[0], "fecha_pedido": pedido[1], "id_cliente": pedido[2], "total": pedido[3]}
            for pedido in pedidos
        ]
        return {"success": True, "pedidos": pedidos_dict}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Actualizar Pedido
def actualizar_pedido(id_pedido, id_cliente, total):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE pedidos
            SET id_cliente = %s, total = %s
            WHERE id_pedido = %s;
        """, (id_cliente, total, id_pedido))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Pedido no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Eliminar Pedido
def eliminar_pedido(id_pedido):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s;", (id_pedido,))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Pedido no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


## detalles pedidos

# Crear Detalle de Pedido
def crear_detalle_pedido(id_pedido, id_producto, cantidad, precio_unitario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, %s)
            RETURNING id_detalle;
        """, (id_pedido, id_producto, cantidad, precio_unitario))
        id_detalle = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id_detalle": id_detalle}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Leer Detalles de Pedido
def leer_detalles_pedido():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM detalles_pedido;")
        detalles = cursor.fetchall()
        detalles_dict = [
            {"id_detalle": detalle[0], "id_pedido": detalle[1], "id_producto": detalle[2], "cantidad": detalle[3], "precio_unitario": detalle[4]}
            for detalle in detalles
        ]
        return {"success": True, "detalles": detalles_dict}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Actualizar Detalle de Pedido
def actualizar_detalle_pedido(id_detalle, id_pedido, id_producto, cantidad, precio_unitario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE detalles_pedido
            SET id_pedido = %s, id_producto = %s, cantidad = %s, precio_unitario = %s
            WHERE id_detalle = %s;
        """, (id_pedido, id_producto, cantidad, precio_unitario, id_detalle))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Detalle no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()

# Eliminar Detalle de Pedido
def eliminar_detalle_pedido(id_detalle):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM detalles_pedido WHERE id_detalle = %s;", (id_detalle,))
        if cursor.rowcount == 0:
            return {"success": False, "error": "Detalle no encontrado"}
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()
