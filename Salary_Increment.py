"""Salary increment  according to the year that they have been worked in the company if the worked 1 year they are salary  will increase 1% """

#First getting the value form the user and store in the yearofservice variable
yearofservice=input("Enter the year of service : ")
#using if condition to check the given value is equal to 5 years or more than 5 years
def validinput():
    if int(yearofservice) < 0 :
     #if the yearofservice is less than 5 year 
      print("Enter the valid number")
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







if yearofservice.isdigit():
     print("your are eligible for salary increment")
     validinput()
else:
    print("enter the valid number")     

   
  



    
 



       

     
     

          
 

    



