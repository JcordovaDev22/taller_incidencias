import logging

# Configuración básica de logs
logging.basicConfig(level=logging.ERROR, filename='app.log', filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def procesar_datos(lista):
    total = 0
    conteo_validos = 0
    
    for valor in lista:
        try:
            # Convertimos a float para manejar tanto números como strings numéricos
            total += float(valor)
            conteo_validos += 1
        except (TypeError, ValueError) as e:
            # Si el valor no es convertible, registramos el error y continuamos
            logging.error(f"Incidencia técnica: Valor no procesable '{valor}'. Detalle: {e}")
            continue
            
    # Retornamos el promedio solo si hay elementos válidos
    return total / conteo_validos if conteo_validos > 0 else 0

# Prueba con el dataset original
datos = [10, 20, "30", 40]
resultado = procesar_datos(datos)
print(f"Resultado final: {resultado}")