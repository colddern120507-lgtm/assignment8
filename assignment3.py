class Elevator:
    def __init__(self, tang_duoi_cung, tang_tren_cung):
        self.tang_duoi_cung = tang_duoi_cung
        self.tang_tren_cung = tang_tren_cung
        self.tang_now = tang_duoi_cung

    def lentang(self):
        if self.tang_now < self.tang_tren_cung:
            self.tang_now += 1
            print("len tang", self.tang_now)

    def xuongtang(self):
        if self.tang_now > self.tang_duoi_cung:
            self.tang_now -= 1
            print("xuong tang", self.tang_now)

    def di_den_tang(self, tang_muctieu):
        while self.tang_now < tang_muctieu:
            self.lentang()
        while self.tang_now > tang_muctieu:
            self.xuongtang()


class Building:
    def __init__(self, tang_duoi_cung, tang_tren_cung, so_thang_may):
        self.tang_duoi_cung = tang_duoi_cung
        self.danh_sach_thang_may = []
        for i in range(so_thang_may):
            self.danh_sach_thang_may.append(Elevator(tang_duoi_cung, tang_tren_cung))

    def run_elevator(self, so_thang, tang_muctieu):
        self.danh_sach_thang_may[so_thang].di_den_tang(tang_muctieu)

    def fire_alarm(self):
        print("chay nha roi lang nuoc oi")   # <-- dòng m đang thiếu
        for thang in self.danh_sach_thang_may:
            thang.di_den_tang(self.tang_duoi_cung)


toa_nha = Building(1, 10, 2)

toa_nha.run_elevator(0, 5)
toa_nha.run_elevator(1, 3)

toa_nha.fire_alarm()