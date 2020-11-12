def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print('Welcome User :) \n'
      'Select any option\n'
      '1 . Additon\n'
      '2 . Subtraction\n'
      '3 . Multiplication\n'
      '4 . Division')

ui = int(input("Select any one operation from 1 to 4"))

if ui>=5:
    print("Try Again!")
    
else:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))

    if ui==1:
        print(n1, '+', n2, "=", add(n1,n2))

    elif ui==2:
        print(n1, '-', n2, '=', sub(n1,n2))

    elif ui==3:
        print(n1, '*', n2, "=", mul(n1,n2))

    elif ui==4:
        print(n1, '/', n2, '=', div(n1,n2))

