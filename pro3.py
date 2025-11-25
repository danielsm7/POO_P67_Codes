import RPi.GPIO as GPIO
import time

def e3():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18,GPIO.OUT)
	GPIO.setup(25,GPIO.IN)
	j=0
	print ("Tiempo estimado de uso 10 seg...")
	while j<150:
		if GPIO.input(25):
			GPIO.output(18,False)
		else:
			GPIO.output(18,True)
		time.sleep(0.1)
		j+=1
	print ("Saliendo...")
	GPIO.cleanup()
	return
