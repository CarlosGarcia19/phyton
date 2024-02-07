1print(***************************************")
2 print("Biienvenido a mi primera chamba PHYTON")
print（“***********************************"）
print("Ingresa tu nombre")
nombre=input()
if not nombre:
	print("No se ingreso nombre, favor de ingresarlo")
else:

	print("ingresa tu apellido paterno")
	apellidop=input()
	if not apellidop:
		print("No se ingreso apellidop, favor de ingresarlo")
	else:
	print("ingresa tu apellido materno")
	apellidon=input()
	print("ingresa tu correo")
	correo=input()
	if not correo:
		print("No se ingreso correo, favor de ingresarlo")
	else:
		print ("ingresa tu telefono")
		telefono=input()
		if not telefono:
			print ("No se ingreso telefono, No se puede terminar el proceso de inscripcion")
		else:	
			print ("Hola"+nombre+apellidoptapellidom+telefono+correo)