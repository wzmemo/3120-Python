# test if leap year
def main1():
    userInput = input('Enter a year: ')
    while userInput.isdigit()== False:
        userInput = input('Enter a year ONLY : ')
    leapCheck(userInput)
    print ('End of Program ')
def leapCheck(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year,'is a leap year')
            else:
                print(year, 'is not a leap year')
        else:
            print (year,'is a leap year')
    else:
        print (year,'is not a leap year')
        
main1()
