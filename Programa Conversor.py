import tkinter as tk
from tkinter import ttk


class ConversorLongitudElegante(tk.Tk):
    # Paleta de colores (Slate / Indigo Theme)
    COLOR_BG = "#0f172a"  # Slate 900
    COLOR_CARD = "#1e293b"  # Slate 800
    COLOR_BORDER = "#334155"  # Slate 700
    COLOR_TEXT_PRIMARY = "#f8fafc"  # Slate 50
    COLOR_TEXT_MUTED = "#94a3b8"  # Slate 400
    COLOR_ACCENT = "#6366f1"  # Indigo 500
    COLOR_RESULT_HIGHLIGHT = "#38bdf8"  # Sky Blue 400

    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana Principal
        self.title("Conversor de Longitud Pro")
        self.geometry("460x420")
        self.minsize(420, 390)
        self.configure(bg=self.COLOR_BG)

        # Matriz de Factores (respecto al Metro)
        self.FACTORES = {
            "Milímetros (mm)": 0.001,
            "Centímetros (cm)": 0.01,
            "Metros (m)": 1.0,
        }

        # 2. Configuración de Estilos TTK
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self._configurar_estilos()

        # 3. Construcción del Layout
        self._crear_interfaz()

    def _configurar_estilos(self):
        """Aplica una paleta de colores oscura, tipografía moderna y bordes limpios."""
        self.style.configure(".", background=self.COLOR_CARD)

        # Labels
        self.style.configure(
            "TLabel",
            background=self.COLOR_CARD,
            foreground=self.COLOR_TEXT_MUTED,
            font=("Segoe UI", 9, "bold"),
        )
        self.style.configure(
            "Title.TLabel",
            foreground=self.COLOR_TEXT_PRIMARY,
            font=("Segoe UI", 15, "bold"),
        )

        # Comboboxes
        self.style.configure(
            "TCombobox",
            fieldbackground=self.COLOR_BG,
            background=self.COLOR_BORDER,
            foreground=self.COLOR_TEXT_PRIMARY,
            arrowcolor=self.COLOR_TEXT_PRIMARY,
            bordercolor=self.COLOR_BORDER,
            lightcolor=self.COLOR_BORDER,
            darkcolor=self.COLOR_BORDER,
            padding=6,
        )
        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", self.COLOR_BG)],
            foreground=[("readonly", self.COLOR_TEXT_PRIMARY)],
            selectbackground=[("readonly", self.COLOR_BG)],
            selectforeground=[("readonly", self.COLOR_TEXT_PRIMARY)],
        )

        # Opción emergente del combobox (menú desplegable)
        self.option_add("*TCombobox*Listbox.background", self.COLOR_BG)
        self.option_add("*TCombobox*Listbox.foreground", self.COLOR_TEXT_PRIMARY)
        self.option_add(
            "*TCombobox*Listbox.selectBackground", self.COLOR_ACCENT
        )
        self.option_add(
            "*TCombobox*Listbox.selectForeground", self.COLOR_TEXT_PRIMARY
        )

    def _crear_interfaz(self):
        # Contenedor Principal (Efecto Tarjeta Flotante)
        card_frame = tk.Frame(
            self,
            bg=self.COLOR_CARD,
            bd=1,
            relief="flat",
            highlightbackground=self.COLOR_BORDER,
            highlightthickness=1,
        )
        card_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        card_frame.columnconfigure(0, weight=1)
        card_frame.columnconfigure(1, weight=1)

        # Cabecera
        lbl_titulo = ttk.Label(
            card_frame,
            text="Conversor de Longitud",
            style="Title.TLabel",
        )
        lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(20, 5), padx=20)

        lbl_subtitulo = ttk.Label(
            card_frame,
            text="Cálculo reactivo en tiempo real con tolerancia a fallos",
            font=("Segoe UI", 8),
            foreground=self.COLOR_TEXT_MUTED,
        )
        lbl_subtitulo.grid(
            row=1, column=0, columnspan=2, pady=(0, 20), padx=20
        )

        # RF-01: Campo de Entrada
        lbl_entrada = ttk.Label(card_frame, text="VALOR A CONVERTIR")
        lbl_entrada.grid(
            row=2, column=0, columnspan=2, sticky="w", padx=20, pady=(0, 4)
        )

        self.var_entrada = tk.StringVar()
        self.var_entrada.trace_add("write", lambda *args: self.calcular())

        self.entry_valor = tk.Entry(
            card_frame,
            textvariable=self.var_entrada,
            font=("Segoe UI", 12),
            bg=self.COLOR_BG,
            fg=self.COLOR_TEXT_PRIMARY,
            insertbackground=self.COLOR_TEXT_PRIMARY,
            bd=0,
            highlightbackground=self.COLOR_BORDER,
            highlightcolor=self.COLOR_ACCENT,
            highlightthickness=1,
            relief="flat",
        )
        self.entry_valor.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=20, ipady=8, pady=(0, 15)
        )
        self.entry_valor.focus()

        # RF-02: Desplegables Origen y Destino
        lbl_origen = ttk.Label(card_frame, text="DESDE")
        lbl_origen.grid(row=4, column=0, sticky="w", padx=(20, 5), pady=(0, 4))

        self.combo_origen = ttk.Combobox(
            card_frame,
            values=list(self.FACTORES.keys()),
            state="readonly",
            font=("Segoe UI", 9),
        )
        self.combo_origen.set("Centímetros (cm)")
        self.combo_origen.grid(
            row=5, column=0, sticky="ew", padx=(20, 5), pady=(0, 20)
        )
        self.combo_origen.bind(
            "<<ComboboxSelected>>", lambda e: self.calcular()
        )

        lbl_destino = ttk.Label(card_frame, text="HASTA")
        lbl_destino.grid(row=4, column=1, sticky="w", padx=(5, 20), pady=(0, 4))

        self.combo_destino = ttk.Combobox(
            card_frame,
            values=list(self.FACTORES.keys()),
            state="readonly",
            font=("Segoe UI", 9),
        )
        self.combo_destino.set("Metros (m)")
        self.combo_destino.grid(
            row=5, column=1, sticky="ew", padx=(5, 20), pady=(0, 20)
        )
        self.combo_destino.bind(
            "<<ComboboxSelected>>", lambda e: self.calcular()
        )

        # Panel de Resultado Destacado
        self.frame_resultado = tk.Frame(
            card_frame,
            bg=self.COLOR_BG,
            highlightbackground=self.COLOR_BORDER,
            highlightthickness=1,
        )
        self.frame_resultado.grid(
            row=6, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 15), ipady=10
        )

        lbl_res_tag = tk.Label(
            self.frame_resultado,
            text="RESULTADO",
            font=("Segoe UI", 8, "bold"),
            bg=self.COLOR_BG,
            fg=self.COLOR_TEXT_MUTED,
        )
        lbl_res_tag.pack(anchor="w", padx=15, pady=(5, 0))

        self.var_resultado = tk.StringVar(value="—")
        self.lbl_resultado = tk.Label(
            self.frame_resultado,
            textvariable=self.var_resultado,
            font=("Segoe UI", 16, "bold"),
            bg=self.COLOR_BG,
            fg=self.COLOR_TEXT_MUTED,
        )
        self.lbl_resultado.pack(anchor="w", padx=15, pady=(2, 5))

        # RF-04: Botón Limpiar con Estado Hover
        self.btn_limpiar = tk.Button(
            card_frame,
            text="Limpiar campos",
            command=self.limpiar,
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_BORDER,
            fg=self.COLOR_TEXT_PRIMARY,
            activebackground=self.COLOR_ACCENT,
            activeforeground="#ffffff",
            bd=0,
            cursor="hand2",
            relief="flat",
        )
        self.btn_limpiar.grid(
            row=7, column=0, columnspan=2, sticky="ew", padx=20, ipady=8, pady=(0, 20)
        )

        # Efectos Hover en el Botón
        self.btn_limpiar.bind(
            "<Enter>", lambda e: self.btn_limpiar.config(bg=self.COLOR_ACCENT)
        )
        self.btn_limpiar.bind(
            "<Leave>", lambda e: self.btn_limpiar.config(bg=self.COLOR_BORDER)
        )

    def calcular(self):
        """Lógica de conversión con tolerancia a fallos y formato limpio."""
        texto = self.var_entrada.get().strip()

        # RNF-01: Estado neutro si el campo está vacío
        if not texto:
            self.var_resultado.set("—")
            self.lbl_resultado.config(fg=self.COLOR_TEXT_MUTED)
            return

        # RF-01: Conversión de coma (,) a punto (.)
        texto_normalizado = texto.replace(",", ".")

        try:
            # RF-01: Conversión a float y valor absoluto
            valor = abs(float(texto_normalizado))

            origen = self.combo_origen.get()
            destino = self.combo_destino.get()

            factor_origen = self.FACTORES[origen]
            factor_destino = self.FACTORES[destino]

            # Lógica de Conversión
            valor_metros = valor * factor_origen
            resultado = valor_metros / factor_destino

            simbolo_destino = destino.split("(")[1].replace(")", "")

            # RF-03: Salida con precisión completa y resaltado de color
            val_fmt = int(resultado) if resultado.is_integer() else resultado
            self.var_resultado.set(f"{val_fmt} {simbolo_destino}")
            self.lbl_resultado.config(fg=self.COLOR_RESULT_HIGHLIGHT)

        except ValueError:
            # RNF-01: Estado neutro ante entradas no numéricas
            self.var_resultado.set("—")
            self.lbl_resultado.config(fg=self.COLOR_TEXT_MUTED)

    def limpiar(self):
        """RF-04: Restablece la entrada y el resultado."""
        self.var_entrada.set("")
        self.var_resultado.set("—")
        self.lbl_resultado.config(fg=self.COLOR_TEXT_MUTED)
        self.entry_valor.focus()


if __name__ == "__main__":
    app = ConversorLongitudElegante()
    app.mainloop()