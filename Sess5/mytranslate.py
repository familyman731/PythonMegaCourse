from difflib import get_close_matches

def mytranslate (w,data):
	w = w.lower()
	
	if w in data.keys():
		return data[w]
		
	elif get_close_matches(w,data.keys()):
	
		m = get_close_matches(w,data.keys())[0]
		yn = input("Did you mean %s? (y or n)" % m).lower()
		
		if yn == 'y':
			return data[m]
			
		else:
			return "\nI don't know what you meant. Goodbye.\n"
			
	else:
		return "\nThat word does not exist in this dictionary. Goodbye.\n"
		