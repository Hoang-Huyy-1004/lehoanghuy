from lxml import etree

# ====== Đọc file XML ======
tree = etree.parse("sv.xml")
root = tree.getroot()

print("\n===== KẾT QUẢ TRUY VẤN XPATH =====\n")

# Câu 1
print("Câu 1: Lấy tất cả sinh viên")
xpath1 = "/school/student"
result1 = root.xpath(xpath1)
for sv in result1:
    id_ = sv.findtext("id")
    name = sv.findtext("name")
    date = sv.findtext("date")
    print(f" {id_}: {name} ({date})")
print("-" * 70)

# Câu 2
print("Câu 2: Liệt kê tên tất cả sinh viên")
xpath2 = "/school/student/name/text()"
result2 = root.xpath(xpath2)
for name in result2:
    print(f" {name}")
print("-" * 70)

# Câu 3
print("Câu 3: Lấy tất cả id của sinh viên")
xpath3 = "/school/student/id/text()"
result3 = root.xpath(xpath3)
for id_ in result3:
    print(f" {id_}")
print("-" * 70)

# Câu 4
print("Câu 4: Lấy ngày sinh của sinh viên có id = 'SV01'")
xpath4 = "/school/student[id='SV01']/date/text()"
result4 = root.xpath(xpath4)
for date in result4:
    print(f" {date}")
print("-" * 70)

# Câu 5
print("Câu 5: Lấy các khóa học")
xpath5 = "/school/enrollment/course/text()"
result5 = root.xpath(xpath5)
for course in result5:
    print(f" {course}")
print("-" * 70)

# Câu 6
print("Câu 6: Lấy toàn bộ thông tin của sinh viên đầu tiên")
xpath6 = "/school/student[1]/*"
result6 = root.xpath(xpath6)
for node in result6:
    print(f" <{node.tag}> {node.text}")
print("-" * 70)

# Câu 7
print("Câu 7: Lấy mã sinh viên đăng ký khóa học 'Vatly203'")
xpath7 = "/school/enrollment[course='Vatly203']/studentRef/text()"
result7 = root.xpath(xpath7)
for ref in result7:
    print(f" {ref}")
print("-" * 70)

# Câu 8
print("Câu 8: Lấy tên sinh viên học môn 'Toan101'")
xpath8 = "/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()"
result8 = root.xpath(xpath8)
for name in result8:
    print(f" {name}")
print("-" * 70)

# Câu 9
print("Câu 9: Lấy tên sinh viên học môn 'Vatly203'")
xpath9 = "/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()"
result9 = root.xpath(xpath9)
for name in result9:
    print(f" {name}")
print("-" * 70)

# Câu 10
print("Câu 10: Lấy ngày sinh của sinh viên có id='SV01'")
xpath10 = "/school/student[id='SV01']/date/text()"
result10 = root.xpath(xpath10)
for date in result10:
    print(f" {date}")
print("-" * 70)

# Câu 11
print("Câu 11: Lấy tên và ngày sinh của sinh viên sinh năm 1997")
xpath11 = "/school/student[starts-with(date,'1997')]/name/text() | /school/student[starts-with(date,'1997')]/date/text()"
result11 = root.xpath(xpath11)
for val in result11:
    print(f" {val}")
print("-" * 70)

# Câu 12
print("Câu 12: Lấy tên sinh viên có ngày sinh trước năm 1998")
xpath12 = "/school/student[number(substring(date,1,4)) < 1998]/name/text()"
result12 = root.xpath(xpath12)
for name in result12:
    print(f" {name}")
print("-" * 70)

# Câu 13
print("Câu 13: Đếm tổng số sinh viên")
xpath13 = "count(/school/student)"
result13 = root.xpath(xpath13)
print(f" {int(result13)}")
print("-" * 70)

# Câu 14
print("Câu 14: Lấy tất cả sinh viên chưa đăng ký môn nào")
xpath14 = "/school/student[not(id = /school/enrollment/studentRef)]/name/text()"
result14 = root.xpath(xpath14)
for name in result14:
    print(f" {name}")
print("-" * 70)

# Câu 15
print("Câu 15: Lấy phần tử <date> anh em ngay sau <name> của SV01")
xpath15 = "/school/student[id='SV01']/name/following-sibling::date"
result15 = root.xpath(xpath15)
for node in result15:
    print(f" <{node.tag}> {node.text}")
print("-" * 70)

# Câu 16
print("Câu 16: Lấy phần tử <id> anh em ngay trước <name> của SV02")
xpath16 = "/school/student[id='SV02']/name/preceding-sibling::id"
result16 = root.xpath(xpath16)
for node in result16:
    print(f" <{node.tag}> {node.text}")
print("-" * 70)

# Câu 17
print("Câu 17: Lấy toàn bộ node <course> trong enrollment có studentRef='SV03'")
xpath17 = "/school/enrollment[studentRef='SV03']/course"
result17 = root.xpath(xpath17)
for node in result17:
    print(f" <{node.tag}> {node.text}")
print("-" * 70)

# Câu 18
print("Câu 18: Lấy sinh viên có họ là 'Trần'")
xpath18 = "/school/student[starts-with(name,'Trần')]/name/text()"
result18 = root.xpath(xpath18)
for name in result18:
    print(f" {name}")
print("-" * 70)

# Câu 19
print("Câu 19: Lấy năm sinh của sinh viên SV01")
xpath19 = "substring(/school/student[id='SV01']/date,1,4)"
result19 = root.xpath(xpath19)
print(f" {result19}")
print("-" * 70)

print("\n===== KẾT THÚC =====")