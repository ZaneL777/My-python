def abc(num):
    sum = 0
    for i in range(num):
        price = float(input("รับราคาสินค้าที่ %d: " % (i+1)))
        sum += price
    return sum
def Tax(sum):
    vat = sum * 7 / 100
    return vat
def Dis(sum):
    z = (((sum+((sum*7)/100))*5)/100)
    return z
def total(a,b,c):
    t =a + b - c
    return t
num = int(input("จำนวนสินค้า: "))
sum = abc(num)
print("ราคารวม : %.2f" % sum)
print("ภาษี7%% : %.2f" % Tax(sum))
print("ส่วนลด5%% : %.2f" % Dis(sum))
print("รวมทั้งหมดที่ต้องจ่าย : %.2f" % total(sum, Tax(sum),Dis(sum)))