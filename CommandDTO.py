class CommandDTO:
    def __init__(self, role: str="yourself", tone: str="neutral", prompt: str="random comment", limit = 150, temperature = 1, imgURL = None, history: list = None):
        self.__role = role
        self.__tone = tone
        self.__prompt = prompt
        self.__limit = limit
        self.__temperature = temperature
        self.__imgURL = imgURL
        self.__history = history

    @property
    def role(self) -> str:
        return self.__role

    @property
    def tone(self) -> str:
        return self.__tone

    @property
    def prompt(self) -> str:
        return self.__prompt

    @prompt.setter
    def prompt(self, value: str):
        self.__prompt = value

    @property
    def limit(self) -> int:
        return self.__limit
    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def imgURL(self) -> str:
        return self.__imgURL

    @property
    def history(self) -> list:
        return self.__history