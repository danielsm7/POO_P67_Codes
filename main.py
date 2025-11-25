
import os
import ledbcm as led
import pro2
import pro3
import pro4
def pro_1():
	led.e1()
	return
def pro_2():
	pro2.e2()
	return
def pro_3():
	print ("NO OLVIDE PRESIONAR EL BOTON !!")
	pro3.e3()
	return
def pro_4():
	print ("NO OLVIDE PRESIONAR EL BOTON!!")
	pro4.e4()
	return
while True:
	op=0
	os.system('cls')
	print ("hola, seleccione el proyecto a ejecutar:\n")
	print ("1)Led bcm 2)Led Board 3)Boton Bcm 4)boton Board")
	op=int(input("op=_"))
	if op==1:
		print ("***** LED CON BCM****\n")
		pro_1()
	if op==2:
		print ("*** LED CON BOARD***\n")
		pro_2()
	if op==3:
		print ("*** BOTON CON BCM***\n")
		pro_3()
	if op==4:
		print ("*** BOTON CON BOARD ***\n")
		pro_4()
	
	ss=input("Desea Salir del main? S/N: ")
	if ss in ["s","S"]:
		print ("Adios...")
		os.system('cls')
		break

