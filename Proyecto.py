nombreVendedor = input("Indica tu nombre: ")
totalVentas = input("Indica cuanto has vendido este mes: ")

comisiones = float(totalVentas)

resultado = 18 * comisiones / 100

print("Esto es lo que recibiras en comisiones: "+str(resultado))