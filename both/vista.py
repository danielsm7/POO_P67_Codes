
import telepot


class TelegramView:

    def __init__(self, token):
        self.bot = telepot.Bot(token)

    def send_message(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)
        print("Os: ",message)
        
    def get_info(self):
        """Función de prueba de conexión."""
        return self.bot.getMe()