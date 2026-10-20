import customtkinter as ctk
from logica import convertir

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Conversor de longitudes")
app.geometry("660x490")
app.minsize(600, 460)

def calcular():
    try:
        numero = convertir(entrada.get(), origen.get(), destino.get())
        resultado.configure(text=f"{numero:.10g} {destino.get()}", text_color="#6ee7b7")
    except ValueError:
        resultado.configure(text="Introduce un número válido y finito", text_color="#fca5a5")

def limpiar():
    entrada.delete(0, "end")
    origen.set("mm")
    destino.set("m")
    resultado.configure(text="—", text_color="#e2e8f0")
    entrada.focus_set()

ctk.CTkLabel(app,text="Conversor de longitudes",font=("Arial",28,"bold")).pack(pady=(30,15))
ctk.CTkLabel(app,text="Valor · coma o punto decimal").pack()
entrada = ctk.CTkEntry(app,width=320,height=42)
entrada.pack(pady=10)
fila = ctk.CTkFrame(app,fg_color="transparent")
fila.pack(pady=10)
ctk.CTkLabel(fila,text="Origen").grid(row=0,column=0,sticky="w",padx=15)
ctk.CTkLabel(fila,text="Destino").grid(row=0,column=1,sticky="w",padx=15)
origen = ctk.CTkOptionMenu(fila,values=["mm","cm","m"],width=180)
origen.grid(row=1,column=0,padx=15,pady=6)
destino = ctk.CTkOptionMenu(fila,values=["mm","cm","m"],width=180)
destino.grid(row=1,column=1,padx=15,pady=6)
destino.set("m")
ctk.CTkButton(app,text="Convertir",command=calcular,height=44,width=260).pack(pady=15)
resultado = ctk.CTkLabel(app,text="—",font=("Arial",25),wraplength=560)
resultado.pack(pady=10)
ctk.CTkButton(app,text="Limpiar",command=limpiar,fg_color="#334155").pack(pady=10)
app.mainloop()
