
nguoi = input("Nhập: ")

while nguoi not in ['kéo', 'búa', 'bao']:
    print("Nhập không hợp lệ. Vui lòng nhập lại.")
    nguoi = input("Nhập: ")

import random as rd

may = rd.choice(['kéo', 'búa', 'bao'])

print("Máy ra: ", may)

def kq(nguoi, may):
    if nguoi == may:
        print("Hòa")
    elif (nguoi == 'kéo' and may == 'bao') or (nguoi == 'búa' and may == 'kéo') or (nguoi == 'bao' and may == 'búa'):
        print("Bạn thắng")
    else:
        print("Bạn thua")

kq(nguoi, may)

