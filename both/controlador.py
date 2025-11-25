import time

from telepot.loop import MessageLoop

from archivo import interaccion
from modelo import Robot, RobotExplorador, RobotMedico, RobotLed
from vista import TelegramView

TOKEN = '8362589744:AAEmpqaxGP7aE9IW6v_MO_Km5v65R6fg-9o'
model = Robot()
explorador = RobotExplorador()
medico = RobotMedico()
led = RobotLed()
telegram_view = TelegramView(TOKEN)

running = True
estado_medico = None
estado_temperatura = None
estado_humedad = None


def action(msg):
    global estado_medico
    global estado_temperatura
    global estado_humedad
    chat_id = msg['chat']['id']
    command = msg['text'].lower()  # Convertir a minúsculas
    # envio mi comando a guardar en txt
    interaccion('Usuario', command)
    print("Telegram: ", command)
    if 'hola' in command:
        telegram_view.send_message(chat_id,
                                   "¡Hola! Soy tu Robot Asistente. ¿En qué puedo ayudarte hoy?, escribe 'menu' para ver las opciones.")
        interaccion("Bot",
                    "¡Hola! Soy tu Robot Asistente. ¿En qué puedo ayudarte hoy?, escribe 'menu' para ver las opciones.")
    elif 'menu' in command:
        menu = """
        Selecciona una opción:
            a) Robot Led
            b) Robot Explorador
            c) Robot Medico
        """
        telegram_view.send_message(chat_id, menu)
        interaccion("Bot", menu)
    elif command == 'a':
        telegram_view.send_message(chat_id, "Iniciando Robot Led...")
        interaccion("Bot", "Iniciando Robot Led...")
        led.switch()
        telegram_view.send_message(chat_id, "Se ha completado la secuencia del Robot Led.")
        interaccion("Bot", "Se ha completado la secuencia del Robot Led.")
    elif command == 'b':
        telegram_view.send_message(chat_id, "Iniciando Robot Explorador...")
        interaccion("Bot", "Iniciando Robot Explorador...")
        telegram_view.send_message(chat_id, "¡No olvide presionar el botón i para iniciar el recorrido!")
        interaccion("Bot", "¡No olvide presionar el botón para iniciar el recorrido!")
        while explorador.get_gpio().input(explorador.get_boton_pin()):
            time.sleep(0.1)

        explorador.get_gpio().output(explorador.get_led_pin(), True)
        k = explorador.robot_explorador(telegram_view, chat_id)

        telegram_view.send_message(chat_id, f"Exploración completada en {k} segundos.")
        interaccion("Bot", f"Exploración completada en {k} segundos.")

        explorador.get_gpio().output(explorador.get_led_pin(), False)

    elif command == 'c':
        telegram_view.send_message(chat_id, "Iniciando Robot Medico...")
        interaccion("Bot", "Iniciando Robot Medico...")
        time.sleep(1)

        menu_medico = """
        Selecciona una opción para el Robot Medico:
            t) Temperatura
            h) Humedad
        """
        telegram_view.send_message(chat_id, menu_medico)
        interaccion("Bot", menu_medico)
        estado_medico = "esperando_opcion"
    elif 'status' in command:
        estado = led.status()
        telegram_view.send_message(chat_id, estado)
    elif estado_medico == "esperando_opcion":
        if command == 't':
            telegram_view.send_message(chat_id, "Ingrese el tiempo de medicion:")
            interaccion("Bot", "Ingrese el tiempo de medicion:")
            estado_temperatura = "esperando_tiempo"
        elif command == 'h':
            telegram_view.send_message(chat_id, "Ingrese el tiempo de medición:")
            interaccion("Bot", "Ingrese el tiempo de medición:")
            estado_humedad = "esperando_tiempo"
        else:
            telegram_view.send_message(chat_id, "Opción incorrecta. Use t o h.")
            interaccion("Bot", "Opción incorrecta. Use t o h.")
        estado_medico = None
    elif estado_temperatura == "esperando_tiempo":
        try:
            tiempo = int(command)
            interaccion("Usuario", f"Tiempo de medición: {tiempo} segundos")
            telegram_view.send_message(chat_id, f"Midiendo temperatura durante {tiempo} segundos...")
            interaccion("Bot", f"Midiendo temperatura durante {tiempo} segundos...")
            t_c, t_f = medico.medir_temperatura(tiempo)
            telegram_view.send_message(chat_id, f"La temperatura medida es: {t_c} °C")
            telegram_view.send_message(chat_id, f"La temperatura medida es: {t_f} °F")
            interaccion("Bot", f"La temperatura medida es: {t_f} °F")
            interaccion("Bot", f"La temperatura medida es: {t_c} °C")
        except ValueError:
            telegram_view.send_message(chat_id, "Por favor, ingrese un número válido para el tiempo.")
            interaccion("Bot", "Por favor, ingrese un número válido para el tiempo.")
        estado_temperatura = None
    elif estado_humedad == "esperando_tiempo":
        try:
            tiempo = int(command)
            interaccion("Usuario", f"Tiempo de medición: {tiempo} segundos")
            telegram_view.send_message(chat_id, f"Midiendo humedad durante {tiempo} segundos...")
            interaccion("Bot", f"Midiendo humedad durante {tiempo} segundos...")
            time.sleep(tiempo)
            humedad = medico.medir_humedad(tiempo)
            telegram_view.send_message(chat_id, f"La humedad medida es: {humedad} %")
            interaccion("Bot", f"La humedad medida es: {humedad} %")
        except ValueError:
            telegram_view.send_message(chat_id, "Por favor, ingrese un número válido para el tiempo.")
            interaccion("Bot", "Por favor, ingrese un número válido para el tiempo.")
        estado_humedad = None
    elif command == 'adios':
        telegram_view.send_message(chat_id, "Adios!")
        interaccion("Bot", "Adios!")
        global running
        running = False

    else:
        telegram_view.send_message(chat_id, "Comando no reconocido. Por favor, escribe 'menu' para ver las opciones.")
        interaccion("Bot", "Comando no reconocido. Por favor, escribe 'menu' para ver las opciones.")


# ejecucion Principal
print(telegram_view.get_info())
print('Up and Running....')
MessageLoop(telegram_view.bot, action).run_as_thread()
while running:
    time.sleep(5)
