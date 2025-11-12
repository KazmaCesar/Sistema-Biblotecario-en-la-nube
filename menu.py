import ttkbootstrap as ttk
from opc_menu import crear_opciones

def abrir_menu(root, nombre, rol):
    for widget in root.winfo_children():
        widget.destroy()

    # Contenedor principal dividido en menú lateral y contenido
    frame_principal = ttk.Frame(root)
    frame_principal.pack(expand=True, fill="both")

    # Panel lateral (menú)
    frame_menu = ttk.Frame(frame_principal, padding=10)
    frame_menu.pack(side="left", fill="y")

    # Panel principal (contenido)
    frame_contenido = ttk.Frame(frame_principal, padding=20)
    frame_contenido.pack(side="right", expand=True, fill="both")

    # Título superior
    titulo = ttk.Label(frame_contenido, text="📚 Sistema de Préstamos de Libros",
                       font=("Segoe UI", 20, "bold"))
    titulo.pack(pady=(0, 20))

    # Datos del usuario
    ttk.Label(frame_contenido, text=f"Bienvenido {nombre}", font=("Segoe UI", 14)).pack(pady=5)
    ttk.Label(frame_contenido, text=f"Rol: {rol}", font=("Segoe UI", 12)).pack(pady=5)

    # Crear las opciones del menú lateral
    crear_opciones(frame_menu, frame_contenido)

    # Botón salir
    boton_salir = ttk.Button(frame_menu, text="Cerrar sesión",
                             bootstyle="danger", command=lambda: root.destroy())
    boton_salir.pack(side="bottom", fill="x", pady=10)

    root.title("Menú principal - Sistema de Préstamos de Libros")
