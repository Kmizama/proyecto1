def funcion(x):
    return 2*x + 1
archivo =open("numeros.txt","r")
archivo2 = open("resultado.txt","w")
lineas = archivo.readlines()
for linea in lineas:
    x = int(linea)
    y = funcion(x)
    print(y)
    y = str(y)
    archivo.write(y)
    archivo.write("\n")
archivo.close()
archivo2.close()

