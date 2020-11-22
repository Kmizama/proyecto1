def funcion(x):
    return 2*x + 1
archivo =open("numeros.txt","r")
linea = archivo.readline()
print(linea)
while linea != "":
    linea = archivo.readline()
    y = funcion(linea)
    print(y)
archivo.close() 
