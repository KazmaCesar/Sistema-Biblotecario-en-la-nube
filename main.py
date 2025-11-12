import ttkbootstrap as ttk
from interfaz_login import mostrar_login

if __name__ == "__main__":
    app = ttk.Window(themename="superhero")
    app.geometry("1000x600")
    app.title("Libreria TecNM")

    mostrar_login(app)

    app.mainloop()
