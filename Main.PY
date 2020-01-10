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
ER_ENDING1 = "e"
ER_ENDING2 = "es"
ER_ENDING3 = "e"
ER_ENDING4 = "ons"
ER_ENDING5 = "ez"
ER_ENDING6 = "ent"
# Ending: -ir
IR_ENDING1 = "s"
IR_ENDING2 = "s"
IR_ENDING3 = "t"
IR_ENDING4 = "ons"
IR_ENDING5 = "ez"
IR_ENDING6 = "ent"

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
    print (PPN1 + space + WordStart +  ER_ENDING1)
    print (PPN2 + space + WordStart +  ER_ENDING2)
    print (PPN3 + space + WordStart +  ER_ENDING3)
    print (PPN4 + space + WordStart +  ER_ENDING4)
    print (PPN5 + space + WordStart +  ER_ENDING5)
    print (PPN6 + space + WordStart +  ER_ENDING6)
elif WordEnd == "ir":
    print("Support for these types will be added in 1.1")
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
