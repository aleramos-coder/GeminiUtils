from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
import google.generativeai as genai
from sympy.physics.units import temperature

from chatbot.apiKey import returnKey


class CommandDTO:
    def __init__(self, role: str, tone: str, prompt: str, limit = 150, temperature = 1):
        self.__role = role
        self.__tone = tone
        self.__prompt = prompt
        self.__limit = limit
        self.__temperature = temperature

    @property
    def role(self) -> str:
        return self.__role

    @property
    def tone(self) -> str:
        return self.__tone

    @property
    def prompt(self) -> str:
        return self.__prompt

    @property
    def limit(self) -> int:
        return self.__limit
    @property
    def temperature(self) -> float:
        return self.__temperature


class ChatBot(ABC):
    @abstractmethod
    def getKey(self)->str:
        pass
    @abstractmethod
    def create(self) -> 'ChatBot':
        pass

    @abstractmethod
    def generateText(self, command:CommandDTO)->str:
        pass

class Gemini(ChatBot):
    def getKey(self)->str:
        load_dotenv("API_KEY.env")
        return os.getenv("API_KEY") or returnKey()

    def create(self) -> 'Gemini':
        return Gemini()

    def generateText(self, command:CommandDTO) -> str:
        genai.configure(api_key=self.getKey())
        model = genai.GenerativeModel("gemini-1.5-flash")
        try:
            response = model.generate_content(f'''
            imagine you are a {command.role},
            using this tone {command.tone}
            characters limit {command.limit}
            do this: {command.prompt}
            ''', generation_config = genai.GenerationConfig(temperature = command.temperature))
            return response.text

        except Exception as e:
            print(e)
            raise e


class BotFactory:
    def getBot(self, type: str = "Gemini") -> ChatBot:
        if type.lower().strip() == "gemini":
            return Gemini().create()
        else:
            raise Exception("Bot implementation not found")



