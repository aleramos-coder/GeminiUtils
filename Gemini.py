from chatbot import CommandDTO
from chatbot.ChatBot import ChatBot
import os
from dotenv import load_dotenv
import google.generativeai as genai

from chatbot.apiKey import returnKey


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