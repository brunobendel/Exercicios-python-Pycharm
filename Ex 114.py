import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('Deu Ruim o Site não está funcionando')
else:
    print('Esse site está disponivel.')
    print(site.read())