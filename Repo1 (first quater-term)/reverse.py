sentence = input('Enter a sentence: ')
split_words = sentence.split()
reversed_words = split_words[::-1]
reversed_sentence = ' '.join(reversed_words)
print(reversed_sentence)