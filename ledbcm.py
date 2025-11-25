import RPi.GPIO as GPIO
import time
def e1():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18,GPIO.OUT)
	r='S'
	while r in ['s','S']:
		for i in range (3):
			GPIO.output(18,True)
			time.sleep(1)
			GPIO.output(18,False)
			time.sleep(1)
		r=input("desea seguir? S/N:...")
		if r in ['n','N']:
			print ("SAliendo...")
			GPIO.cleanup()
			break
			return
