import random
readername = input('Enter your name here: ')
print('Hello' + readername)

name = [' Harjas ', ' Charchill ', ' Sameer ', ' Jairaj ']
place = [' India ', ' Germany ', ' France ', ' Canada ', ' England ']
quests = [' arrive to grand bulding and take a photograph', ' go to meet a celebrity', ' drive in a large jeep', ' Eat pizza at the most lavish restaurant you came across', ' Buy 20 expensive things in the most extravantage shop they see along the street',' Go to the most beautiful area they search up in India']
role = [' normal boy ', ' old man ', ' teenage boy ', ' secondary student ', ' wroaker at harrods ', ' university student ']
weather = [' a sunny day ', ' a very humid and hot day ', ' a cold night ', ' a cloudy day ', ' a rainy day ']


story ='Once upon a time a' + random.choice(role) + 'called' + random.choice(name) + 'lived in a beautiful area called'  + random.choice(place) + 'where it was' + random.choice(weather) + 'and in this place' + random.choice(name) + 'will have to' + random.choice(quests) +'.'
print(story)