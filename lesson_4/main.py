# 1. Scrieți un program care o sa creeze un joc pentru ghicirea capitalei unei țări, cu 4 opțiuni de răspuns.
#Citiți conținutul fișierului countries.txt.
#Utilizați funcția random pentru a alege țara și capitala ei, folosiți aceeași metodă pentru a găsi alte 3 opțiuni de răspuns.
#Creați întrebarea folosind 4 opțiuni de răspuns.
#Captați răspunsul utilizatorului  folosind funcția input() și afișați răspunsul corect.

import random

def Games():
    countries_dico = {}
    countries = open('countries.txt')

    for line in countries:
        line = line.split(',')
        country = line[0]
        capitals = line[-1]
        countries_dico[country] = capitals.replace('\n','')
        country = list(countries_dico.keys())
        capitals = list(countries_dico.values())
    random_country = random.choice(country)
    capitals_answer = capitals[country.index(random_country)] #Metoda index intoarce key stiin valoarea din dictionar#
    print("What is the capital of the country", random_country, "?")
    print(f'Answer options:')
    print(f'1.',random.choice(capitals))
    print(f'2.',capitals_answer)
    print(f'3.',random.choice(capitals))
    print(f'4.',random.choice(capitals))
    answer = input(f'Enter the answer: ')

    if capitals[country.index(random_country)] == answer:
        print('You entered the correct answer!')
    else:    
        print('You entered the incorrect answer.\nThe correct answer is: ',capitals[country.index(random_country)])
      
Games()
