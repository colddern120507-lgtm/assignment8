import random


class Car:
    def __init__(self, bien_so, toc_do_toi_da):
        self.bien_so = bien_so
        self.toc_do_toi_da = toc_do_toi_da
        self.toc_do_hien_tai = 0
        self.quang_duong = 0

    def drive(self, gio):
        self.quang_duong += self.toc_do_hien_tai * gio


class Race:
    def __init__(self, ten, quang_duong, danh_sach_xe):
        self.ten = ten
        self.quang_duong = quang_duong
        self.danh_sach_xe = danh_sach_xe

    def hour_passes(self):
        for xe in self.danh_sach_xe:
            thay_doi = random.randint(-10, 15)
            xe.toc_do_hien_tai += thay_doi

            if xe.toc_do_hien_tai < 0:
                xe.toc_do_hien_tai = 0
            if xe.toc_do_hien_tai > xe.toc_do_toi_da:
                xe.toc_do_hien_tai = xe.toc_do_toi_da

            xe.drive(1)

    def print_status(self):
        print("\ntrang thai:")
        for xe in self.danh_sach_xe:
            print(xe.bien_so, xe.toc_do_hien_tai, xe.quang_duong)

    def race_finished(self):
        for xe in self.danh_sach_xe:
            if xe.quang_duong >= self.quang_duong:
                return True
        return False

danh_sach_xe = []

for i in range(10):
    xe = Car("xecualongdz-" + str(i+1), random.randint(100, 200))
    danh_sach_xe.append(xe)

cuoc_dua = Race("Grand Demolition Derby", 8000, danh_sach_xe)

gio = 0

while not cuoc_dua.race_finished():
    gio += 1
    cuoc_dua.hour_passes()

    if gio % 10 == 0:
        cuoc_dua.print_status()

cuoc_dua.print_status()
print("ket thuc sau", gio, "gio")