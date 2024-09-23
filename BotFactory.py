from chatbot import ChatBot
from chatbot.Gemini import Gemini


class BotFactory:
    def getBot(self, type: str = "Gemini") -> ChatBot:
        if type.lower().strip() == "gemini":
            return Gemini().create()
        else:
            raise Exception("Bot implementation not found")