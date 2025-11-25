import time
import RPi.GPIO as GPIO

class robot:
    
    """ aqui solo va los ejecutables, ya sean funciones, 
    acciones y no tiene que ver con telegram"""     
    led=18
    boton=25
    def __init__(self):
        # El estado inicial del LED es 'apagado'
        self.state = "off" 
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.boton, GPIO.IN)
        GPIO.output(self.led, False)    
    def cleanup(self):
        GPIO.cleanup()
    def saludar(self):
        return "Hi, what can I help you?"
    def menu(self):
        return "great!!\nSelecciona:\nA)robot led.\nB)Robot Explorador.\nC)Robot Medico."
    def robot_led(self):
        res="Activando robot led"
        for i in range(7):
            GPIO.output(self.led, True) # Encender
            time.sleep(0.5)
            GPIO.output(self.led, False)  # Apagar
            time.sleep(0.5)
        # La respuesta a mostrar al usuario
        return (res,i) 

    def robot_explorador(self):
        res="hola soy robot explorador"
        k=0
        while k<150:
            if GPIO.input(self.boton):
                GPIO.output(self.led,False)
            else:
                GPIO.output(self.led,True)
                res="Explorando..."
                print("Explorando...")
            time.sleep(0.1)
            k+=1
        GPIO.output(self.led,False)
        # La respuesta a mostrar al usuario
        return (res,k/10)  
    def robot_medico(self):
        return "hola soy medico"
    def status(self):
        """Devuelve el estado actual del LED."""
        return f"Led is currently {self.state}"

# Si necesitas simular el encendido/apagado físico, iría aquí (ej. GPIO)
