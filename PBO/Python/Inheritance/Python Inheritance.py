class BangunDatar:
    def Luas(self):
        print("\nMenghitung Luas Bangun Datar")
    def Keliling(self):
        print("Menghitung Keliling Bangun Datar\n")

class Persegi(BangunDatar):
    def sisi(self):
        pass

class PersegiPanjang(BangunDatar):
    def panjang(self):
        pass
    def lebar(self):
        pass

class Segitiga(BangunDatar):
    def alas(self):
        pass
    def tinggi(self):
        pass

class Lingkaran(BangunDatar):
    def jari(self):
        pass

class Main(object):
    print("===== Menghitung Luas dan Keliling Bangun Datar =====")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    menu = int(input("Pilih Menu (1-4): "))

    bangundatar = BangunDatar()
    bangundatar.Luas()
    bangundatar.Keliling()

    if menu==1:

        print("===== Persegi =====")
        persegi=Persegi()
        persegi.sisi = int(input("Masukkan Sisi : "))
        persegi.Luas()
        persegi.Keliling()

    elif menu==2:
        print("===== Persegi Panjang =====")
        persegipanjang=PersegiPanjang()
        persegipanjang.panjang = int(input("Masukkan Panjang : "))
        persegipanjang.lebar = int(input("Masukkan Lebar : "))
        persegipanjang.Luas()
        persegipanjang.Keliling()

    elif menu==3:
        print("===== Segitiga =====")
        segitiga=Segitiga()
        segitiga.alas = int(input("Masukkan Alas : "))
        segitiga.tinggi = int(input("Masukkan Tinggi : "))
        segitiga.Luas()
        segitiga.Keliling()

    elif menu==4:
        print("===== Lingkaran =====")
        lingkaran=Lingkaran()
        lingkaran.jari = int(input("Masukkan Jari-Jari : "))
        lingkaran.Luas()
        lingkaran.Keliling()
        
    else :
        print("Masukkan angka (1-4)")
        pass