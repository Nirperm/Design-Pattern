import io


class HtmlWriter():

    def __init__(self, writer):
        self.__writer = io.StringIO(writer)

    def title(self, title):
        # IOException
        self.__writer.write('<html>')
        self.__writer.write('<head>')
        self.__writer.write('<title>' + self.title + '</title>')
        self.__writer.write('</head>')
        self.__writer.write('<body> \n')
        self.__writer.write('<h1>' + title + '<h1> \n')

    def paragraph(self, msg):
        # IOException
        self.__writer.write('<p>' + msg + '</p>\n')

    def link(self, href, caption):
        self.paragraph('<a href=\'' + href + '\' >' + caption + '</a>')

    def mailto(self, mailaddr, username):
        # IOException
        self.link('mailto:' + mailaddr + username)

    def close(self):
        # IOException
        self.__writer.write('</body>')
        self.__writer.write('</html>\n')
        self.__writer.close()
