import time
import random
from datetime import datetime

obj_now = datetime.now()

class Kumanda():
#add computer local minute to şarj_seviyesi
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT", dokunmatik_ekran="Kapalı", yazılım_güncelle = "Kapalı", şarj_seviyesi =obj_now.minute):
        print("Kumanda oluşturuluyor...")

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        self.dokunmatik_ekran = dokunmatik_ekran
        self.yazılım_güncelle = yazılım_güncelle
        self.şarj_seviyesi = şarj_seviyesi
    

     
    def tv_ac(self):
        if (self.tv_durum=="Açık"):
            print("TV zaten açık.")
        else:
            print("TV açılıyor...")
            self.tv_durum="Açık"

    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("TV zaten kapalı.")
        else:
            print("TV kapanıyor...")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
            
            while True:
                cevap=input("Sesi azalt: '<'\nSesi arttır: '>'\nÇıkış: 'q'\n")
    
                if (cevap=="<"):
                    if (self.tv_ses!=0):
                        self.tv_ses-=1
                        print("Ses:",self.tv_ses)
                elif (cevap==">"):
                    if (self.tv_ses!=31):
                        self.tv_ses+=1
                        print("Ses:",self.tv_ses)
                else:
                    print("Ses güncellendi:",self.tv_ses)
                    break
        
    def kanal_ekle(self,kanal_ismi):
        if kanal_ismi in self.kanal_listesi:
            print("Kanal zaten mevcut.")
        else:
            print("Kanal eklendi.")
            self.kanal_listesi.append(kanal_ismi)

            print("Kanal ekleniyor...")
            time.sleep(1)
            
            self.kanal_listesi.append(kanal_ismi)
            print("Kanal eklendi...")
            time.sleep(1)

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def dokunmatik_ekranı_aç(self):
        while True:
            cevap = input ("Dokunmatik ekranı açmak istiyor musunuz? (E/H)")
            if cevap == "E":
                print("Dokunmatik ekran açılıyor...")
                self.dokunmatik_ekran = "Açık"
                if self.dokunmatik_ekran == "Açık":
                    print("Dokunmatik ekran zaten açık.")
                    break

            elif cevap == "H":
                print("Dokunmatik ekranı açmayı reddettiniz, kumanda kapatılıyor.")
                break

            else:
                print("Lütfen E veya H harflerinden birini giriniz.")
                continue
    
    def yazılımı_güncelle(self):
        while True:
            cevap = input ("Yazılım güncellemesini kontrol etmek istiyor musunuz? (E/H)")
            if cevap == "E":
                if self.yazılım_güncelle == "Açık":
                    print("Yazılımınız güncel.")
                    break

                else:
                    print("Yazılım güncellemesi açılıyor...")
                    self.yazılım_güncelle = "Açık"
                    time.sleep(2)
                    print("Yazılım güncellendi")
                    continue
                               
            elif cevap == "H":
                print("Yazılım güncellemesini açmayı reddettiniz, kumanda kapatılıyor.")
                break
            else:
                print("Lütfen E veya H harflerinden birini giriniz.")
                continue

    def şarj_seviyesini_göster(self):
        while True:
            cevap = input ("Şarj seviyesini görmek istiyor musunuz? (E/H)")
            if cevap == "E":
                print("Şarj seviyesi:",self.şarj_seviyesi)
                if self.şarj_seviyesi == 0:
                    print(f"Kumandanın şarjı % {self.şarj_seviyesi}, lütfen şarj ediniz.")
                    break
                elif self.şarj_seviyesi == 100:
                    print(f"Kumandanın şarjı % {self.şarj_seviyesi}, şarjınız dolmuştur.")
                    break
                else:
                    print(f"Kumandanın şarjı % {self.şarj_seviyesi}")
                    break


    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\nDokunmatik ekran: {}\nYazılım güncelleme: {}\nŞarj seviyesi: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal,self.dokunmatik_ekran,self.yazılım_güncelle,self.şarj_seviyesi)

İşlem_menüsü = print("""


    1.TV Aç
    2.TV kapat
    3.Ses ayarları
    4.Kanal ekle
    5.Açık Kanalı Öğren
    6.Kanal Sayısı
    7. TV Bilgileri
    8. Rastgele Kanal
    9. Dokunmatik Ekranı Aç
    10. Yazılımı Güncelle
    11. Şarj Seviyesini Göster
    12. Çıkış

Çıkmak için 'ya basın
""")

while True:
    kumanda=Kumanda()
    işlem=input("İşlemi seçiniz:")
    if (işlem=="q"):
        print("Program sonlandırılıyor...")
        break
    elif (işlem=="1"):
        kumanda.tv_ac()
        break
    elif (işlem=="2"):
        kumanda.tv_kapat()
        break
    elif (işlem=="3"):
        kumanda.ses_ayarları()
        break
    elif (işlem=="4"):
        kanallar=input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz:")
        kanal_listesi=kanallar.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
        break
    elif (işlem=="5"):
        kumanda.rastgele_kanal()
        break
    elif (işlem=="6"):
        print("Kanal sayısı:",len(kumanda))
        break
    elif (işlem=="7"):
        print(kumanda)
        break
    elif (işlem=="8"):
        kumanda.rastgele_kanal()
        break
    elif (işlem=="9"):
        kumanda.dokunmatik_ekranı_aç()
        break
    elif (işlem=="10"):
        kumanda.yazılımı_güncelle()
        break
    elif (işlem=="11"):
        kumanda.şarj_seviyesini_göster()
        break
    else:
        print("Geçersiz işlem...")
        break

