import RPi.GPIO as GPIO
import time

def e4():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(22,GPIO.IN)
	j=0
	print ("Tiempo estimado de uso 10 seg...")
	while j<150:
		if GPIO.input(22):
			GPIO.output(12,False)
		else:
			GPIO.output(12,True)
		time.sleep(0.1)
		j+=1
	print ("Saliendo...")
	GPIO.cleanup()
	return
