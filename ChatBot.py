from abc import ABC, abstractmethod

class CommandDTO:
    def __init__(self, role: str, tone: str, prompt: str):
        self.__role = role
        self.__tone = tone
        self.__prompt = prompt

    @property
    def role(self) -> str:
        return self.__role

    @property
    def tone(self) -> str:
        return self.__tone

    @property
    def prompt(self) -> str:
        return self.__prompt

class ChatBot(ABC):
    @abstractmethod
    def create(self) -> 'ChatBot':
        pass

class Gemini(ChatBot):
    def create(self) -> 'Gemini':
        return Gemini()

class BotFactory:
    def getBot(self, type: str = "Gemini") -> ChatBot:
        if type.lower().strip() == "gemini":
            return Gemini().create()
        else:
            raise Exception("Bot implementation not found")

bot = BotFactory().getBot("Gemini")
print("Bot: ", bot.__class__.__name__)
