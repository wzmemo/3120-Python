def main5():
    number = input('Give number: ')
    while number.isdigit()==False:
        number = input('Please provide ONLY a number: ')
    curiousCheck(number)

def curiousCheck(num):
    #num = int(num) #first four lines create factorial
   
    for digit in num:
        digit = int(digit)
        factorialDigit = 1
        factorialSum = 0
        for i in range(1,digit+1):
            factorialDigit *= i
        
        
        factorialSum = factorialSum + factorialDigit
        print (factorialSum)
   
    print (factorialSum) #not adding correcntly

main5()
