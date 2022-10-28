class PCLab():
    def __init__(self, sınıf_kodu = "CS505", bilgisayar_sayısı = 30, server_kapasitesi = "Tam Dolu", doluluk_durumu = "Boş", öğrenci_sayısı = 15):
        self.sınıf_kodu = sınıf_kodu
        self.bilgisayar_sayısı = bilgisayar_sayısı
        self.server_kapasitesi = server_kapasitesi
        self.öğrenci_sayısı = öğrenci_sayısı
        self.doluluk_durumu = doluluk_durumu

    def bilgisayar_ekle(self, bilgisayar_sayısı):

        while True:
            cevap = input(f"Mevcut bilgisayar sayısı : {self.bilgisayar_sayısı}, bilgisayar sayısını 1 arttırmak 1 için '+'\nBilgisayar sayısını azaltmak için '-'\nÇıkış için 'q'\n")

            if cevap == "+":

                if self.bilgisayar_sayısı != 0:
                    self.bilgisayar_sayısı += 1
                    print("Bilgisayar Sayısı:", self.bilgisayar_sayısı)

            elif cevap == "-":
                if self.bilgisayar_sayısı != 31:
                    self.bilgisayar_sayısı -= 1
                    print("Bilgisayar Sayısı:", self.bilgisayar_sayısı)

            else:
                print("Bilgisayar sayısı güncellendi:", self.bilgisayar_sayısı)
                break

    def server_kapasitesi_göster(self):

        if self.öğrenci_sayısı > self.bilgisayar_sayısı:
            print("Server kapasitesi dolu.")

        else:
            print("Server kapasitesi boş.")

    def doluluk_durumu_göster(self):

        if self.öğrenci_sayısı > self.bilgisayar_sayısı:
            print("Doluluk Durumu: Dolu")

        else:
            print("Doluluk Durumu: Boş")


    def öğrenci_ekle(self, öğrenci_sayısı):

        while True:
            cevap = input(f" Mevcut sayı: {self.öğrenci_sayısı}, öğrenci sayısını 1 arttırmak için '+'\nÖğrenci sayısını azaltmak için '-'\nÇıkış için 'q'\n")

            if cevap == "+":

                if self.öğrenci_sayısı != 0:
                    self.öğrenci_sayısı += 1
                    print("Öğrenci Sayısı:", self.öğrenci_sayısı)

            elif cevap == "-":

                if self.öğrenci_sayısı != 31:
                    self.öğrenci_sayısı -= 1
                    print("Öğrenci Sayısı:", self.öğrenci_sayısı)

            else:
                print("Öğrenci sayısı güncellendi:", self.öğrenci_sayısı)
                break

    
    def __str__(self):
        return "Sınıf Kodu: {}\nBilgisayar Sayısı: {}\nServer Kapasitesi: {}\nÖğrenci Sayısı: {}\nDoluluk Durumu: {}\n".format(self.sınıf_kodu, self.bilgisayar_sayısı, self.server_kapasitesi, self.öğrenci_sayısı, self.doluluk_durumu)

print("""

    1. Bilgisayar Sayısı
    2. Server Kapasitesi
    3. Doluluk Durumu
    4. Öğrenci Sayısı
    5. Çıkış

""")


while True:
    cevap = input("Seçim Yapınız: ")
    if cevap == "1":
        bilgisayar = PCLab()
        bilgisayar.bilgisayar_ekle(1)
    elif cevap == "2":
        server = PCLab()
        server.server_kapasitesi_göster()
    elif cevap == "3":
        doluluk = PCLab()
        doluluk.doluluk_durumu_göster()
    elif cevap == "4":
        öğrenci = PCLab()
        öğrenci.öğrenci_ekle(1)
    else:
        print("Çıkış Yapılıyor...")
        break