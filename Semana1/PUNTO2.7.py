LITROS_POR_GALON= 3.785

litros_Producidos = int(input("Ingrese la cantidad de litros producidos: "))
precio_Por_Galon = int(input("Ingrese el precio por galón: "))

galones_Producidos = litros_Producidos / LITROS_POR_GALON

Pago = galones_Producidos * precio_Por_Galon

print(f"Usted recibirá ${Pago:.2f} por la producción del día.")

