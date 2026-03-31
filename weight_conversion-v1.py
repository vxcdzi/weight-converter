# Weight Converter (Kilograms to Pounds)
og_weight = float(input("Enter the weight (no units): ")) # Weight inputted by the user
og_unit = input("Enter unit of weight inputted (K for kilogram and L for pound) ") # Unit of the weight inputted by the user

if (og_unit == "K") or (og_unit == "k"):
    new_weight = og_weight*2.205 # conversion of weight into pounds if weight given by the user is in kilograms
    new_unit = "lbs"
    print(f"The weight after conversion to pounds is {new_weight} {new_unit}")
elif (og_unit == "L") or (og_unit == "l") :
     new_weight = og_weight/2.205 # conversion of weight into kilograms if weight given by the user is in pounds
     new_unit = "kg"
     print(f"The weight after conversion to kilograms is {new_weight} {new_unit}")

else:
    print("Enter the correct unit!!")