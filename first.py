# First program :)
#message = "Hello, welcome to making your first program!" #variable can't start with numbers and starts with lowercase, has meaning
# "=" is an assignment operator here, left has variable and right has value CANT FLIP
#The message is the value or data. int - integer, float - +/- decimals, bool - True/False, str - string (contains alpha, numeric, and special symbols)
# list - data type that can hold many other data types, dict - dictionary 
#name = input("What is your name?: ") #input is an example of: built in function, input stores string input from terminal to the related variable 
#print(message, name, end="\n", sep=" ") #sep is a separated and when unspecified seperates with space
#print("I hope this answers your question")

# num1=6
# num2=7
# print(num1+num2)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(num1+num2) #input reads/understands all inputs as string so numbers don't add --> SO WE ADD INT() which also means no more strings 