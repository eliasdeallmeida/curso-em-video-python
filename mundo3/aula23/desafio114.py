#  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    acessarSite = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('>>> ERRO: não foi possível acessar o site.')
else:
    print('>>> SUCESSO: o site está disponível.')
finally:
    print('Obrigado e volte sempre!')