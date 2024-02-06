"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Burešová
email: zuza.buresova@centrum.cz
discord: zuza_34473
"""

from task_template import TEXTS

registred_users = {
    "bob" : "123", "ann" : "pass123", 
    "mike" : "password123", "liz" : "pass123"}
separator = "-" * 40

text_words = []
titlecase = []
uppercase = []
lowercase = []
numeric = []
length_words = []
lenghts_frequency = dict()

# prihlaseni uzivatelu a kontrola jejich registrace
user = (input("username:")).lower()
password = input("password:")

if user not in registred_users \
    or password != registred_users[user]:
    print("Unregistered user, terminating the program..")
    quit()
print(f"{separator}\nWelcome to the app, {user}\n\
We have 3 texts to be analyzed.\n{separator}")

# analyza textu (number_text => TEXTS[number_text - 1])
try:
    number_text = int(input("Enter a number btw. 1 and 3 to select: "))
    if number_text not in range(1, len(TEXTS)+1):
        print("Incorrect text number, terminating the program..")
        quit()
except ValueError:
        print("Incorrect input, enter a number, terminating the program..")
        quit()

print(separator)

for word in TEXTS[number_text - 1].split():
    text_words.append(word.strip(",.?! "))

for word in text_words:
    if word.istitle() and word.isalpha():
        titlecase.append(word)
    elif word.isupper() and word.isalpha():
        uppercase.append(word)
    elif word.islower() and word.isalpha():
        lowercase.append(word)
    elif word.isnumeric():
        numeric.append(int(word))
    length_words.append(len(word))

print(f"There are {len(text_words)} words in the selected text.")
print(f"There are {len(titlecase)} titlecase words.")
print(f"There are {len(uppercase)} uppercase words.")
print(f"There are {len(lowercase)} lowercase words.")
print(f"There are {len(numeric)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric)}")

# cetnost ruznych delek slov v textu
length_words = sorted(length_words)

for lenght in length_words:
    lenghts_frequency.update({lenght: length_words.count(lenght)})
max_frequency = max(lenghts_frequency.values())

print(separator)
print(f"LEN|{"OCCURENCES".center(max_frequency+2)}|NR.")
print(separator)

for lenght, frequency in lenghts_frequency.items():
    print(f"{str(lenght).rjust(3)}|{("*" * frequency).ljust(max_frequency + 2)}|{frequency}")