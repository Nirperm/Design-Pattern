import sys
from text_builder import TextBuilder
from html_builder import HTMLBuilder
from director import Director


def usage():
    print('Usage: Python main plain')
    print('Usage: Python main html')


def main():
    print(sys.argv[1])
    if len(sys.argv) != 2:
        usage()
        sys.exit()

    if sys.argv[1] == 'plain':
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)
    elif sys.argv[1] == 'html':
        html_builder = HTMLBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.get_result()
        print(filename + 'が作成されました。')
    else:
        usage()
        sys.exit()


if __name__ == "__main__":
    main()
