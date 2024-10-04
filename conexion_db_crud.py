import psycopg2

# Configuración de la conexión
def conectar():
    return psycopg2.connect(
        host="localhost", 
        database="ventas_online",  
        user="postgres",  
        password=12345  
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
        print(f"Cliente creado con ID: {id_cliente}")
    except Exception as e:
        print(f"Error al crear cliente: {e}")
        conn.rollback()
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
        for cliente in clientes:
            print(cliente)
    except Exception as e:
        print(f"Error al leer clientes: {e}")
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
        conn.commit()
        print(f"Cliente con ID {id_cliente} actualizado.")
    except Exception as e:
        print(f"Error al actualizar cliente: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Eliminar Cliente
def eliminar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s;", (id_cliente,))
        conn.commit()
        print(f"Cliente con ID {id_cliente} eliminado.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear cliente
    crear_cliente("Alejandro velez", "alejo@gmail.com", "12345226789")

    # Leer clientes
    leer_clientes()

    # Actualizar cliente
    actualizar_cliente(1, "Alejandro velez", "alejo@nuevoemail.com", "98761231254321")

    # Eliminar cliente
    eliminar_cliente(1)

