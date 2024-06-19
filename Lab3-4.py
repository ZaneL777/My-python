def sum_numbers(numbers):
    return sum(numbers)
n = int(input("ใส่จำนวนเต็มที่จะป้อน: "))
numbers = []
for i in range(n):
    num = int(input("ใส่จำนวนเต็มที่จะป้อน{i+1}: "))
    numbers.append(num)
    result = sum_numbers(numbers)
    print(f"ผลลัพธ์ที่ีได้ต่อ{result}")