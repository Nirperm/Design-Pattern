from string_display import StringDisplay
from side_border import SideBorder
from full_border import FullBorder


if __name__ == '__main__':
    b1 = StringDisplay('Hello, world')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)

    b1.show()
    b2.show()
    b3.show()
