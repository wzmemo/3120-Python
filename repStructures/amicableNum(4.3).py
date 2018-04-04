# Amicable number

def main7():
    amicable1 = int(input('Enter first number: '))  
    amicable2 = int(input('Enter second number: '))
    
    isAmicable1 = amicable_check(amicable1)
    isAmicable2 = amicable_check(amicable2)
    if amicable1 == isAmicable2 and amicable2 == isAmicable1:
        print (amicable1,'and', amicable2, 'are amicable numbers')
    else:
        print ('Not amicable number pairs')

    
def amicable_check(a):
    amicable_total = 0
    for n in range(1,a):
        if a % n == 0:
            amicable_total += n
    return amicable_total

main7()
