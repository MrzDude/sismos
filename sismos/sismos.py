import matplotlib.pyplot as plt

def lee_datos(nombre):
    datos = []
    ar = open(nombre)
    for linea in ar:
        linea = linea.rstrip('\n')
        linea = linea.split(',')
        datos.append(linea)
    ar.close()
    return datos

def obtener_fecha_hora_mayor_sismo(datos):
    magnitud = 0
    fecha = ""
    hora = ""
    for dato in datos:
        magnitud_actual = float(dato[-2]) #accede a la mangitud a travez del penultimo elemento de la lista
        if(magnitud_actual > magnitud):
            magnitud = magnitud_actual
            fecha = dato[0]
            hora = dato[1] 
    return [fecha, hora]

def cantidad_por_rango(datos, limite_inferior, limite_superior):
    cantidad = 0
    for dato in datos:
        magnitud = float(dato[-2]) #accede a la mangitud a travez del penultimo elemento de la lista
        if(magnitud >= limite_inferior and magnitud < limite_superior):
            cantidad += 1
    return cantidad

def obtener_sismos_por_rango(datos):
    cantidades = []
    cantidades.append(cantidad_por_rango(datos, 7.0, 8.0))
    cantidades.append(cantidad_por_rango(datos, 8.0, 9.0))
    cantidades.append(cantidad_por_rango(datos, 9.0, 100.0))
    return cantidades

def cantidad_por_siglo(datos, siglo):
    cantidad = 0
    for dato in datos:
        siglo_actual = int(dato[0][6:8]) + 1 # Obtiene el siglo accediendo a los 2 primeros digitos del año y sumando 1
        if(siglo_actual == siglo):
            cantidad += 1
    return cantidad

def obtener_sismos_por_siglo(datos):
    siglos = [16, 17, 18, 19, 20, 21]
    cantidades = []
    for siglo in siglos:
        cantidad = cantidad_por_siglo(datos, siglo)
        cantidades.append(cantidad)
    return cantidades

def mostrar_fecha_hora_mayor_sismo(fecha_hora):
    print("Fecha:", fecha_hora[0], "y hora:", fecha_hora[1], "del mayor sismo registrado.","\n")

def mostrar_sismos_por_rango(sismos_por_rango):
    print("Cantidad de sismos >= 7.0 y < 8.0:", sismos_por_rango[0],"\n")
    print("Cantidad de sismos >= 8.0 y < 9.0:", sismos_por_rango[1],"\n")
    print("Cantidad de sismos >= 9.0:", sismos_por_rango[2],"\n")

def mostrar_sismos_por_siglo(sismos_por_siglo):
    siglos = [16,17,18,19,20,21]
    for i in range(len(siglos)):
        print("Cantidad de sismos siglo", str(siglos[i])+":", sismos_por_siglo[i],"\n")

def mostrar_grafico(sismos_por_siglo):
    x = [16, 17, 18, 19, 20, 21]
    y = sismos_por_siglo
    plt.title("Cantidad de sismos por siglo")
    plt.xlabel("Siglos")
    plt.ylabel("Cantidad de sismos")
    plt.bar(x, y)
    plt.show()

if __name__ == '__main__':
    datos = lee_datos('sismos.txt')

    fecha_hora_mayor_sismo = obtener_fecha_hora_mayor_sismo(datos)
    mostrar_fecha_hora_mayor_sismo(fecha_hora_mayor_sismo)

    sismos_por_rango = obtener_sismos_por_rango(datos)
    mostrar_sismos_por_rango(sismos_por_rango)

    sismos_por_siglo = obtener_sismos_por_siglo(datos)
    mostrar_sismos_por_siglo(sismos_por_siglo)
    mostrar_grafico(sismos_por_siglo)