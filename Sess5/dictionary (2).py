import json
from mytranslate import mytranslate

data = json.load(open("data.json"))

w = input("Enter word: ")

out = mytranslate(w,data)

if type(out) == str:
	print(out)
	
else:
	i = 0
	for i, item in enumerate(out):
		print("{0}. {1}".format(i, item))

input("Press Enter to exit...")
