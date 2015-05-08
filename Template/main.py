from char_display import CharDisplay
from string_display import StringDisplay


if __name__ == '__main__':
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, World')
    d3 = StringDisplay('こんにちわ')

    d1.display()
    d2.display()
    d3.display()
