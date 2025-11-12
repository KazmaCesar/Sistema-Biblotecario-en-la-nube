import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from vistas import vista_inicio, vista_prestamos

def crear_opciones(frame_menu, frame_contenido):
    opciones = [
        ("🏠 Inicio", "inicio"),
        ("📗 Nuevo préstamo", "prestamo"),
        ("🔁 Devolución", "devolucion"),
        ("📖 Préstamos", "prestamos"),
        ("📚 Libros", "libros"),
        ("👥 Usuarios", "usuarios"),
        ("📊 Reportes", "reportes"),
        ("⚙️ Configuración", "configuracion"),
    ]

    def mostrar_contenido(nombre):
        for widget in frame_contenido.winfo_children():
            widget.destroy()
        if nombre == "inicio":
            vista_inicio.mostrar(frame_contenido)
        elif nombre == "prestamos":
            vista_prestamos.mostrar(frame_contenido)
        else:
            ttk.Label(frame_contenido, text=f"Vista: {nombre.capitalize()}",
                      font=("Helvetica", 16, "bold")).pack(pady=20)
            ttk.Label(frame_contenido, text="Aquí irá el contenido de esta sección.",
                      font=("Helvetica", 12)).pack(pady=10)

    for texto, nombre in opciones:
        ttk.Button(frame_menu, text=texto, bootstyle=SECONDARY,
                   command=lambda n=nombre: mostrar_contenido(n)).pack(fill=X, pady=5)

    mostrar_contenido("inicio")
