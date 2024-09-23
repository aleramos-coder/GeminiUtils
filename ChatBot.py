from abc import ABC, abstractmethod

from CommandDTO import CommandDTO



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









