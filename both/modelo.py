import random
import time

import RPi.GPIO as GPIO
import adafruit_dht
import board


class Robot:
    led = 18
    boton = 25

    def __init__(self, nombre="Robot"):
        self.nombre = nombre
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.boton, GPIO.IN)


class RobotLed(Robot):
    def __init__(self, led_state=False):
        super().__init__(nombre="Robot Led")
        self.led_state = led_state
        GPIO.output(self.led, self.led_state)

    def set_state(self, state):
        self.led_state = state
        GPIO.output(self.led, state)

    def switch(self):
        for _ in range(5):
            GPIO.output(self.led, True)
            time.sleep(0.5)
            GPIO.output(self.led, False)
            time.sleep(0.5)

    def status(self):
        return f"LED encendido: {self.led_state}"


class RobotMedico(Robot):

    def __init__(self, nombre="Robot Medico"):
        super().__init__(nombre=nombre)
        self.dht_device = adafruit_dht.DHT11(board.D4)
    def medir_temperatura(self, tiempo):
        start = time.time()
        temperatura = None
        temperature_f = None

        while time.time() - start < tiempo:
            try:
                t = self.dht_device.temperature
                temperatura = t
                temperature_f = t * 9 / 5 + 32
            except RuntimeError:
                print("Error al leer la temperatura.")

            time.sleep(0.5)

        if temperatura is None:
            temperatura = 0.0
            temperature_f = 0.0

        return round(temperatura, 2), round(temperature_f, 2)

    def medir_humedad(self, tiempo):
        start = time.time()
        humedad = None
        while time.time() - start < tiempo:
            try:
                h = self.dht_device.humidity
                humedad = h
            except RuntimeError:
                print("Error al leer la humedad.")
        return round(humedad, 2)


class RobotExplorador(Robot):
    def robot_explorador(self, telegram_view, chat_id):
        k = 0
        while k < 15:
            k += 1
            telegram_view.send_message(chat_id, message=f"Explorando...")
            time.sleep(0.5)
        return k / 10

    def get_gpio(self):
        return GPIO

    def get_boton_pin(self):
        return self.boton

    def get_led_pin(self):
        return self.led
