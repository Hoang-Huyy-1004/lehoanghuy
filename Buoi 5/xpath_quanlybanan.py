from lxml import etree

# ====== Đọc file XML ======
tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

print("\n===== KẾT QUẢ TRUY VẤN XPATH =====\n")

# Câu 1
print("Câu 1: Lấy tất cả bàn")
xpath1 = "/QUANLY/BANS/BAN/TENBAN/text()"
result1 = root.xpath(xpath1)
for val in result1:
    print(f"→ {val}")
print("-" * 70)

# Câu 2
print("Câu 2: Lấy tất cả nhân viên")
xpath2 = "/QUANLY/NHANVIENS/NHANVIEN/TENV/text()"
result2 = root.xpath(xpath2)
for val in result2:
    print(f"→ {val}")
print("-" * 70)

# Câu 3
print("Câu 3: Lấy tất cả tên món")
xpath3 = "/QUANLY/MONS/MON/TENMON/text()"
result3 = root.xpath(xpath3)
for val in result3:
    print(f"→ {val}")
print("-" * 70)

# Câu 4
print("Câu 4: Lấy tên nhân viên có mã NV02")
xpath4 = "/QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV/text()"
result4 = root.xpath(xpath4)
for val in result4:
    print(f"→ {val}")
print("-" * 70)

# Câu 5
print("Câu 5: Lấy tên và số điện thoại của nhân viên NV03")
xpath5 = "/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/*[self::TENV or self::SDT]/text()"
result5 = root.xpath(xpath5)
for val in result5:
    print(f"→ {val}")
print("-" * 70)

# Câu 6
print("Câu 6: Lấy tên món có giá > 50,000")
xpath6 = "/QUANLY/MONS/MON[GIA>50000]/TENMON/text()"
result6 = root.xpath(xpath6)
for val in result6:
    print(f"→ {val}")
print("-" * 70)

# Câu 7
print("Câu 7: Lấy số bàn của hóa đơn HD03")
xpath7 = "/QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN/text()"
result7 = root.xpath(xpath7)
for val in result7:
    print(f"→ {val}")
print("-" * 70)

# Câu 8
print("Câu 8: Lấy tên món có mã M02")
xpath8 = "/QUANLY/MONS/MON[MAMON='M02']/TENMON/text()"
result8 = root.xpath(xpath8)
for val in result8:
    print(f"→ {val}")
print("-" * 70)

# Câu 9
print("Câu 9: Lấy ngày lập của hóa đơn HD03")
xpath9 = "/QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP/text()"
result9 = root.xpath(xpath9)
for val in result9:
    print(f"→ {val}")
print("-" * 70)

# Câu 10
print("Câu 10: Lấy tất cả mã món trong hóa đơn HD01")
xpath10 = "/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()"
result10 = root.xpath(xpath10)
for val in result10:
    print(f"→ {val}")
print("-" * 70)

# Câu 11
print("Câu 11: Lấy tên món trong hóa đơn HD01")
xpath11 = "/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()"
result11 = root.xpath(xpath11)
for val in result11:
    print(f"→ {val}")
print("-" * 70)

# Câu 12
print("Câu 12: Lấy tên nhân viên lập hóa đơn HD02")
xpath12 = "/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV/text()"
result12 = root.xpath(xpath12)
for val in result12:
    print(f"→ {val}")
print("-" * 70)

# Câu 13
print("Câu 13: Đếm số bàn")
xpath13 = "count(/QUANLY/BANS/BAN)"
result13 = root.xpath(xpath13)
print(f"→ {int(result13)}")
print("-" * 70)

# Câu 14
print("Câu 14: Đếm số hóa đơn lập bởi NV01")
xpath14 = "count(/QUANLY/HOADONS/HOADON[MANV='NV01'])"
result14 = root.xpath(xpath14)
print(f"→ {int(result14)}")
print("-" * 70)

# Câu 15
print("Câu 15: Lấy tên tất cả món có trong hóa đơn của bàn số 2")
xpath15 = "/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()"
result15 = root.xpath(xpath15)
for val in result15:
    print(f"→ {val}")
print("-" * 70)

# Câu 16
print("Câu 16: Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3")
xpath16 = "/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]/TENV/text()"
result16 = root.xpath(xpath16)
for val in result16:
    print(f"→ {val}")
print("-" * 70)

# Câu 17
print("Câu 17: Lấy tất cả hóa đơn mà nhân viên nữ lập")
xpath17 = "/QUANLY/HOADONS/HOADON[MANV=/QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()"
result17 = root.xpath(xpath17)
for val in result17:
    print(f"→ {val}")
print("-" * 70)

# Câu 18
print("Câu 18: Lấy tất cả nhân viên từng phục vụ bàn số 1")
xpath18 = "/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]/TENV/text()"
result18 = root.xpath(xpath18)
for val in result18:
    print(f"→ {val}")
print("-" * 70)

# Câu 19
print("Câu 19: Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn")
xpath19 = "/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON/CTHDS/CTHD[SOLUONG>1]/MAMON]/TENMON/text()"
result19 = root.xpath(xpath19)
for val in result19:
    print(f"→ {val}")
print("-" * 70)

# Câu 20
print("Câu 20: Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'")
xpath20 = "/QUANLY/BANS/BAN[SOBAN=/QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN/text()"
result20 = root.xpath(xpath20)
for val in result20:
    print(f"→ {val}")
print("-" * 70)

print("\n===== KẾT THÚC =====")
