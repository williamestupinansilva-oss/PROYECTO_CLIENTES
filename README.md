PROYECTO_CLIENTES

API REST desarrollada con **FastAPI** para la administración de **Clientes**, **Facturas** y **Transacciones**, utilizando **SQLite** como base de datos.

Descripción

Este proyecto implementa un CRUD (Crear, Leer, Actualizar y Eliminar) para tres entidades principales:

- Clientes
- Facturas
- Transacciones

La aplicación está organizada siguiendo una estructura modular para facilitar su mantenimiento y escalabilidad.


Tecnologías utilizadas

- Python 3.12+
- FastAPI
- Uvicorn
- SQLite3
- Pydantic

Estructura del proyecto

PROYECTO_CLIENTES/
│
├── app/
│   ├── enrutadores/
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── factura.py
│   │   └── transaccion.py
│   │
│   ├── __init__.py
│   ├── conexion_BD.py
│   ├── listas.py
│   └── main.py
│
├── bd_clientes.sqlite3
├── requirements.txt
├── .gitignore
└── README.md


Descripción de carpetas

app/

Contiene todo el código fuente del proyecto.

enrutadores/

Aquí se encuentran los endpoints de la API.

- **clientes.py**
  - CRUD de clientes.

- **facturas.py**
  - CRUD de facturas.

- **transacciones.py**
  - CRUD de transacciones.

modelos/

Define los modelos de datos mediante Pydantic.

- cliente.py
- factura.py
- transaccion.py

Estos modelos validan la información recibida por la API.

conexion_BD.py

Se encarga de establecer la conexión con la base de datos SQLite.


listas.py

Archivo donde se manejan listas o funciones auxiliares utilizadas por la aplicación.

main.py

Archivo principal desde donde se inicia la API.

Base de datos

Se utiliza una base de datos SQLite llamada:

bd_clientes.sqlite3


En ella se almacenan:

- Clientes
- Facturas
- Transacciones

⚙ Instalación

1. Clonar el repositorio

bash
git clone https://github.com/TU-USUARIO/PROYECTO_CLIENTES.git

Entrar al proyecto

bash
cd PROYECTO_CLIENTES

2. Crear entorno virtual

Windows

bash
python -m venv venv


Activar el entorno

bash
venv\Scripts\activate


Linux/Mac

bash
python3 -m venv venv

source venv/bin/activate




3. Instalar dependencias

bash
pip install -r requirements.txt




4. Ejecutar el servidor

bash
uvicorn app.main:app --reload


Si el archivo principal está en otra ubicación:

bash
uvicorn main:app --reload

Acceder a la API

Una vez iniciada la aplicación:

Swagger

http://127.0.0.1:8000/docs


Redoc

http://127.0.0.1:8000/redoc



Funcionalidades

Clientes

- Crear cliente
- Consultar clientes
- Buscar cliente por ID
- Actualizar cliente
- Eliminar cliente


Facturas

- Crear factura
- Consultar facturas
- Buscar factura
- Actualizar factura
- Eliminar factura

Transacciones

- Crear transacción
- Consultar transacciones
- Buscar transacción
- Actualizar transacción
- Eliminar transacción


Dependencias

Las dependencias del proyecto se encuentran en:


requirements.txt


Instalarlas mediante:

bash
pip install -r requirements.txt

Ejemplo de ejecución

Iniciar servidor:

bash
uvicorn app.main:app --reload

Salida esperada:

INFO:     Uvicorn running on http://127.0.0.1:8000

Abrir en el navegador:


http://127.0.0.1:8000/docs


Autor

William Estupiñán Silva           Ficha= 3407180

