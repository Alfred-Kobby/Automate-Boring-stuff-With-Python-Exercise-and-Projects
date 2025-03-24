import re

file = open('sentence.txt')
text = file.read()
file.close()

matcher = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')

matched = matcher.findall(text)
if matched is not None:
    for i in range(len(matched)):
        if matched[i] == 'ADJECTIVE':
            adjective = input("Enter an adjective: \n")
            text = re.sub('ADJECTIVE', adjective, text, 1)
        elif matched[i] == 'NOUN':
            noun = input("Enter an noun: \n")
            text = re.sub('NOUN', noun, text, 1)
        elif matched[i] == 'ADVERB':
            adverb = input("Enter an adverb: \n")
            text = re.sub('ADVERB', adverb, text, 1)
        elif matched[i] == 'VERB':
            verb = input("Enter an verb: \n")
            text = re.sub('VERB', verb, text, 1)
print(text)

file = open('sentence.txt', 'w')
file.write(text)
file.close()
