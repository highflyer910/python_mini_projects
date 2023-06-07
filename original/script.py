import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data.json')

with open(file_path) as file:
    data = json.load(file)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    print("The word doesn't exist. Please double-check it.")

word = input("Enter your word: ")
print(translate(word))
