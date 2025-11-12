
el sistema tiene implementadas las siguientes funciones:

Pantalla de inicio de sesión (login) con validación contra una base de datos en línea.

Diseño moderno usando la librería ttkbootstrap.

Conexión remota segura a una base de datos MySQL alojada en Hostinger.

Menú principal funcional con navegación lateral y vistas dinámicas.

Estructura modular (interfaz, menú, vistas, conexión).



integrar las funcionalidades completas de gestión de libros, usuarios y reportes.


Estructura del proyecto
sistema_prestamos/
│
├── conexion_bd.py
├── interfaz_login.py
├── logo.png
├── main.py
├── menu.py
├── opc_menu.py
├── README.md
├── .gitignore
│
└── vistas/
    ├── 
    │
    ├── Inicio/
    │   ├─
    │   └── vista_inicio.py
    │
    ├── Prestamo/
    │   
    │   └── vista_prestamos.py
    │
    └── Nuevo_prestamo/
        ├─
        └── vista_nprestamo.py


////////////////Requisitos////////////////
Python

Versión recomendada: Python 3.11 o superior

########  Librerías necesarias  ########

Ejecuta este comando para instalar todas las dependencias:

pip install ttkbootstrap requests mysql-connector-python


>>>>>>>>>Ejecución del sistema

1)Clona este repositorio en tu equipo:

git clone https://github.com/KazmaCesar/Sistema-Biblotecario-en-la-nube.git


2)Ingresa al directorio:

cd Sistema-Biblotecario-en-la-nube


3)Instala las librerías necesarias:

pip install -r requirements.txt


4) Ejecuta el programa:

python main.py