from string_display import StringDisplay
from side_border import SideBorder
from full_border import FullBorder


def main():
    b1 = StringDisplay('Hello, world')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay('こんにちは。')
                    ), '*'
                )
            )
        ), '/'
    )

    b1.show()
    b2.show()
    b3.show()
    b4.show()

if __name__ == "__main__":
    main()
