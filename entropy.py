import numpy as np
import math

h = 0
k = 0

f = open("_clostridium_bolteae_90a9.Clos_bolt_90A9_V1.dna.nonchromosomal.fa","r")
if f.mode=='r':
	contents=f.read()
n = len(contents)
	
freq = np.zeros(256,dtype=np.int)
for i in range(0,n-1):        #last character is a null character
	if 0<=ord(contents[i])<=255:
		k = k + 1
		freq[ord(contents[i])] = freq[ord(contents[i])] + 1
y = freq/(k)
print("Number of ascii characters in the given file are " + str(k))
for i in range(0,len(freq)):
	try:
		h = h + (-y[i]*math.log(y[i],2))
	except ValueError:
		continue
print("Entropy of the distribution is " + str(h))
compression = k*(h/8)
print("optimal compression of file in bytes = "+str(compression))
