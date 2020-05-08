import csv

#Might have to change the number used when the dictionary is being created
data = []

with open('words.csv') as csvfile:
    word_reader = csv.reader(csvfile, delimiter=',')
    for row in word_reader:
        data = data + row

words = data

word_dict = {}

for word in words:
    word = word.lower()

#print(words)

for word in words:
    if len(word) == 0:
        continue
    elif len(word.replace(" ","")) in word_dict:
        word_dict[len(word.replace(" ",""))].append(word.lstrip().rstrip())
    else:
        word_dict[len(word.replace(" ",""))] = [word.lstrip().rstrip()]

for key in word_dict.keys():
    print("Key: " + str(key) + " Values: " + ' | '.join(map(str, word_dict[key])) )

num = 1
while num != "exit":
    num = input("How many letters is/are the word(s)? (Don't count whitespaces!)\n")
    if num in word_dict.keys():
        print("\n" + ' | '.join(map(str, word_dict[num])) + "\n")
    else:
        print("No words found with length " + str(num) + "!\n")
