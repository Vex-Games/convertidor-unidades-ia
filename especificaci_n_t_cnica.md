# Especificación Técnica (Spec-Driven) — Conversor de Longitud en Python

### 1. Visión General del Sistema
Aplicación de escritorio interactiva y responsiva desarrollada en Python para la conversión en tiempo real de unidades de longitud (milímetros, centímetros y metros). La aplicación garantiza máxima estabilidad frente a entradas inválidas y realiza ajustes automáticos de formato.

---

### 2. Requisitos Funcionales
* **RF-01 Entrada de Datos:**
  * Campo de texto reactivo para la entrada del valor numérico.
  * Admite números enteros y decimales usando tanto punto (`.`) como coma (`,`) como separador decimal.
  * Conversión automática de valores negativos a positivos mediante valor absoluto (`abs()`).
* **RF-02 Selección de Unidades:**
  * Desplegable de unidad de `Origen` con opciones: Milímetros (mm), Centímetros (cm), Metros (m). Valor por defecto: **cm**.
  * Desplegable de unidad de `Destino` con opciones: Milímetros (mm), Centímetros (cm), Metros (m). Valor por defecto: **m**.
* **RF-03 Reactividad y Cálculo:**
  * Cálculo instantáneo en tiempo real ante cualquier evento de teclado (ingreso/borrado) o cambio en los desplegables.
  * Salida con precisión completa de decimales, sin redondeos ni límites arbitrarios.
* **RF-04 Acción de Limpieza:**
  * Botón "Limpiar" para restablecer el campo de entrada a estado vacío y limpiar el resultado.

---

### 3. Requisitos No Funcionales y Resiliencia
* **RNF-01 Manejo de Errores (Tolerancia a Fallos):**
  * Ante textos no numéricos, símbolos o campos vacíos, la aplicación entra en estado neutro (muestra resultado vacío) sin lanzar excepciones ni cerrar la interfaz.
* **RNF-02 Interfaz de Usuario (UI):**
  * Desarrollada sobre la librería estándar `tkinter` / `ttk`.
  * Diseño limpio, centrado, accesible y responsivo al redimensionamiento de ventana.

---

### 4. Lógica de Conversión (Matriz de Factores a Metros)
$$\text{Factor}_{\text{mm}} = 0.001, \quad \text{Factor}_{\text{cm}} = 0.01, \quad \text{Factor}_{\text{m}} = 1.0$$

$$\text{Valor}_{\text{metros}} = |\text{Entrada}| \times \text{Factor}_{\text{origen}}$$

$$\text{Resultado} = \frac{\text{Valor}_{\text{metros}}}{\text{Factor}_{\text{destino}}}$$