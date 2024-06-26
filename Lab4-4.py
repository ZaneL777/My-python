std = {
    'name': "Sunithi",
    "age":16,
    'gpa':2.50,
    "old_school":"โรงเรียนสารสาสน์วิเทศธนบุรี"
    }
print(std)
print("สวัสดีครับ %s"%(std["name"]))
print("อายุ %d เกรดเฉลี่ย %.2f จบจาก %s  " % (std["age"] , std["gpa"] , std["old_school"]))