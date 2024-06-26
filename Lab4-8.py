print("หาพื้นที่วงกลม")
def Circle(radius):
    pi = 22 / 7
    area = pi * (radius ** 2) 
    return area
print("พื้นที่วงกลม %.2f" % Circle(5))
print("พื้นที่วงกลม %.2f" % Circle(25))