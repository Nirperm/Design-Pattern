class HtmlWriter():

    def __init__(self, writer):
        self.__writer = writer

    def title(self, title):
        self.__writer.write('<!DOCTYPE html> \n')
        self.__writer.write('<html>')
        self.__writer.write('<head>')
        self.__writer.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> \n')
        self.__writer.write('<title>' + title + '</title>')
        self.__writer.write('</head>')
        self.__writer.write('<body> \n')
        self.__writer.write('<h1>' + title + '<h1> \n')

    def paragraph(self, msg):
        self.__writer.write('<p>' + msg + '</p>\n')

    def link(self, href, caption):
        self.paragraph('<a href=\'' + href + '\' >' + caption + '</a>')

    def mailto(self, mailaddr, username):
        self.link('mailto:' + mailaddr, username)

    def close(self):
        self.__writer.write('</body>')
        self.__writer.write('</html>\n')
        self.__writer.close()
