import json

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	else:
		print("The word doesn't exist. Please double check it.")

word = input("Enter your word: ")

print(translate(word))   

