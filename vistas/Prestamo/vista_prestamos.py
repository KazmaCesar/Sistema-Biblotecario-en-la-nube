import ttkbootstrap as ttk
from datetime import datetime, timedelta

def mostrar(frame):
    # Limpiar frame
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="📖 Gestión de Préstamos", font=("Segoe UI", 20, "bold")).pack(pady=(20, 40))

    # Frame del formulario
    form = ttk.Frame(frame, padding=20)
    form.pack()

    # Campo: Matrícula del alumno
    ttk.Label(form, text="Matrícula del alumno:", font=("Segoe UI", 12)).grid(row=0, column=0, sticky="e", pady=10, padx=10)
    entry_matricula = ttk.Entry(form, width=40)
    entry_matricula.grid(row=0, column=1, pady=10, padx=10)

    # Campo: ID del libro
    ttk.Label(form, text="ID del libro:", font=("Segoe UI", 12)).grid(row=1, column=0, sticky="e", pady=10, padx=10)
    entry_libro = ttk.Entry(form, width=40)
    entry_libro.grid(row=1, column=1, pady=10, padx=10)

    # Separador visual
    ttk.Separator(form, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", pady=20)

    # Fecha actual y fecha de devolución (automáticas)
    fecha_prestamo = datetime.now().strftime("%d/%m/%Y")
    fecha_devolucion = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")

    ttk.Label(form, text="Fecha de préstamo:", font=("Segoe UI", 12)).grid(row=3, column=0, sticky="e", pady=10, padx=10)
    ttk.Label(form, text=fecha_prestamo, font=("Segoe UI", 12, "bold")).grid(row=3, column=1, sticky="w", pady=10, padx=10)

    ttk.Label(form, text="Fecha de devolución:", font=("Segoe UI", 12)).grid(row=4, column=0, sticky="e", pady=10, padx=10)
    ttk.Label(form, text=fecha_devolucion, font=("Segoe UI", 12, "bold")).grid(row=4, column=1, sticky="w", pady=10, padx=10)

    # Botón aceptar
    ttk.Button(frame, text="Aceptar", bootstyle="success", width=20).pack(pady=40)
