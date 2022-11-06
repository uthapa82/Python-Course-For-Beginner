# try:
#     answer = 5 / 0
#     print(answer)

# except:
#     print("Ohh you're trying to divide number by 0 :(")

# print("Give me 2 numbers, and I'll divide them. ")
# print("Enter q to quit")

# while True:
#     first = input("\nEnter first number ")
#     if first == 'q':
#         break
    
#     second = input("\n Enter second number: ")
#     if second == 'q':
#         break
#     try:
#         answer = int(first) / int(second)
#     except ZeroDivisionError:
#         print("Can't divide by 0 !")
#     else:
#         print(answer)

# ---3 
filename = 'test.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    message = "Sorry the file " + filename + " is not created."
    print(message)