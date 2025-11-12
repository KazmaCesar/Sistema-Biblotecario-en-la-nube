import ttkbootstrap as ttk

def mostrar(frame):
    ttk.Label(frame, text="📖 Gestión de Préstamos", font=("Segoe UI", 20, "bold")).pack(pady=30)
    ttk.Label(frame, text="Aquí se mostrarán los préstamos activos y podrás crear nuevos.",
              font=("Segoe UI", 12)).pack(pady=10)
