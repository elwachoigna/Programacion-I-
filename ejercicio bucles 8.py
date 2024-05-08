contador=0
cadena=input("Ingrese un texto")
vocal=["a","e"]
for i in range(1,len(cadena)):
    if cadena[i] in vocal:
        contador+=1
print (contador)
