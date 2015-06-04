# from builder import Builder


class Director():

    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        # Optimize: string arity
        self.__builder.make_title('Greeting')
        self.__builder.make_string('朝から昼にかけて')
        string = ['おはようございます', 'こんにちは。']
        self.__builder.make_items(string)
        self.__builder.make_string('夜に')
        string = ['こんばんは', 'おやすみなさい', 'さようなら']
        self.__builder.make_items(string)
        self.__builder.close()
