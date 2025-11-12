import ttkbootstrap as ttk

def mostrar(frame):
    ttk.Label(frame, text="🏠 Bienvenido al sistema", font=("Segoe UI", 20, "bold")).pack(pady=30)
    ttk.Label(frame, text="Desde aquí puedes gestionar préstamos, devoluciones y más.",
              font=("Segoe UI", 12)).pack(pady=10)
