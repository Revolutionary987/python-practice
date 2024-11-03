### Assignment 1: Handling Division by Zero

# Write a function that takes two integers as input and returns their division. Use try, except, and finally blocks to handle division by zero and print an appropriate message.

# def division():
#     num = int(input("Enter the numerator : "))
#     den = int(input("Enter the denominator : "))
#     try:
#        return num/den
#     except ZeroDivisionError :
#         print ("Can't divide by zero")
#     finally:
#         print("Division is over")

# print(division())

### Assignment 2: File Reading with Exception Handling

# Write a function that reads the contents of a file named `data.txt`. Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.
# def file_read():
#  DOUBT   # 
#     try:
#         file=open('data.txt','r')
#         return(file.read())
#     except FileNotFoundError:
#         print("File Not Found")
#     finally:
#         try:
#             (file.close())
#         except AttributeError:
#                 print("File Not Found")
    
    
# file_read()

### Assignment 3: Handling Multiple Exceptions

# Write a function that takes a list of integers and returns their sum. Use try, except, and finally blocks to handle TypeError if a non-integer value is encountered and print an appropriate message.
# def summ(num):
#     try:
#         return (sum(num))
#     except TypeError:
#         print("Please enter only integers")
#     finally:
#         print("Summing over the list is complete now.")
# print("The sum of numbers in the given list is :",summ([1,2,3]))

### Assignment 4: Exception Handling in User Input

# Write a function that prompts the user to enter an integer. Use try, except, and finally blocks to handle ValueError if the user enters a non-integer value and print an appropriate message.

# def int_input():
#     try:
#         return (int(input("Please Enter An Integer : ")))
#     except ValueError:
#         print("You Have Entered A Non-Integer Value.")
#     finally:
#         print("Program ends now")
# int_input()


### Assignment 5: Exception Handling in Dictionary Access

# Write a function that takes a dictionary and a key as input and returns the value associated with the key. Use try, except, and finally blocks to handle KeyError if the key is not found in the dictionary and print an appropriate message.
# def dict_access(dict,key):
#     try:
#         return (dict[key])
#     except KeyError:
#         print("The Given Dictionary Doesn't Contain The Given Key.")
#     finally:
#         print("Program ends now")
# dict={'a': 1, 'b': 2, 'c': 3}   
# print(dict_access(dict,'b'))


### Assignment 6: Nested Exception Handling

# Write a function that performs nested exception handling. It should first attempt to convert a string to an integer, and then attempt to divide by that integer. Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.
# def nested_exception():
#     try:
#         num=(int(input("Please Enter An Integer:")))
#         try:
#             return (num)
        
#         except ValueError:
#             print("You Have Entered A Non-Integer Value.")
#     except ValueError:
#         print("You Have Entered A Non-Integer Value.")

#     finally:
#         if "num" in locals():
#             try:
#                 print(10/num)
#             except ZeroDivisionError:
#                 print("The Given Integer Is Zero, Hence The Division By It Cannot Be Performed Now. Please Enter An Integer Which Isn'T Zero.")
        
# nested_exception()
# # OR
# def nested_exception():
#     num = None  # Initialize num
#     try:
#         num = int(input("Please Enter An Integer: "))
#         print("You have entered input")
#     except ValueError:
#         print("You Have Entered A Non-Integer Value.")
#         return None
#     finally:
#         if num is not None:  # Check if num was successfully assigned
#             try:
#                 print("Result of division: ", 10 / num)
#             except ZeroDivisionError:
#                 print("The Given Integer Is Equal To Zero, Hence You Can't Divide By It.")
#         print("Program ends now")


### Assignment 7: Exception Handling in List Operations

# Write a function that takes a list and an index as input and returns the element at the given index. Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.

# def list_op(list,index):
#     try:
#         return list[index]
#     except IndexError:
#         print("The Given List Doesn't contain The Given Index.")
# list=['a', 'b', 'c']
# print(list_op(list,2))
# print(list_op(list,3))

### Assignment 8: Exception Handling in Network Operations

# Write a function that attempts to open a URL and read its contents. Use try, except, and finally blocks to handle network-related errors and print an appropriate message.
# Doubt
# import requests

# def url_op():
#     try:
#         return (requests.get("https://www.google.com/"))
#     except ConnectionError:
#         print("Server is down right now, please try again later.")
#     except TimeoutError:
#         print("The Request Timed Out, Please Try Again Later.")
#     except requests.HTTPError:
#         print("HTTP Error Occurred While Attempting To Open The Given URL.")

### Assignment 9: Exception Handling in JSON Parsing

# Write a function that attempts to parse a JSON string. Use try, except, and finally blocks to handle JSONDecodeError if the string is not a valid JSON and print an appropriate message.
# import json
# def json_parse(json_string):
#     try:
#         return (json.loads(json_string))
#     except json.JSONDecodeError:
#         print("The Given String Is Not A Valid JSON, Hence It Cannot Be Parsed Now.")
#     finally:
#         print("Parsing of the given string is complete now.")
# print(json_parse('{"name": "John", "age": 30}'))
# print(json_parse('{"name": "John", "age": 30'))


### Assignment 10: Custom Exception Handling

# Define a custom exception named `NegativeNumberError`. Write a function that raises this exception if a negative number is encountered in a list. Use try, except, and finally blocks to handle the custom exception and print an appropriate message.
# Important
# class NegativeNumberError(Exception):
#     pass
# def custom_exception():
#     try:
#         num=int(input("Please Enter a positive number:"))
#         if num<0:
#             raise NegativeNumberError("Enter only positive number")
#         return num
#     except (NegativeNumberError):
#         print("Enter only positive numbers")
        
#     finally:
#         print("You have created a custom exception")
# print(custom_exception())

### Assignment 11: Exception Handling in Function Calls

#  Write a function that calls another function which may raise an exception. Use try, except, and finally blocks to handle the exception and print an appropriate message.
# def func():
#     try:
#         return int(input("Enter a number:"))
#     except ValueError:
#         print("Please enter an integer")
# def func2():
#     return func()
# print(func2())

### Assignment 12: Exception Handling in Class Methods

# Define a class with a method that performs a division operation. Use try, except, and finally blocks within the method to handle division by zero and print an appropriate message.

# class Division:
#     def __init__(self,division):
#         self.division=division
#     def perform_division(self):
#         try:
#             num=int(input("Enter a number:"))
#             return 10/num
#         except ZeroDivisionError:
#             print("You can't divide by zero")
# div=Division(1)
# result=div.perform_division()
# if result is not None:
#     print(result)

## Assignment 13: Exception Handling in Data Conversion

# Write a function that takes a list of strings and converts them to integers. Use try, except, and finally blocks to handle ValueError if a string cannot be converted and print an appropriate message.
### Assignment 14: Exception Handling in List Comprehensions

# Write a function that uses a list comprehension to convert a list of strings to integers. Use try, except, and finally blocks within the list comprehension to handle ValueError and print an appropriate messag

# def convert_int(list):
#     try:
#         return [int(num)for num in list]
#     except ValueError:
#         print("The List contains strings which cannot be converted to integers")
# print(convert_int(['1','2']))
# result=convert_int(["1","b"])
# if result is not None:
#     print(result)


### Assignment 15: Exception Handling in File Writing

# Write a function that attempts to write a list of strings to a file. Use try, except, and finally blocks to handle IOError and ensure the file is properly closed.

# def list_to_file(list):
#     try:
#         with open("test.txt","w+") as file:
#             file=file.write()
            
#     except (IOError,TypeError):
#         print("An Error Occurred While Attempting To Write The Given List Of Strings To A File.")

# print(list_to_file(["1","2"]))
