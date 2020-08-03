# 1. Ce valoare o sa contina variabila a după execuția codului ?
a = 10
a += len(str(a))
print(a)
#Raspuns a = 12
######################################################################################################
# 2. Codul de mai jos conține o eroare, modificați codul astfel încît programul să funcționze corect.
# "In padurea cu alune aveau casa" + 2 + "pitici"
#Raspuns:
# Prima metoda
"In padurea cu alune aveau casa" + str(2) + "pitici"
# A doua metoda
f'"In padurea cu alune aveau casa" + {2} + "pitici"'
######################################################################################################
# 3. Ce valoare o sa contina variabila a dupa executia codului ?
a = 10
a += 1
print(a)
#Raspuns a = 11
######################################################################################################
# 4. Codul de mai jos contine o erroare, Modificati codul ca nu apara erroare?
a = int(input())
a += 1
print(a)
######################################################################################################
# 5. Scrieți un program care primește la input numele fisierului (text.txt, program.java) si intoarce 
# extensia lui (txt, java). Puteti sa folositi functia split()
a = "text.txt"
b = "program.java"
a = a.split(".",1)
b = b.split(".",1)
print(a[-1])
print(b[-1])
######################################################################################################
# 6.1		Ce valoare are expresia a[int(int('3' * 2) // 11] ?
a = [int(int('3'*2)//11)]
print(a)
#Raspuns 6.1: a = [3]
# 6.2		Adaugati o valoare nouă în lista a pe prima poziție.
a = ['a', 'b', 'c', 'd']
a[0] = 'a1'
print(a)
# 6.3		Ștergeți ultimele 2 valori din lista.
a = ['a', 'b', 'c', 'd']
del a[2]
del a[-1]
print(a)
# 6.4		Ordonati lista a descrescator
a = ['a', 'b', 'c', 'd']
a.sort(reverse=True)
print(a)
# 6.5		Creați o listă nouă b care sa conțină toate elementele din lista a cu excepția primelor 2 elemente.
a = ['a', 'b', 'c', 'd']
b = a[2:4]
print(b)
# 7.	Scrieți un program care afișează toate elementele din un invetar si calculează suma lor.
elemente = {"scaune": 77, "mese": 66, "dulapuri": 1}
suma = elemente.get('scaune') + elemente.get('mese') + elemente.get('dulapuri')
print("Suma totala este: ",suma)
print(list(elemente.keys()))



