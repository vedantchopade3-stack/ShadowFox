height=float(input("Enter the height of the  in meters: "))
weight=float(input("Enter the weight of the  in kg: "))
bmi=weight/(height*height)
print("The BMI of the person is:", bmi)
if bmi >=30:
    print("Obesity")
elif bmi >=25 and bmi <29:
    print("Overweight")
elif bmi >=18.5 and bmi <25:
    print("Normal weight")          
else:
    print("Underweight")