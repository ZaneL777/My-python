def CTF(C):
    F = (C * 9/5) + 32
    return F
def CTK(C):
    K = C + 273.15
    return K
celsius = float(input("ป้อนอุณหภูมิเซลเซียส: "))
fahrenheit = CTF(celsius)
kelvin = CTK(celsius)
print(f"อุณหภูมิ : {celsius}C เท่ากับ : {fahrenheit:.2f}F")
print(f"อุณหภูมิ : {celsius}C เท่ากับ : {kelvin:.2f}K")