import re
from typing import Optional

import requests
from PIL import Image

from chatbot import CommandDTO
from chatbot.ChatBot import ChatBot
import os
from dotenv import load_dotenv
import google.generativeai as genai

from chatbot.apiKey import returnKey


def checksForImgRequest(imgRequest, content_type):
    if imgRequest.status_code > 299:
        raise Exception("Image Not Found")

    if not content_type:
        raise Exception("Content-Type not found")

    # Check if the content type is an image
    if not content_type.startswith('image/'):
        raise Exception("Not an image format")
    return True

def imgHandler(imgURL):
    imgRequest = requests.get(imgURL.replace('\\/', '/'))
    content_type = imgRequest.headers.get('Content-Type')
    isValid = checksForImgRequest(imgRequest, content_type)

    file_extension = re.search(r'\.(jpg|png)', imgURL)  # e.g., "jpeg" from "image/jpeg"
    file_name = f"imgTMP{file_extension.group(0)}"

    with open(file_name, "wb") as f:
        f.write(imgRequest.content)
    print(f"Image saved as {file_name}")

    # Optional: Open the image for processing
    img = Image.open(file_name)

    return file_name


class Gemini(ChatBot):
    def getKey(self)->str:
        load_dotenv("API_KEY.env")
        return os.getenv("API_KEY") or returnKey()

    def create(self) -> 'Gemini':
        return Gemini()

    def generate_content(self, command: CommandDTO, sample_file: Optional[str] = None) -> str:
        model = genai.GenerativeModel("gemini-1.5-flash")
        try:
            content = f'''
            imagine que vc e um {command.role},
            usando esse tom {command.tone}
            limite de characters {command.limit}
            faca isto: {command.prompt}
            '''
            if sample_file:
                response = model.generate_content([content, sample_file])
            else:
                response = model.generate_content(content, generation_config=genai.GenerationConfig(
                    temperature=command.temperature))
            return response.text

        except Exception as e:
            print(e)
            raise e

    def readImg(self, command:CommandDTO):
        genai.configure(api_key=self.getKey())
        if command.imgURL is None:
            raise Exception("Image URL not provided")
        imgPath = imgHandler(command.imgURL)

        sample_file = genai.upload_file(path=imgPath, display_name="imgTMP")

        # Retrieve the file from GenAI
        file = genai.get_file(name=sample_file.name)

        # Generate content using the image
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

        try:
            response = self.generate_content(command, sample_file)
            return response
        except Exception as e:
            print(e)
            raise e

        finally:
            if sample_file:
                os.remove(imgPath)
                print("Tmp img removed")

    def generateText(self, command:CommandDTO) -> str:
        genai.configure(api_key=self.getKey())
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = self.generate_content(command)
        return response