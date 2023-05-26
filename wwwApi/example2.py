from html.parser import HTMLParser
from urllib.request import urlopen, Request

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos += 1

    def num_polos(self):
        return self.n_polos

def getSource(url):
    headers = {
        'User-Agent': 'Mozzila/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req_url = "https:XXXX0000"
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()

html = getSource('https://univesp.br/cursos/engenharia-de-computacao')
parser = MyParser()
parser.feed(html)
print(parser.num_polos())
