class RegisterNote(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RegisterNote, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

if __name__ == "__main__":
    rn = RegisterNote()
    rn2 = RegisterNote()
    rn.set_name("a")
    rn.set_name("b")
    print(id(rn))  # => 3074264748
    print(id(rn2))  # => 3074264748
    print(rn.get_name())  # => b
    print(rn.get_name())  # => b
    print(rn is rn2)  # => True
