def huffmanDecode (dictionary, text):
	res = ""
	while text:
		for k in dictionary:
			if text.startswith(k):
				print(text)
				res += dictionary[k]
				text = text[len(k):]
	return res

text_1 = open('bacillus_trial.fa')
text=text_1.read()
print(text)
