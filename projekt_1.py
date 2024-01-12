"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Burešová
email: zuza.buresova@centrum.cz
discord: zuza_34473
"""

from task_template import TEXTS

registrovani_uzivatele = {
    "bob" : "123", "ann" : "pass123", 
    "mike" : "password123", "liz" : "pass123"}
oddelovac = "-" * 40
# prihlaseni uzivatelu a kontrola jejich registrace
user = (input("username:")).lower()
password = input("password:")

if user not in registrovani_uzivatele \
    or password != registrovani_uzivatele[user]:
    print("unregistered user, terminating the program..")
    quit()
print(f"{oddelovac}\nWelcome to the app, {user}\n\
We have 3 texts to be analyzed.\n{oddelovac}")

# analyza textu (number_text => TEXTS[number_text - 1])
number_text = input("Enter a number btw. 1 and 3 to select: ")
for pismeno in number_text:
    if not pismeno.isdigit():
        print("incorrect text number, terminating the program..")
        quit()
number_text = int(number_text)
if number_text not in range(1,4):
    print("incorrect text number, terminating the program..")
    quit()
print(oddelovac)
text_slova = [slovo.strip(",.?! ") for slovo in TEXTS[number_text - 1].split()]


print("There are", len(text_slova), "words in the selected text.")
titlecase = [(slovo.istitle() and slovo.isalpha()) for slovo in text_slova]
print("There are", titlecase.count(True), "titlecase words.")
uppercase = [(slovo.isupper() and slovo.isalpha()) for slovo in text_slova]
print("There are", uppercase.count(True), "uppercase words.")
lowercase = [(slovo.islower() and slovo.isalpha()) for slovo in text_slova]
print("There are", lowercase.count(True), "lowercase words.")
numeric = [slovo for slovo in text_slova if slovo.isnumeric()]
print("There are", len(numeric), "numeric strings.")
numeric_int = [int(slovo) for slovo in numeric]
print("The sum of all the numbers", sum(numeric_int))

# cetnost ruznych delek slov v textu
delky_slov = sorted([len(slovo) for slovo in text_slova])
cetnost_delek = {delka: delky_slov.count(delka) for delka in delky_slov}
max_cetnost = max(cetnost_delek.values())

print(oddelovac)
print("LEN", "OCUURENCES".center(max_cetnost+2), "NR.", sep = "|")
print(oddelovac)
for delka, cetnost in cetnost_delek.items():
    print(str(delka).rjust(3), ("*" * cetnost).ljust(max_cetnost + 2), cetnost, sep = "|")