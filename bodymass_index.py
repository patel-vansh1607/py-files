print("--------------------")
print("This code shows you your body mass index")
print("--------------------")

height = float(input("Enter your height: "))
height_units = float(input("Press 1 if height in cm and press 2 if height in m: "))
print("---------------------------------------------------------------------")

if height_units == 1:
    convert = height / 100

else:
    height_units == height_units

print("---------------------------------------------------------------------")
weight = float(input("Enter your weight: "))
weight_units = float(input("Press 1 if weight in g and press 2 if weight in kg: "))
print("---------------------------------------------------------------------")

if weight_units == 1:
    weight_units= weight / 1000
else:
    weight_units  == weight_units  

print("********************************")

bodymassindex = weight  / (height**2)
print("your body mass index is", bodymassindex) 