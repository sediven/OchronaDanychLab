#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4
import string
wszystkie=[]
for i in range(256):
	wszystkie.append(0)

tekst="""Atak brutalnej siły na kryptogram polega na systematycznym przetestowaniu całej przestrzeni możliwych kluczy. Przeprowadzenie ataku wymaga określenia jednoznacznego kryterium zakończenia. Algorytm musi umieć stwierdzić, czy kryptogram został odszyfrowany prawidłowo. Ogólną metodą odróżniania poprawnego odszyfrowania od przypadkowych wyników jest entropia. Tekst naturalny ma entropię znacząco niższą niż przypadkowy wynik odszyfrowania. Znając jednak charakter tekstu jawnego, można zaproponować znacznie prostsze rozwiązania."""



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

def permutationgenerator():
	for a in range(ord('a'),ord('z')):
		for b in range(ord('a'),ord('z')):
			for c in range(ord('a'),ord('z')):
				for d in range(ord('a'),ord('z')):
					#genertuj kluzc
					klucz=""
					klucz+=chr(a)+chr(b)+chr(c)+chr(d)
					
					#zdezsyfruj tekst kluczem
					cipher = ARC4.new(klucz)
					decrypted = cipher.decrypt(encrypted)
					#sprawdz entropie zdeszyfrowanego
					inicjacja(decrypted)
					if(entr()<5):
						return klucz
						


cipher = ARC4.new("baba")

encrypted = cipher.encrypt(tekst)

inicjacja(tekst)

h=entr()
print permutationgenerator()
