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