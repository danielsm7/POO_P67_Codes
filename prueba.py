import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

class RP:
	def __init__(self,pin, modo):
		self.modo=modo
		self.pin=pin
	def ejecutar(k):
		r='S'
		while r in ['s','S']:
			for i in range (3):
				GPIO.output(k,True)
				time.sleep(1)
				GPIO.output(k,False)
				time.sleep(1)
			r=input("desea seguir?  S/N...")
			if r in ['n','N']:
				time.sleep(1)
				print ("Saliendo.....")
				GPIO.cleanup
				break
				return

	op=input("selecione: A)BCM B)BOARD  __")
	if op in ['a','A']:
		print("led con BCM")
		k=18
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(k,GPIO.OUT)
		ejecutar(k)
	if op in['B','b']:
		print("led con BOARD")
		k=12 
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(k,GPIO.OUT)
		ejecutar(k)
