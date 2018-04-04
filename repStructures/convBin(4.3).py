
def conv_bin(number): # write function to convert to bin
    return format(number,'b')

def is_pal(string): # write function to convert to palin
    if string == string[::-1]:
        return True #boolean
    else:
        return False

def main():
    total = 0 #initalize total
    for i in range (0,1000000): #range under million
        # find first value in base 10, no need to convert
        # if palindromic will return boolean true
        val = is_pal(str(i)) 
        #convert using fuction 
        binary = conv_bin(i)
        # find second value in base 2,
        # if palindromic will return boolean true
        val2 = is_pal(str(binary))
        #compare
        if val == True and val2 == True:
            #sum
            total = total + i
    print (total)
    
main()
