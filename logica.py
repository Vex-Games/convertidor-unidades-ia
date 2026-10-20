import math

FACTORES = {"mm": 0.001, "cm": 0.01, "m": 1.0}

def convertir(texto, origen, destino):
    valor = float(texto.strip().replace(",", "."))
    if not math.isfinite(valor):
        raise ValueError("Introduce un número finito")
    if origen not in FACTORES or destino not in FACTORES:
        raise ValueError("Unidad desconocida")
    resultado = valor * FACTORES[origen] / FACTORES[destino]
    if not math.isfinite(resultado):
        raise ValueError("Resultado fuera de rango")
    return resultado
