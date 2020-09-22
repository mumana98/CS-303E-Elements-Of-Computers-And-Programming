#Matthew Umana msu245

def reverse_string(string):
    #return string[::-1]
    new_string = ""
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string

def is_palindrome(string):
    string1 = string
    string2 = reverse_string(string)
    if(string1 == string2):
        return "Palinedrome!"
    else:
        return "Not a palindrome."

def Prime(num):
    for i in range(0,num):
        if num == 1 or num == 2:
            return "prime"
        elif i == 0:
            continue
        elif(num % i == 0):
            if(num == 1 or num == 2):
                return "prime"
                break
            elif(i == 1):
                continue
            else:
                return "not prime"
                break
        elif(i == num-1):
            return "prime"

def is_Prime(num):
    for i in range(1,num):
        if(num % i == 0):
            if(num == 1 or num == 2):
                #return "prime"
                break
            elif(i == 1):
                continue
            else:
                #return "not prime"
                break
        elif(i == num-1):
            return num


def twin_primes():
    for i in range(1,1001):
        prime1=is_Prime(i)
        prime2=is_Prime(i+2)
        if(prime1 != None and prime2 != None):
            print(str(prime1) + ", " + str(prime2))



def main():

    for x in range(3):
        palindrome_string = input("Enter a word: ")
        print(is_palindrome(palindrome_string))
    
    for x in range(3):
        number = eval(input("Enter a number: "))
        if Prime(number) == "prime" and Prime(int(reverse_string(str(number)))) == "prime":
            if is_palindrome(str(number)) == "Palinedrome!":
                print("Not an emirp.")
            else:
                print("Emirp!")
        else:
            print("Not an emirp.")
    twin_primes()

main()
