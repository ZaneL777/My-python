score = float(input("รับค่าคะแนน: "))
if 80 <= score <= 100:
    print("เกรด:A")
elif 70 <= score <= 79:
    print("เกรด:B")
elif 60 <= score <= 69:
    print("เกรด:C")
elif 50 <= score <= 59:
    print("เกรด:D")
elif 40 <= score <= 49:
    print("เกรด:E")
elif 0 <= score < 40:
    print("เกรด:F")
else:
    print("กรุณากรอกคะแนนให้ถูกต้อง")