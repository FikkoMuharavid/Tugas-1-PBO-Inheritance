class BangunDatar:
    def Luas(self):
        print("Menghitung Luas Bangun Datar")
    def Keliling(self):
        print("Menghitung Keliling Bangun Datar\n")

class Persegi(BangunDatar):
    def sisi(self):
        pass
    def Luas(self, sisi):
        Luas = sisi * sisi
        print("\nLuas Persegi = ",Luas)
    def Keliling(self, sisi):
        Keliling = 4 * sisi
        print("Keliling Persegi = ",Keliling)

class PersegiPanjang(BangunDatar):
    def panjang(self):
        pass
    def lebar(self):
        pass
    def Luas(self, panjang, lebar):
        Luas = panjang * lebar
        print("\nLuas Persegi Panjang = ",Luas)
    def Keliling(self, panjang, lebar):
        Keliling = 2 * (panjang+lebar)
        print("Keliling Persegi Panjang = ",Keliling)

class Segitiga(BangunDatar):
    def alas(self):
        pass
    def tinggi(self):
        pass
    def Luas(self, alas, tinggi):
        Luas = 1/2 * (alas * tinggi)
        print("\nLuas Segitiga = ",Luas)

class Lingkaran(BangunDatar):
    def jari(self):
        pass
    def Luas(self, jari):
        Luas = 3.14 * jari * jari
        print("\nLuas Lingkaran = ",Luas)
    def Keliling(self, jari):
        Keliling = 2 * 3.14 * jari
        print("Keliling Lingkaran = ",Keliling)

class Main(object):
    print("===== Menghitung Luas dan Keliling Bangun Datar =====")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    menu = int(input("Pilih Menu : "))

    bangundatar = BangunDatar()
    bangundatar.Luas()
    bangundatar.Keliling()
    
    if menu==1:
        print("======= Persegi== =====")
        persegi = Persegi()
        persegi.sisi = int(input("Masukkan Sisi : "))
        persegi.Luas(persegi.sisi)
        persegi.Keliling(persegi.sisi)

    elif menu==2:
        print("======= Persegi Panjang== =====")
        persegipanjang = PersegiPanjang()
        persegipanjang.panjang = int(input("Masukkan Panjang : "))
        persegipanjang.lebar = int(input("Masukkan Lebar : "))
        persegipanjang.Luas(persegipanjang.panjang, persegipanjang.lebar)
        persegipanjang.Keliling(persegipanjang.panjang, persegipanjang.lebar)

    elif menu==3:
        print("======= Segitiga =======")
        segitiga = Segitiga()
        segitiga.alas = int(input("Masukkan Alas : "))
        segitiga.tinggi = int(input("Masukkan Tinggi : "))
        segitiga.Luas(segitiga.alas, segitiga.tinggi)

    elif menu==4:
        print("======= Lingkaran =======")
        lingkaran = Lingkaran()
        lingkaran.jari = int(input("Masukkan Jari-Jari : "))
        lingkaran.Luas(lingkaran.jari)
        lingkaran.Keliling(lingkaran.jari)

    else :
        print("Masukkan angka (1-4)")
        pass