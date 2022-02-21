import math

a = float(input("please enter first number: "))
op = input("please enter the operator (+,-,*,/,radical,sin,cos,cot,tan,factorial) : ")

if op == "+" or op == "-" or op == "*" or op == "/" :
    b = float(input("please enter second number: "))

if op == "+" :
    result = a + b
elif op == "-" :
    result = a - b
elif op == "*" :
    result = a * b
elif op == "/" :
    if b != 0 :
        result = a / b
    else :
        result = " cannot divide by ZERO !! "    
elif op == "radical" :
    if a >= 0 :
        result = math.sqrt(a)
    else :
        result = "cannot show undefined result !!"
elif op == "sin" :    
    result = math.sin(math.degrees(a))
elif op == "cos" : 
    result = math.cos(math.degrees(a))
elif op == "cot" : 
    result = math.cot(math.degrees(a))
elif op == "tan" : 
    result = math.tan(math.degrees(a))    
elif op == "factorial" : 
    result = math.factorial(a)

print("result =", result)    
