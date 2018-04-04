# test if even/odd
def main2():
    userNum = input('Enter number: ')
    while userNum.isdigit()==False:
        userNum = input('Enter ONLY number: ')
    evenOdd(userNum)
    print ('end of prgm')
def evenOdd(num):
    num = int(num)
    if num % 2 == 0:
        print (num, 'is an even number')
    else:
        print (num, 'is an odd number')
main2()
