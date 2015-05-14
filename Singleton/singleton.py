class Singleton():
    __instance = None

    def __new__(cls, *args, **keys):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
