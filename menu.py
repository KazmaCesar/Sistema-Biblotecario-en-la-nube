import ttkbootstrap as ttk
from opc_menu import crear_opciones

def abrir_menu(root, nombre, rol):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Menú principal - Sistema de Préstamos de Libros")

    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    frame_menu = ttk.Frame(main_frame, width=250, padding=20)
    frame_menu.pack(side="left", fill="y")

    frame_contenido = ttk.Frame(main_frame, padding=20)
    frame_contenido.pack(side="right", fill="both", expand=True)

    ttk.Label(frame_menu, text=f"👋 Bienvenido, {nombre}", font=("Segoe UI", 12, "bold")).pack(pady=(0,10))
    ttk.Label(frame_menu, text=f"Rol: {rol}", font=("Segoe UI", 10)).pack(pady=(0,20))

    crear_opciones(frame_menu, frame_contenido)

    def cerrar_sesion():
        from interfaz_login import mostrar_login
        mostrar_login(root)

    ttk.Button(frame_menu, text="🚪 Cerrar sesión", bootstyle="danger",
               command=cerrar_sesion).pack(side="bottom", fill="x", pady=10)
