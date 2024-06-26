def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

weight_kg = 125  
height_m = 1.75  

bmi = calculate_bmi(weight_kg, height_m)
print("BMI ของคุณคือ %.2f" % bmi)
