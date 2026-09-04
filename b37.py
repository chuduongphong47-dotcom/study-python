ngay = int(input())
thang = int(input())
nam = int(input())

print("Ngay hien tai:", ngay, "/", thang, "/", nam)

def ngay_tiep_theo(ngay, thang, nam):
    if thang == 4 or thang == 6 or thang == 9 or thang == 11:
        so_ngay_trong_thang = 30
    elif thang == 2:
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 31

    ngay = ngay + 1
    if ngay > so_ngay_trong_thang:
        ngay = 1
        thang = thang + 1
        if thang > 12:
            thang = 1
            nam = nam + 1
    return ngay, thang, nam

ngay, thang, nam = ngay_tiep_theo(ngay, thang, nam)
print("Ngay tiep theo:", ngay, "/", thang,"/", nam)