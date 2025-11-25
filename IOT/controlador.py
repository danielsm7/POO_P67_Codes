import time
from telepot.loop import MessageLoop
from modelo import robot
from vista import TelegramView
from archivo import interaccion

TOKEN = '8370667380:AAFgHt21jrDzhvcramWpiojCpDaNsG2cf4s'
# Inicializa el Modelo y la Vista
model = robot()
telegram_view = TelegramView(TOKEN)
running = True
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower() # Convertir a minúsculas
    # envio mi comando a guardar en txt
    interaccion('Usuario', command)
    print("Telegram: ",command)
    respuesta= []
    if 'hola' in command:
        respuesta.append(model.saludar())
    elif 'menu' in command:
        respuesta.append(model.menu())
    elif command=='a':
        res, j = model.robot_led()
        respuesta.append(res)
        respuesta.append(f"j= {j}")
    elif command=='b':
        respuesta.append("¡No olvide presionar el botón!")
        # PASO 2: Llama al Modelo y desempaqueta la tupla
        res, k = model.robot_explorador()
        respuesta.append(res)
        respuesta.append(f"k= {k}")
    elif command=='c':
        respuesta.append(model.robot_medico())

    elif 'status' in command:
        respuesta.append(model.status())
    elif command == 'adios':
        # 1. Avisar al usuario
        respuesta.append(("¡Adiós! Cerrando el bot de forma segura...", 0))
        # 2. Registrar la salida
        for letra in respuesta:
            interaccion('Bot', letra)
            telegram_view.send_message(chat_id, letra)
        # 3. Señalizar el cierre
        global running
        running = False

    else:
        respuesta.append("Error. again, di 'hola'")

    # 3. como es lista, vamos a desglozar y queda mejor en telegram
    for letra in respuesta:
        # registro la salida tambien a mi archivo txt
        interaccion('Bot', letra)
        telegram_view.send_message(chat_id, letra)

# ejecucion Principal
print(telegram_view.get_info())
print('Up and Running....')
MessageLoop(telegram_view.bot, action).run_as_thread()

while running:
    time.sleep(5)