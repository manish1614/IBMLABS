def compute_incf(x,y):
 if x > y:
    smaller = y
 else:
    smaller= x
 for i in range(1, smaller + 1):
    if (x % i == 0) and (y % i == 0):
        hcf = i
 return hcf


num1 = int(input("Enter a New number"))
num2 = int(input("Enter a New Number"))
print("The H.C.F. is", compute_incf(num1, num2))
