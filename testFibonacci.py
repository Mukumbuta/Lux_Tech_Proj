def testFibonacci(inputNumber):
    firstTerm  = 0
    secondTerm = 1
    thirdTerm  = 0
    while(thirdTerm < inputNumber):
        thirdTerm   = firstTerm + secondTerm
        firstTerm   = secondTerm
        secondTerm  = thirdTerm
    if(thirdTerm == inputNumber):
        print(f'The number you entered, {inputNumber}, is a Fibonacci number.')
    else:
        print(f'The number you entered, {inputNumber}, is not a Fibonacci number.')
inputNumber = input("Enter any positive number:\n")
testFibonacci(int(inputNumber))
