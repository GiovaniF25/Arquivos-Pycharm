import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudem não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')
    print(site.read())   #aqui eu pego o conteudo html do site