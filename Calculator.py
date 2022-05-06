import math

userInput = input("Query: ").replace("log(", "math.log(")
if not userInput.isalpha():
    print(eval(userInput))