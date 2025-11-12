import ttkbootstrap as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
import threading
from menu import abrir_menu

def verificar_login(usuario, contrasena, callback):
    url = "https://lightslategrey-nightingale-978510.hostingersite.com/login.php"
    try:
        data = {"usuario": usuario, "contrasena": contrasena}
        response = requests.post(url, data=json.dumps(data))
        print("📩 Respuesta del servidor:\n", response.text)
        result = response.json()

        if result.get("status") == "ok":
            callback(True, result.get("rol"), result.get("nombre"))
        else:
            messagebox.showerror("Error", result.get("message", "Error desconocido."))
            callback(False, None, None)

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "No hay conexión a Internet o el servidor no responde.")
        callback(False, None, None)
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")
        callback(False, None, None)


def mostrar_login(root):
    root.geometry("1000x600")
    for widget in root.winfo_children():
        widget.destroy()

    contenedor = ttk.Frame(root, padding=40)
    contenedor.pack(expand=True, fill="both")

    # Configurar diseño en 2 columnas
    contenedor.columnconfigure(0, weight=1)
    contenedor.columnconfigure(1, weight=1)

    # ==== 🧾 Sección izquierda: formulario ====
    frame_form = ttk.Frame(contenedor, padding=40)
    frame_form.grid(row=0, column=0, sticky="nsew")

    titulo = ttk.Label(frame_form, text="📚 Libreria Tecnm-Milpa alta", font=("Segoe UI", 26, "bold"))
    titulo.pack(pady=(0, 50))

    usuario_label = ttk.Label(frame_form, text="Usuario:", font=("Segoe UI", 14))
    usuario_label.pack(pady=5)
    usuario_entry = ttk.Entry(frame_form, width=40, font=("Segoe UI", 12))
    usuario_entry.pack(pady=5, ipady=5)

    contrasena_label = ttk.Label(frame_form, text="Contraseña:", font=("Segoe UI", 14))
    contrasena_label.pack(pady=5)
    contrasena_entry = ttk.Entry(frame_form, show="*", width=40, font=("Segoe UI", 12))
    contrasena_entry.pack(pady=5, ipady=5)

    cargando_label = ttk.Label(frame_form, text="", font=("Segoe UI", 11))
    cargando_label.pack(pady=10)

    def iniciar_sesion():
        usuario = usuario_entry.get().strip()
        contrasena = contrasena_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning("Advertencia", "Por favor ingrese usuario y contraseña.")
            return

        cargando_label.config(text="🔄 Verificando credenciales...")
        boton.config(state="disabled")

        def on_result(valido, rol, nombre):
            cargando_label.config(text="")
            boton.config(state="normal")
            if valido:
                abrir_menu(root, nombre, rol)

        threading.Thread(target=verificar_login, args=(usuario, contrasena, on_result), daemon=True).start()

    boton = ttk.Button(frame_form, text="Iniciar Sesión", bootstyle="success", width=30, command=iniciar_sesion)
    boton.pack(pady=30)

    # ==== 🖼️ Sección derecha: logotipo ====
    frame_logo = ttk.Frame(contenedor)
    frame_logo.grid(row=0, column=1, sticky="nsew")
    frame_logo.rowconfigure(0, weight=1)
    frame_logo.columnconfigure(0, weight=1)

    try:
        # Coloca la ruta de tu imagen (por ejemplo: "logo.png" en la misma carpeta)
        imagen = Image.open("logo.png")
        imagen = imagen.resize((370, 300), Image.LANCZOS)
        logo_img = ImageTk.PhotoImage(imagen)
        logo_label = ttk.Label(frame_logo, image=logo_img)
        logo_label.image = logo_img
        logo_label.grid(row=0, column=0, sticky="nsew")
    except Exception as e:
        ttk.Label(frame_logo, text="(No se encontró el logo)", font=("Segoe UI", 12, "italic")).grid(row=0, column=0, sticky="nsew")

    root.title("Inicio de sesión - Sistema de Préstamos de Libros")
