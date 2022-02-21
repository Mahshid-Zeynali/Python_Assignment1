a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a < b + c and b < a + c and c < a + b :
    print ("This triangle can be drawn")
else :
    print("This triangle cannot be drawn")    