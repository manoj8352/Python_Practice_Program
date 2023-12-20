"""Salary increment , salary will increase according to their year of service ,if their year of service is less 5 year their not eligible for salary increment """

#First getting the value form the user and store in the yearofservice variable
print("enter you year of service in whole number format ")
yearofservice=input("Enter the year of service : ")
#using if condition to check the given value is equal to 5 years or more than 5 years
def validinput():
    if int(yearofservice) < 5 :
     #if the yearofservice is less than 5 year 
      print("You are not eligible for salary increment ")
    elif int(yearofservice) > 5   or int(yearofservice) == 5:
     #if condition is true ,get the  salary detail  from the user and store the value in the salary variable  
         salary=int(input("Enter your salary : "))
         #calculating the salary increment
         calculate=salary*(int(yearofservice)/100)
         salaryincrease=salary+calculate
         #result of  the salary increment
         print("Your salary  has been increase "+str(yearofservice)+"%, Now your salary is "+str(salaryincrease))

    else:
       print("your not eligible for salary increment")
#isdigit is used for checking where the input is only contain number
if yearofservice.isdigit():
     
     validinput()
else:
    print("enter the valid number")     

   
  



    
 



       

     
     

          
 

    



