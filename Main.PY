##############################
#Please Enter Word
##############################
print("Please enter your Word (Frensh only!)")
Word = input("Your Answer: ")
print()
print("You choosed " + Word + "!")
print()
print()
print()
##############################
#Personal Pronoun and Endings for Verbs as String, for easy change if i did something wrong or smth
##############################

#PersonalProNouns
PPN1 = "Je"
PPN2 = "Tu"
PPN3 = "Il/Elle/On"
PPN4 = "Nous"
PPN5 = "Vous"
PPN6 = "Ils/Elles/Ons"
# Ending: -er
ENDING1 = "e"
ENDING2 = "es"
ENDING3 = "e"
ENDING4 = "ons"
ENDING5 = "ez"
ENDING6 = "ent"

#other
space = " "


##############################
#Getting WordStart and WordEnd
##############################
WordEnd = Word[-2:]
WordStart = Word[:-2]

if WordEnd == "er":
    print(" Word: " + Word)
    print()
    print (PPN1 + space + WordStart +  ENDING1)
    print (PPN2 + space + WordStart +  ENDING2)
    print (PPN3 + space + WordStart +  ENDING3)
    print (PPN4 + space + WordStart +  ENDING4)
    print (PPN5 + space + WordStart +  ENDING5)
    print (PPN6 + space + WordStart +  ENDING6)

elif Word == "etre": 
    print()
    print("Je suis")
    print("Tu es")
    print("Il/Elle/On est")
    print("nous sommes")
    print("vous etes")
    print("ils/elles sont")
    print()
else:
    print("Sorry, This Word is currently not supported :( Check on GitHub for Updates")
