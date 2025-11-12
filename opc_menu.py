import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from importlib import import_module

# mapea la opción a un módulo dentro del paquete "vistas"
RUTAS_VISTAS = {
    "inicio": "Inicio.vista_inicio",
    "nuevo_prestamo": "Nuevo_prestamo.vista_nprestamo",
    "devolucion": None,
    "prestamos": "vistas.nuevo_prestamo.vista_nprestamo",
    "libros": None,
    "usuarios": None,
    "reportes": None,
    "configuracion": None
}

def crear_opciones(frame_menu, frame_contenido):
    opciones = [
        ("🏠 Inicio", "inicio"),
        ("📗 Nuevo préstamo", "nuevo_prestamo"),
        ("🔁 Devolución", "devolucion"),
        ("📖 Préstamos", "prestamos"),
        ("📚 Libros", "libros"),
        ("👥 Usuarios", "usuarios"),
        ("📊 Reportes", "reportes"),
        ("⚙️ Configuración", "configuracion"),
    ]

    def mostrar_contenido(clave):
        for w in frame_contenido.winfo_children():
            w.destroy()

        ruta = RUTAS_VISTAS.get(clave)
        if ruta:
            try:
                modulo = import_module(f"vistas.{ruta}")
                if hasattr(modulo, "mostrar"):
                    modulo.mostrar(frame_contenido)
                    return
                else:
                    ttk.Label(frame_contenido, text=f"La vista '{ruta}' no define mostrar(frame).",
                              font=("Helvetica", 14, "bold")).pack(pady=20)
                    return
            except ModuleNotFoundError:
                ttk.Label(frame_contenido, text=f"Vista '{ruta}' no encontrada (ModuleNotFound).",
                          font=("Helvetica", 14, "bold")).pack(pady=20)
                return
            except Exception as e:
                ttk.Label(frame_contenido, text=f"Error al cargar la vista: {e}",
                          font=("Helvetica", 12)).pack(pady=10)
                return

        ttk.Label(frame_contenido, text=f"Vista: {clave.capitalize()} (en desarrollo)",
                  font=("Helvetica", 16, "bold")).pack(pady=20)
        ttk.Label(frame_contenido, text="Aquí irá el contenido de esta sección.",
                  font=("Helvetica", 12)).pack(pady=10)

    for texto, clave in opciones:
        ttk.Button(frame_menu, text=texto, bootstyle=SECONDARY,
                   command=lambda c=clave: mostrar_contenido(c)).pack(fill=X, pady=5)

    # Mostrar la vista de inicio por defecto si existe
    mostrar_contenido("inicio")
