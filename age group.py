print("This program sorts you in your age group")
age= int(input("Enter your age: "))
 
if age >= 0 and age<= 1:
   print("Your age group is Infant")
elif age  > 1 and age  <=5:
    print ("Your age group is Toddler")
elif age >= 6 and age <= 12:
    print("Your age group is Child")
elif age >= 13 and age <= 19:
    print("Your age group is Tennager")
elif age >=20 and age <= 60:
    print("Your age group is Adults")
elif age >=60 and age <= 100:
    print("Your age group is Elderly")
else:
    print ("Wrong input")