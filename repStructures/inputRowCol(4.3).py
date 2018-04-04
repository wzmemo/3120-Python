# ask user for r rows and c columns 
# print r for rows and c for columns
def main2():
    row = int(input('How many rows do you want: '))
    col = int(input('How many columns do you want: '))
    for r in range (row):
        for c in range (col):
            print ('*', end = "")
        print()
main2()
