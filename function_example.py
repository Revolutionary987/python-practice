# Temp conversion 
def temp_conversion():
    scale=input("Enter the temperature scale: (Celsius-C and Fahrenheit-F): ")
    return scale
     # if statement ### C = Celcius, F = Fahrenheit, K = Kelvin ##########
def celsius(temperature):
    return temperature*9/5+32

def fahrenheit(temperature):
    return (temperature-32)*5/9


scale=temp_conversion()

if scale.upper()=="C":  
    temperature=int(input("Enter the temperature in celcius:"))
    temp=celsius(temperature)
    print("The tempature in fahrenheit is:",temp,"F")
    

elif scale.upper()=="F":
    temperature=int(input("Enter the temperature in Fahrenheit:"))
    temp=fahrenheit(temperature)
    print("The tempature in celcius is:", temp, "C")     
    

# Password strength checker
# """ Note that password should contain min 8 letters , and atleast one special characters,capital letter ,small letter,digit"""
# def password_strength():

    password = input('Please enter your password:')
    return password

def password_checker(password):
    
    if len(password)<8:
        print("Your password must be at least 8 characters long.")

    if  not any(char.isupper() for char in password):
        print("Weak password")
        return False
    if not any(char.isdigit() for char in password):
        print("Weak password")
        return False
    if not any(char.islower() for char in password):
        print("Weak password")
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        print("Weak password")
        return False
    print('Your password is strong enough to be used.')

password=password_strength()

password_checker(password)

#Cost of items in list
def cart():
    dictionary = {}
    while 1:
        Cart=(input("Please enter the item name along with cost ibn the format (ItemName:cost) in dollars:$ "))
        if Cart=="":break
        try:        
            item,cost=Cart.split(":")
            dictionary.update({item:float(cost)})     
        except ValueError:
            print('Your input was not formatted correctly. Please try again.')
    return dictionary

def cost(dictionary):
    total_price = 0.0
    for value in dictionary: total_price += float(dictionary[value])
    print("The total price of the items is:",total_price,"$")

dictionary = cart()

cost(dictionary)


# check whether a string is a panlindrome

def word_input():
    word = input('Enter a word: ')
    return word.strip()

def palindrome_checker(word):
    if word==word[::-1]:
        print(f"{word} is a palindrome")

    else:print(f"{word} is not a palindrome")
    
word=word_input()
palindrome_checker(word)
        
# fibonacci series
def fibo(n):
    if  n==0 :return 0
    elif n==1 : return 1
    else:   
        return((fibo(n-1))+fibo(n-2))
n=int(input('Enter the number of terms you want to print:'))
for i in range(n+1):
    print("The fibonacci series is:",fibo(i))

# Factorial of a number using recursion

def factorial_recursion(number):
    if number==0:
        return 1
    return number*factorial_recursion(number-1)
print(factorial_recursion(10))

