import math

def menu_inicio():
    print("Menu Inicio:")
    print("1. Ingresar números")
    print("2. Cargar números desde 'datos.txt'")
    print("3. Salir")

def obtener_datos():
    entrada = input("Ingrese un conjunto de datos separados por espacios: ")
    datos = list(map(float, entrada.split()))
    return datos

def guardar_datos(datos, resultados):
    try:
        with open("datos.txt", "w") as archivo:
            archivo.write("Datos iniciales:\n")
            for dato in datos:
                archivo.write(str(dato) + "\n")
            archivo.write("\nResultados de cálculos:\n")
            if "media" in resultados:
                archivo.write("Media: {}\n".format(resultados["media"]))
            if "mediana" in resultados:
                archivo.write("Mediana: {}\n".format(resultados["mediana"]))
            if "moda" in resultados:
                archivo.write("Moda: {}\n".format(resultados["moda"]))
            if "rango" in resultados:
                archivo.write("Rango: {}\n".format(resultados["rango"]))
            if "desviacion_estandar" in resultados:
                archivo.write("Desviación estándar: {}\n".format(resultados["desviacion_estandar"]))
        print("Datos guardados correctamente en 'datos.txt'")
    except IOError:
        print("Error: No se pudo guardar los datos.")

def cargar_datos():
    datos = []
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                # Attempt to convert the line to float
                try:
                    dato = float(linea.strip())
                    datos.append(dato)
                except ValueError:
                    print(f"Advertencia: Ignorando valor no numérico en línea: {linea.strip()}")
        print("Datos cargados correctamente desde 'datos.txt'")
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")
    return datos


def calcular_media(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        return (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    else:
        return datos_ordenados[n // 2]

def calcular_moda(datos):
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    moda_frecuencia = max(frecuencias.values())
    moda = [dato for dato, frecuencia in frecuencias.items() if frecuencia == moda_frecuencia]
    return moda

def calcular_rango(datos):
    return max(datos) - min(datos)

def calcular_desviacion_estandar(datos):
    media = calcular_media(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(suma_cuadrados / len(datos))
    return desviacion_estandar

def menu():
    print("1. Calcular media")
    print("2. Calcular mediana")
    print("3. Calcular moda")
    print("4. Calcular rango")
    print("5. Calcular desviación estándar")
    print("6. Guardar datos en archivo")
    print("7. Cargar datos desde archivo")
    print("8. Salir")

def main():
    datos = []
    resultados = {}
    while True:
        menu_inicio()
        opcion_inicio = input("Seleccione una opción del Menu Inicio: ")
        if opcion_inicio == "1":
            datos = obtener_datos()
            break
        elif opcion_inicio == "2":
            datos = cargar_datos()
            break
        elif opcion_inicio == "3":
            print("¡Hasta luego!")
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            resultados["media"] = calcular_media(datos)
            print("La media es:", resultados["media"])
        elif opcion == "2":
            resultados["mediana"] = calcular_mediana(datos)
            print("La mediana es:", resultados["mediana"])
        elif opcion == "3":
            resultados["moda"] = calcular_moda(datos)
            print("La moda es:", resultados["moda"])
        elif opcion == "4":
            resultados["rango"] = calcular_rango(datos)
            print("El rango es:", resultados["rango"])
        elif opcion == "5":
            resultados["desviacion_estandar"] = calcular_desviacion_estandar(datos)
            print("La desviación estándar es:", resultados["desviacion_estandar"])
        elif opcion == "6":
            guardar_datos(datos, resultados)
        elif opcion == "7":
            datos = cargar_datos()
            if datos:
                print("Datos cargados:", datos)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

