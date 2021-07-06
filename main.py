import json
from difflib import get_close_matches

data = json.load(open('data.json'))


# while True:
#     try:
#         word = input('Enter the word: ')
#         if word in data:
#             print(data[word])
#             break
#         else:
#             print('Please try with other word: ')
#
#     except:
#         print('try again ')

def translate(w):
    if w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean '%s' instead? Please type Y if Yes, else N.: " % get_close_matches(w, data.keys())[0])
        if yn.upper() == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn.upper() == 'N':
            return "The word does not exist, please check it."
        else:
            return "we didn't understand your input."
    else:
        return "The word does not exist, please check it."


word = input('Please enter the word: ')
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print('\n', output)
