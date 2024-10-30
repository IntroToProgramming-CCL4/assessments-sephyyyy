# Exercise 10: Is it even?
def main():
    num = int(input( "Input a number: "))
    message = sub(num)
    print (message)

def sub(num):
    if (num%2) == 0 and num>0:
        return "Your number is positive even."
    elif (num%2) == 0 and num<0:
        return "Your number is negative even."
    elif (num%2) != 0 and num>0:
        return "Your number is positive odd."
    elif (num%2) != 0 and num<0:
        return "Your number is negative odd"
    else:
        return "Your number is zero."

main()
