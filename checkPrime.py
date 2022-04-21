from math import sqrt

def checkPrime(inputNumber):
    num = 1
    if(inputNumber <= num):
        print("The number you entered is not a Prime number.")
    for cont in range(2, int(sqrt(inputNumber)) + 1):
        if(inputNumber % cont == 0):
            print("The number you entered is not a Prime number.")
        else:
            print("The number you entered is a Prime number.")
inputNumber = input("Enter any number:\n")
checkPrime(int(inputNumber))
