#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
wszystkie=[]
for i in range(256):
	wszystkie.append(0)

tekst="""Atak brutalnej siły na kryptogram polega na systematycznym przetestowaniu całej przestrzeni możliwych kluczy. Przeprowadzenie ataku wymaga określenia jednoznacznego kryterium zakończenia. Algorytm musi umieć stwierdzić, czy kryptogram został odszyfrowany prawidłowo. Ogólną metodą odróżniania poprawnego odszyfrowania od przypadkowych wyników jest entropia. Tekst naturalny ma entropię znacząco niższą niż przypadkowy wynik odszyfrowania. Znając jednak charakter tekstu jawnego, można zaproponować znacznie prostsze rozwiązania."""
tekst+=tekst


def inicjacja(tekst):
	for i in range(256):
		wszystkie.append(0)
	for c in tekst:
	        wszystkie[ord(c)]+=1

import math
def log2(x):
	if(x>0):
		return math.log(x)/math.log(2)
	else :
		return 0

def entr():
	h=0
	for i in range(256):
		wszystkie[i]=wszystkie[i]/float(len(tekst))
	for i in range(256):
		h+=(wszystkie[i]*log2(wszystkie[i]))
	return -h



from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes

klucz = "zaq12wsxZAQ!@WSX"
iv = get_random_bytes(8)

descbc = DES.new(klucz[:8], DES.MODE_CBC, iv)
encrypted = descbc.encrypt(tekst)
inicjacja(encrypted)
print "DES CBC"
print entr()

desebc = DES.new(klucz[:8], DES.MODE_ECB)
encrypted = desebc.encrypt(tekst)

inicjacja(encrypted)
print "DES ECB"
print entr()

IV = get_random_bytes(16)
aescbc = AES.new(klucz, AES.MODE_CBC, IV)
encrypted = aescbc.encrypt(tekst[:(len(tekst)/16*16)])
inicjacja(encrypted)
print "AES CBC"
print entr()

aesecb = AES.new(klucz, AES.MODE_ECB, IV)
encrypted = aesecb.encrypt(tekst[:(len(tekst)/16*16)])
inicjacja(encrypted)
print "AES ECB"
print entr()


inicjacja(tekst)

h = entr()
