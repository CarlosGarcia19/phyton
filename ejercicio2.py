print("*******************************")
print("Biienvenido a mi primera chamba PHYTON")
print("***************************")
print("Cuanto usuarios deseas registrar?")
valor=0
opcion =int(input())
if not opcion:
	print("no se ingreso dato")
else:
	valors=False
	for i in range(opcion):
		while (valors== False):
			print("Ingresa tu nombre")
			valor+=1
			nombre=input()
			if len(nombre)›=5 and len(nombre)<=50 :
				valors=True
				print("ingresa tu apellido paterno")
				apellidop=input()
				if len(apellidop) ›=5 and len(apellidop)<=50 :
					valors=True
					print("ingresa tu apellido materno")
					apellidom=input()
					if len(apellidom) >=5 and len(apellidom)<=50:
						valors=True
						print( "ingresa tu correo")
						correo=input()
						if len(correo)>=5 and len(correo)<=50 :
							valors=True
							print("ingresa tu telefono")
							telefono=input()
							if len（telefono）==10：
								valors=True
								print("Hola"+nombre+apellidop+apellidom+telefono+correo)
								if valor==opcion:
									print ("hasta luego")
								else:
									valors=False
							else:
								valors=False
								print("No se ingreso telefono, No se puede terminar el proceso de ingreso")
						else：
							valors=False
							print("No se ingreso correo, favor de ingresarlo")
					else:
						valors=False
						print("No se ingreso apellidomaterno, favor de ingresarlo")
				else:
					valors=False
					print("No se ingreso apellidopaterno, favor de ingresarlo")
			else:
				valors=False
				print("No se ingreso nombre correcto, favor de ingresarlo")