Kumanda dosyasına eklenen özellikler : 
  
   1) DOKUNMATİK EKRAN

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
                
   2)YAZILIM GÜNCELLE
  
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
   
   
   
   
   3)ŞARJ SEVİYESİ
   
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
      
