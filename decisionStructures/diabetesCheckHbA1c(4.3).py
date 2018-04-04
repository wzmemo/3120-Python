# diabetes check HbA1c
def main3():
    userInput = input('Input your HbA1c level: ')
    diabetesCalc(userInput)
    print ('end of prgm')
def diabetesCalc(user):
    user = float(user)
    if user < 5.7:
        print ('You are in the normal range ')
    if user >= 5.7 and user < 6.4:
        print ('You are considered to have"pre-diabetes" ')
    if user >= 6.4:
        print ('You are considered diabetic ')
    
main3()
