import random

Hayvanlar = []
Avlanma_sayisi = 0
Ureme_sayisi = 0

class Hayvan:
    def __init__(self, Tur, Cinsiyet, x, y, Hareket_kabiliyeti):
        self.Tur = Tur
        self.Cinsiyet = Cinsiyet
        self.x = x
        self.y = y
        self.Hareket_kabiliyeti = Hareket_kabiliyeti

    @classmethod
    def Yeni_Hayvan_Ekle(cls, Tur, Cinsiyet, Adet, Hareket_kabiliyeti):
        Yeni_Hayvan = []
        Hareket_kabiliyeti = Hareket_kabiliyeti
        for i in range(Adet):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            Yeni_Hayvan.append(cls(Tur, Cinsiyet, x, y,Hareket_kabiliyeti))
        return Yeni_Hayvan

    def Hareket(self):
        dx = random.randint(-self.Hareket_kabiliyeti, self.Hareket_kabiliyeti)
        dy = random.randint(-self.Hareket_kabiliyeti, self.Hareket_kabiliyeti)
        self.x += dx
        self.y += dy
        # Sınırları kontrol etme
        self.x = max(0, min(self.x, 500))
        self.y = max(0, min(self.y, 500))

    def Ureme(self,Hayvanlar):
        for Hayvan in Hayvanlar:
            if self == Hayvan:  # Kendisiyle eşleşmeye çalışmamak için
                return False

            if (Hayvan.Tur == self.Tur) and (Hayvan.Cinsiyet != self.Cinsiyet):
                Mesafe = ((self.x - Hayvan.x) ** 2 + (self.y - Hayvan.y) ** 2) ** 0.5
                if Mesafe >=0 and Mesafe <= 3:
                    return True
                else:
                    return False

            elif (self.Tur == "Tavuk" and Hayvan.Tur == "Horoz") or (self.Tur == "Horoz" and Hayvan.Tur == "Tavuk"):
                Mesafe = ((self.x - Hayvan.x) ** 2 + (self.y - Hayvan.y) ** 2) ** 0.5
                if Mesafe >=0 and Mesafe <= 3:
                    return True
                else:
                    return False

    def Avlanma(self):
        Avlanma_Kosul = {
            'Kurt': ['Koyun', 'Tavuk', 'Horoz'],
            'Aslan': ['İnek', 'Koyun'],
            'Avcı': ['Koyun', 'Tavuk', 'Horoz', 'İnek']}

        Avlanma_Kosul_ = Avlanma_Kosul.get(self.Tur, [])
        for Hayvan in Hayvanlar:
            if Hayvan.Tur in Avlanma_Kosul_:
                Mesafe = ((self.x - Hayvan.x) ** 2 + (self.y - Hayvan.y) ** 2) ** 0.5
                if (self.Tur == 'Kurt' and (Mesafe >= 0 and Mesafe <= 4)) or \
                        (self.Tur == 'Aslan' and (Mesafe >= 0 and  Mesafe <= 5)) or \
                        (self.Tur == 'Avcı' and (Mesafe >= 0 and  Mesafe <= 8)):
                    Hayvanlar.remove(Hayvan) # Avlanılan hayvanı silme
                    global Avlanma_sayisi
                    Avlanma_sayisi += 1
                    print(f"{self.Tur} {self.Cinsiyet} avladı: {Hayvan.Tur} {Hayvan.Cinsiyet}")


Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Koyun", "Erkek", 15,2))
Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Koyun", "Dişi", 15,2))

Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("İnek", "Erkek", 5,2))
Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("İnek", "Dişi", 5,2))

Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Tavuk", "Dişi", 10,1))
Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Horoz", "Erkek", 10,1))

Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Kurt", "Erkek", 5,3))
Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Kurt", "Dişi", 5,3))

Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Aslan", "Erkek", 4,4))
Hayvanlar.extend(Hayvan.Yeni_Hayvan_Ekle("Aslan", "Dişi", 4,4))

Hayvanlar.append(Hayvan("Avcı", "İnsan", 0, 0,1))

print("Hayvan Çiftliğinin İlk Hali\n")
for Hayvan in Hayvanlar:
    print(f"{Hayvan.Cinsiyet} {Hayvan.Tur} Konumu ({Hayvan.x}, {Hayvan.y}) Hareket Kabiliyeti: {Hayvan.Hareket_kabiliyeti})")

print("---------------------------------------------")
print("1000 Adımlık Döngü Başlangıcı\n")

for i in range(1000):
    for Hayvan in Hayvanlar:
        Hayvan.Hareket()
        Hayvan.Avlanma()
        if Hayvan.Ureme(Hayvanlar):
            Cinsiyet = random.choice(["Erkek", "Dişi"])
            Yeni_hayvanlar = Hayvan.Yeni_Hayvan_Ekle(Hayvan.Tur, Cinsiyet, 1, Hayvan.Hareket_kabiliyeti)
            Hayvanlar.extend(Yeni_hayvanlar)
            Yeni_dogan = Yeni_hayvanlar[-1]
            print(f"Yeni Doğan {Yeni_dogan.Cinsiyet} {Yeni_dogan.Tur} Konumu ({Yeni_dogan.x}, {Yeni_dogan.y}) Hareket Kabiliyeti {Yeni_dogan.Hareket_kabiliyeti})")
            Ureme_sayisi += 1
    print(f"{i}. döngü")


Toplam_hayvan_sayisi = len(Hayvanlar)
print("\n\n\n1000 adımlık döngü sonucu :\n")
print(f"Toplam Üreme Sayısı: {Ureme_sayisi}")
print(f"Toplam Avlanma Sayısı: {Avlanma_sayisi}")
print(f"Kalan Toplam Hayvan Sayısı: {Toplam_hayvan_sayisi}")
print("\n\nKalan Hayvan Türleri ve Adetleri :")

Hayvan_sayilari = {}
for Hayvan in Hayvanlar:
    Tur = Hayvan.Tur
    Hayvan_sayilari[Tur] = Hayvan_sayilari.get(Tur, 0) + 1

for Tur, count in Hayvan_sayilari.items():
    print(f"{Tur}: {count} adet")

