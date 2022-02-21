
w = float(input("Enter the weight in Kilograms: "))
h = float(input("Enter the height in Metres: "))

BMI = w / (h ** 2)

if BMI < 18.5 :
    status = "UNDERWEIGHT"
elif 18.5 <= BMI <= 24.9 :  
    status = "NORMAL"
elif 25 <= BMI <= 29.9 :   
    status = "OVERWEIGHT"
elif 30 <= BMI <= 34.9 : 
    status = "OBESE"
elif BMI > 35 :
    status = "EXTREMELY OBESE"

print("Your body mass index is : ", status )