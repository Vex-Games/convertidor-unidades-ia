# SPEC · Conversor de longitudes
Versión 1 · 20/10/2026 · Estado: validada para la práctica

## Objetivo
Una aplicación de escritorio que convierta longitudes entre milímetros, centímetros y metros para hacer comprobaciones rápidas en clase.

## Usuario y entorno
Alumno de FP en Windows, Python 3.12/3.13 y CustomTkinter. Se ejecuta localmente. No necesita Internet después de instalar dependencias.

## Interfaz
Una ventana oscura con título Conversor de longitudes. Campo Valor con etiqueta visible; desplegable Origen y desplegable Destino, ambos con mm, cm y m. Botón Convertir, resultado destacado y botón Limpiar. Márgenes cómodos y controles legibles. Valor inicial vacío, origen mm, destino m y resultado —.

## Requisitos
- R1: Leer un número finito; admitir punto o coma decimal simple y espacios al principio/final. Sin separadores de miles. Admitir negativos.
- R2: Convertir entre mm, cm y m. Si las unidades coinciden, conservar el valor.
- R3: Mostrar el resultado y la unidad de destino. Presentar hasta 10 cifras significativas; no se exige aritmética decimal exacta.
- R4: Vacío, letras y valores no finitos muestran un error visible sin cerrar la ventana. Si el resultado desborda, mostrar error.
- R5: Limpiar vacía el campo, restablece mm → m, borra el resultado y devuelve el foco a Valor.
- R6: Separar la conversión en logica.py y la ventana en app.py. La lógica se puede probar sin abrir la GUI.

## Aceptación
| ID | Entrada | Origen | Destino | Esperado |
|---|---|---|---|---|
| A1 | 1000 | mm | m | 1 m |
| A2 | 2,5 | m | cm | 250 cm |
| A3 | -10 | cm | mm | -100 mm |
| A4 | 5 | cm | cm | 5 cm |
| A5 | vacío / hola / nan | mm | m | Mensaje de error |
| A6 | pulsar Limpiar | cualquiera | cualquiera | Estado inicial |

## Fuera de alcance
Sin mapas, robots reales, historial, ficheros de datos, nube, cuentas de usuario ni base de datos. No añadir Intercambiar todavía: será el primer issue.

## Pendientes y decisiones
El audio no especifica todos los errores ni el formato decimal. En la práctica, el alumno confirma las decisiones R1, R3 y R4 antes de programar. No atribuirlas al cliente si no las dijo.
