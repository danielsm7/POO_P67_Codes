
import telepot

class TelegramView:
    """
    Gestiona la comunicación de salida (saludos, respuestas, errores)
    mediante la API de Telegram (telepot).
    """
    def __init__(self, token):
        self.bot = telepot.Bot(token)

    def send_message(self, chat_id, message):
        """Envía el mensaje (respuesta) generado por el Controlador al chat."""
        # Se asegura de que la respuesta del Controlador llegue al usuario
        self.bot.sendMessage(chat_id, message)
        print("Os: ",message)
        
    def get_info(self):
        """Función de prueba de conexión."""
        return self.bot.getMe()