print ("--------------------------")
print ("Conversion of degrees")
print ("--------------------------")

number_to_convert = int(input("Enter the value you want to convert: "))

temp = int(input("Press 1 to convert from degrees to farenheit OR Press 2 to convert from farenheit to degrees "))

if temp == 1:
    number_to_convert = ((number_to_convert *9/5) +32)
    print("------------------------")
    print("your converted number is", number_to_convert)
    print("------------------------")
elif temp ==2:
    number_to_convert = ((number_to_convert -32 ) *5/9)
    print("------------------------")
    print("your converted number is", number_to_convert)
    print("------------------------")