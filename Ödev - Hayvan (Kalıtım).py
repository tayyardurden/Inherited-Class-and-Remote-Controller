class Canlılar():
    def __init__(self, isim, boy, uzunluk, ağırlık, habitat, beslenme_şekli):  
        self.isim = isim
        self.boy = boy
        self.uzunluk = uzunluk
        self.ağırlık = ağırlık
        self.habitat = habitat
        self.beslenme_şekli = beslenme_şekli

    def bilgileri_goster(self):
        print("Canlıların bilgileri...")
        print("İsim : {}\n Boy: {}\n Uzunluk: {}\n Ağırlık: {}\n Habitat: {}\n Beslenme şekli: {}\n".format(self.isim, self.boy, self.uzunluk, self.ağırlık, self.habitat, self.beslenme_şekli))


class Dinozor(Canlılar):
    def tür_belirle(self, tür):
        self.tür = tür

Velociraptor = Dinozor("Velociraptor", 2.5, 3.5, 100, "Orman", "Etçil")
Velociraptor.bilgileri_goster()
Velociraptor.tür_belirle("Zibidazor")
print(Velociraptor.tür)

Trex = Dinozor("Trex", 3.5, 4.5, 200, "Orman", "Etçil")
Trex.bilgileri_goster()
Trex.tür_belirle("Tiranozor")
print(Trex.tür)

class Kuşlar(Canlılar):
    def cinsiyet_belirle(self, cinsiyet):
        self.cinsiyet = cinsiyet

Kartal = Kuşlar("Kartal", "1m", "2m", "5kg", "Orta Asya", "Etçil")
Kartal.bilgileri_goster()
Kartal.cinsiyet_belirle("Dişi")
print(Kartal.cinsiyet)

Kanarya = Kuşlar("Kanarya", "20cm", "30cm", "50g", "Orta Asya", "Otçul")
Kanarya.bilgileri_goster()
Kanarya.cinsiyet_belirle("Erkek")
print(Kanarya.cinsiyet)

class Balıklar(Canlılar):
    def bulunduğu_bölge(self, bölge):
        self.bölge = bölge

Köpekbalığı = Balıklar("Köpekbalığı", "1m", "2m", "5kg", "Akdeniz", "Etçil")
Köpekbalığı.bilgileri_goster()
Köpekbalığı.bulunduğu_bölge("Akdeniz")
print(Köpekbalığı.bölge)

Hamsi = Balıklar("Hamsi", "20cm", "30cm", "50g", "Akdeniz", "Otçul")
Hamsi.bilgileri_goster()
Hamsi.bulunduğu_bölge("Karadeniz")
print(Hamsi.bölge)

Pattaya = Balıklar("Pattaya", "20cm", "30cm", "50g", "Karadeniz", "Otçul")
Pattaya.bilgileri_goster()
Pattaya.bulunduğu_bölge("Karadeniz")
print(Pattaya.bölge)



