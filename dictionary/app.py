import json
from difflib import get_close_matches
from pathlib import Path

class InteractiveDictionary:

    def __init__(self):
        cwd = Path.cwd()
        self.data = []
        for e in cwd.rglob('data.json'):
            self.data = json.load(open(e))
        if not self.data:
            raise FileNotFoundError("data.json file not found")

    def welcome_message(self):
        print("-----------Welcome to Interactive Dictionary--------------")

    def get_input(self):
        self.welcome_message()
        word = input("Please type in the word: ")
        output = self.translate(word.strip())
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

    def translate(self, w):
        w = w.lower()
        if w in self.data:
            return self.data[w]
        elif len(get_close_matches(w, self.data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, self.data.keys())[0])
            if yn == "Y":
                return self.data[get_close_matches(w, self.data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exist. Please double check it."

if __name__ == '__main__':
    app = InteractiveDictionary()
    app.get_input()