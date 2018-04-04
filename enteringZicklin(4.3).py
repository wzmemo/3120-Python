# entering Zicklin needs at least 45 credits overall with GPA 2.25 higher
def main5():
    credits = input('Enter number of credits: ')
    while credits.isdigit() == False:
        credits = input('Enter ONLY numbers: ')
    gpa = input('Enter GPA: ') #needs to be float but cannot
    while gpa.isdigit() == False:
        gpa = input('Enter ONLY numbers: ')
    credits = int(credits)
    gpa = float(gpa)
    if credits > 45 and gpa > 2.25:
        print ("You can enter Zicklin: ")
    else:
        print ('Im Sorry, you cannot enter Zicklin: ')
main5()
