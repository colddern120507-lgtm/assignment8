class Elevator:
    def __init__(self, tang_duoi_cung, tang_tren_cung):
        self.tang_duoi_cung = tang_duoi_cung
        self.tang_tren_cung = tang_tren_cung
        self.tang_now = tang_duoi_cung
    def lentang(self):
        if self.tang_now < self.tang_tren_cung:
            self.tang_now += 1
            print(f"dilen -> tang {self.tang_now}")

    def xuongtang(self):
        if self.tang_now > self.tang_duoi_cung:
            self.tang_now -= 1
            print(f"dixuong -> tang {self.tang_now}")

    def di_den_tang(self, tang_muctieu):
        while self.tang_now < tang_muctieu:
            self.lentang()
        while self.tang_now > tang_muctieu:
            self.xuongtang()

lift = Elevator(1, 10)

lift.di_den_tang(5)
lift.di_den_tang(1)