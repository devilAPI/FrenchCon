##############################
#imports
##############################
import webbrowser


##############################
#Please Enter Word
##############################
print("Please enter your Word (French only!)")
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
IR_ENDING1 = "is"
IR_ENDING2 = "is"
IR_ENDING3 = "it"
IR_ENDING4 = "ons"
IR_ENDING5 = "ez"
IR_ENDING6 = "ent"
# Ending: -dre
DRE_ENDING1 = "ds"
DRE_ENDING2 = "ds"
DRE_ENDING3 = "d"
DRE_ENDING4 = "dons"
DRE_ENDING5 = "dez"
DRE_ENDING6 = "dent"

#other
space = " "


##############################
#Getting WordStart and WordEnd
##############################
WordEnd = Word[-2:]
WordStart = Word[:-2]
WordEnd3 = Word[-3:]
WordStart3 = Word[:-3]


##############################
#Checking if Word is compatible + Conjugate!
##############################

if Word == "etre": 
    print()
    print("Je suis")
    print("Tu es")
    print("Il/Elle/On est")
    print("nous sommes")
    print("vous etes")
    print("ils/elles sont")
    print() 
elif Word == "avoir": 
    print()
    print("j'ai")
    print("Tu as")
    print("Il/Elle/On a")
    print("nous avons")
    print("vous avez")
    print("ils/elles ont")
    print()
elif Word == "savoir": 
    print()
    print("Je sais")
    print("Tu sais")
    print("Il/Elle/On sait")
    print("nous savons")
    print("vous savez")
    print("ils/elles savent")
    print()
elif Word == "pouvoir": 
    print()
    print("Je peux")
    print("Tu peux")
    print("Il/Elle/On peut")
    print("nous pouvons")
    print("vous pouvez")
    print("ils/elles peuvent")
    print()
elif Word == "vouloir": 
    print()
    print("Je veux")
    print("Tu veux")
    print("Il/Elle/On veut")
    print("nous voulons")
    print("vous voulez")
    print("ils/elles voulent")
    print()
elif Word == "connaitre": 
    print()
    print("Je connais")
    print("Tu connais")
    print("Il/Elle/On connaît")
    print("nous connaissons")
    print("vous connaissez")
    print("ils/elles connaissent")
    print()
elif Word == "aller": 
    print()
    print("Je vais")
    print("Tu vas")
    print("Il/Elle/On va")
    print("nous allons")
    print("vous allez")
    print("ils/elles vont")
    print()
elif Word == "courir": 
    print()
    print("Je cours")
    print("Tu cours")
    print("Il/Elle/On court")
    print("nous courons")
    print("vous courez")
    print("ils/elles courent")
    print()
elif Word == "devoir": 
    print()
    print("Je dois")
    print("Tu dois")
    print("Il/Elle/On doit")
    print("nous devons")
    print("vous devez")
    print("ils/elles doivent")
    print()
elif Word == "dire": 
    print()
    print("Je dis")
    print("Tu dos")
    print("Il/Elle/On dit")
    print("nous desons")
    print("vous dites")
    print("ils/elles disent")
    print()
elif Word == "faire": 
    print()
    print("Je fais")
    print("Tu fais")
    print("Il/Elle/On fait")
    print("nous faisons")
    print("vous faites")
    print("ils/elles font")
    print()
elif Word == "lire": 
    print()
    print("Je lis")
    print("Tu lis")
    print("Il/Elle/On lit")
    print("nous lisons")
    print("vous lisez")
    print("ils/elles lisent")
    print()
elif Word == "mettre": 
    print()
    print("Je mets")
    print("Tu mets")
    print("Il/Elle/On met")
    print("nous mettons")
    print("vous mettez")
    print("ils/elles mettent")
    print()
elif Word == "payer": 
    print()
    print("Je paie")
    print("Tu paies")
    print("Il/Elle/On paie")
    print("nous payons")
    print("vous payez")
    print("ils/elles paient")
    print()
elif Word == "voir": 
    print()
    print("Je vois")
    print("Tu vois")
    print("Il/Elle/On voit")
    print("nous voyons")
    print("vous voyez")
    print("ils/elles voient")
    print()
elif WordEnd == "er":
    print (PPN1 + space + WordStart +  ER_ENDING1)
    print (PPN2 + space + WordStart +  ER_ENDING2)
    print (PPN3 + space + WordStart +  ER_ENDING3)
    print (PPN4 + space + WordStart +  ER_ENDING4)
    print (PPN5 + space + WordStart +  ER_ENDING5)
    print (PPN6 + space + WordStart +  ER_ENDING6)
elif WordEnd == "ir":
    print (PPN1 + space + WordStart +  IR_ENDING1)
    print (PPN2 + space + WordStart +  IR_ENDING2)
    print (PPN3 + space + WordStart +  IR_ENDING3)
    print (PPN4 + space + WordStart +  IR_ENDING4)
    print (PPN5 + space + WordStart +  IR_ENDING5)
    print (PPN6 + space + WordStart +  IR_ENDING6)
elif WordEnd3 == "dre":
    print (PPN1 + space + WordStart3 +  DRE_ENDING1)
    print (PPN2 + space + WordStart3 +  DRE_ENDING2)
    print (PPN3 + space + WordStart3 +  DRE_ENDING3)
    print (PPN4 + space + WordStart3 +  DRE_ENDING4)
    print (PPN5 + space + WordStart3 +  DRE_ENDING5)
    print (PPN6 + space + WordStart3 +  DRE_ENDING6)
else:
    print("Sorry, This Word is currently not supported :( Check on GitHub for Updates")
    OpenGHUpdates = input("Do you want to open Github for update checking? (Y for YES; N for NO)")
    if OpenGHUpdates == "Y":
        print("Here You GO ;)")
        webbrowser.open("https://github.com/devilAPI/FrenchCon/releases")
    elif OpenGHUpdates == "N":
        print("Abort")
        exit(0)
    else:
        print("Sorry. Wrong Answer. (Y for YES; N for NO)")
        print("Abort")
        exit(0)
