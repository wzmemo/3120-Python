def triangulate(n):
    for r in range(1,n+1):
        for c in range(1,r):
            print ('*',end="")
        print('*')
    return

def main():
    number = input('Enter a number you need triangular numbers for: ')
    number = int(number)
    print ('This is the triangular pattern for your number, n =',number)
    final = triangulate(number)
main()
