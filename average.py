name = input("please enter your name: ")
family = input("please enter your family: ")
score1 = float(input("please enter the score of lesson 1: "))
score2 = float(input("please enter the score of lesson 2: "))
score3 = float(input("please enter the score of lesson 3: "))

average = ( score1 + score2 + score3 ) / 3
 
if average >= 17 :
    status = "Great"
elif  17 > average >=12 :  
    status = "Normal"
elif average < 12 :
    status = "Fail"    

print(name , family ,"'s status is :" , status)