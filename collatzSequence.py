def collatz(number):
    if(number %2 ==0):
        result=number // 2
        print(result)
        return result
    else:
        result= 3 * number + 1
        print(result)
        return result
try:
    result=collatz(int(input("Please enter an integer value: \n")))
    while (result != 1):
        result=collatz(result)
except ValueError:
       print("You must enter a string")