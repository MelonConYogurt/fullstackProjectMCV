-- Tabla Clientes
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(150),
    telefono VARCHAR(15)
);

-- Tabla Categorias
CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Tabla Productos
CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    id_categoria INTEGER REFERENCES categorias(id_categoria)
);

-- Tabla Pedidos
CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_cliente INTEGER REFERENCES clientes(id_cliente),
    total DECIMAL(10,2)
);

-- Tabla Detalles_Pedido
CREATE TABLE detalles_pedido (
    id_detalle SERIAL PRIMARY KEY,
    id_pedido INTEGER REFERENCES pedidos(id_pedido),
    id_producto INTEGER REFERENCES productos(id_producto),
    cantidad INTEGER,
    precio_unitario DECIMAL(10,2)
);

