
Nombre = input("Ingrese su nombre: ")
Dias = int(input("Ingrese los dias: "))
Salario = int(input("Ingrese el salario: "))


Prima = int(print(Salario*Dias/360))
Cesantia = int(print(Salario*Dias/360))
Interesescesantias = int(print(Cesantia*12))

print(f"Señor {Nombre} para los {Dias} días laborados y salario {Salario}, su liquidación se compone así:  prima {Salario* Dias / 360} cesantias {Salario* Dias / 360}  intereses cesantias {Cesantia*12/Dias}% ")


































