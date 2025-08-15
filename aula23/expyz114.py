# Crie um código em Python e teste se o site do 'Pudim' está acessível pelo computador usado
import urllib.request
from time import sleep

try:
    print('Tentando acessar o site do pudim...')
    site = urllib.request.urlopen('http://www.pudim.com.br/')
    sleep(1)
except:
    print('O site do pudim não está acessível no momento.')
else:
    print('O site do pudim foi acessado com sucesso!')
