# 1.Scrieți o funcție care convertește temperatura din grade celsius în fahrenheit și invers (formula: c/5 = f-32/9)
def ConvertTemp():
    number = float(input("Enter a number: "))
    fahrenheit = (number * 9/5) + 32
    celsius = (fahrenheit - 32) * 5/9
    print('Celsius is:%0.2f\n'%(fahrenheit),'Farhrenheit is:%0.2f'%(celsius))

ConvertTemp()

# 2.Scrieți o funcție determina dacă un text este palindrom (caiac, capac, minim)
def isPalindrome():
    nume = str(input("Enter a str:"))
    if nume == nume[::-1]:
        print("yes")
    else:
        print("no")

isPalindrome()

# 3.Scrieți o funcție care sa afiseze toți divizorii unui număr întreg.
def AllDivisors():
    number = int(input("Input the number:"))
    for i in range(1,number+1):
        if number % i == 0:
            print(i)

AllDivisors()

# 4. Calculati suma tuturor numerelor între 1000 si 2300 care se împart fără rest la 5 și 7
def SumOfNumbers():
    sum = 0
    for i in range(1000, 2300+1):
        if (i % 5 == 0 ) and (i % 7 == 0):
            sum += i
    print (sum)
    
SumOfNumbers()

# 5. Scrieți o funcție care sa calculeze numărul de litere și cifre din un text.
def CalculateNumberOfLettersAndNumbers():
    txt = input("Introduce the text:")
    digit = alpha = 0
    for i in txt:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            alpha += 1
   
    print("Letters:", alpha, "\n Number:",digit)

CalculateNumberOfLettersAndNumbers()

# 6.Scrieți un program care verifica dacă o parola introdusă de utilizator este securizata
def Parola():
    digit = 0
    lower = 0 
    upper = 0 
    caracter = 0
    parola_users = input("Enter the password:")
    if (len(parola_users) >= 8 and parola_users != '@' and  parola_users != ',' and parola_users != '{' and parola_users != '}'):
        for i in parola_users:
            if i.isdigit():
                digit +=1
            elif i.islower():
                lower +=1
            elif i.isupper():
                upper += 1
            elif (i=='!' or i=='/' or i=='#' or i=='*'):
                caracter +=1
    if(digit >= 1 and lower >= 1 and upper >= 1 and caracter >= 1 and (digit + lower + upper + caracter == len(parola_users))):
        print("Valid password")
    else:
        print("Invalid password")

Parola()

# 7.Scrieți un program care sa elimine cuvinte duplicate dintr-o propozitie.
def DoubleWords():
    i = 0
    words = input("Introduce words:")
    words = words.split()
    print(" ".join(sorted(set(words))))

DoubleWords()
