horas_Trabajadas_Por_Dia = int(input("Ingresa las horas trabajadas: "))
pago_Hora = int(input("Ingresa el pago por hora: "))


horas_Trabajadas_Semanal = (horas_Trabajadas_Por_Dia * 7)
Pago_Semanal = (horas_Trabajadas_Semanal * pago_Hora)

print(f"El pago semanal es: {Pago_Semanal:,}")