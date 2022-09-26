using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpOverride
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===== Bangun Datar =====");
            Console.WriteLine("1. Persegi");
            Console.WriteLine("2. Persegi Panjang");
            Console.WriteLine("3. Segitiga");
            Console.WriteLine("4. Lingkaran");
            Console.Write("Pilih Menu (1-4) : ");
            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.WriteLine("======= Persegi =======");
                    Persegi persegi = new Persegi();
                    Console.Write("Sisi : ");
                    persegi.sisi = int.Parse(Console.ReadLine());
                    Console.WriteLine("\nLuas Persegi : {0}", persegi.luas());
                    Console.WriteLine("Keliling Persegi : {0}", persegi.keliling());
                    break;

                case 2:
                    Console.WriteLine("====== Persegi Panjang ======");
                    PersegiPanjang persegipanjang = new PersegiPanjang();
                    Console.Write("Panjang : ");
                    persegipanjang.panjang = int.Parse(Console.ReadLine());
                    Console.Write("Lebar : ");
                    persegipanjang.lebar = int.Parse(Console.ReadLine());
                    Console.WriteLine("\nLuas Persegi Panjang : {0}", persegipanjang.luas());
                    Console.WriteLine("Keliling Persegi Panjang : {0}", persegipanjang.keliling());
                    break;

                case 3:
                    Console.WriteLine("======= Segitiga =======");
                    Segitiga segitiga = new Segitiga();
                    Console.Write("Alas : ");
                    segitiga.alas = int.Parse(Console.ReadLine());
                    Console.Write("Tinggi : ");
                    segitiga.tinggi = int.Parse(Console.ReadLine());
                    Console.WriteLine("\nLuas Segitiga : {0}", segitiga.luas());
                    break;

                case 4:
                    Console.WriteLine("======= Lingkaran =======");
                    Lingkaran lingkaran = new Lingkaran();
                    Console.Write("Jari-Jari : ");
                    lingkaran.jari = int.Parse(Console.ReadLine());
                    Console.WriteLine("\nLuas Lingkaran : {0}", lingkaran.luas());
                    Console.WriteLine("Keliling Lingkaran : {0}", lingkaran.keliling());
                    break;

                default:
                    Console.WriteLine("Input angka (1-4)");
                    break;
            }
        }
        public abstract class BangunDatar
        {
            public double _hitung;
            public double Hitung
            {
                get { return _hitung; }
                set { _hitung = value; }
            }
            public abstract double luas();
            public abstract double keliling();
        }
        class Persegi : BangunDatar
        {
            private double s;
            public double sisi
            {
                get { return s; }
                set { s = value; }
            }
            public override double luas()
            {
                _hitung = s * s;
                return _hitung;
            }
            public override double keliling()
            {
                _hitung = s * 4;
                return _hitung;
            }
        }
        class PersegiPanjang : BangunDatar
        {
            private float p, l;
            public float panjang
            {
                get { return p; }
                set
                {
                    p = value;
                }
            }
            public float lebar
            {
                get { return l; }
                set
                {
                    l = value;
                }
            }
            public override double luas()
            {
                _hitung = p * l;
                return _hitung;
            }
            public override double keliling()
            {
                float _hitung = 2 * panjang + 2 * lebar;
                return _hitung;
            }
        }
        class Segitiga : BangunDatar
        {
            private float a, t;
            public float alas
            {
                get { return a; }
                set
                {
                    a = value;
                }
            }
            public float tinggi
            {
                get { return t; }
                set
                {
                    t = value;
                }
            }
            public override double luas()
            {
                _hitung = (a * t) / 2;
                return _hitung;
            }
            public override double keliling()
            {
                throw new NotImplementedException();
            }
        }
        class Lingkaran : BangunDatar
        {
            private double r;
            public double jari
            {
                get { return r; }
                set
                {
                    r = value;
                }
            }
            public override double luas()
            {
                _hitung = 3.14 * r * r;
                return _hitung;
            }
            public override double keliling()
            {
                float _hitung = (float)(2 * Math.PI * r);
                return _hitung;
            }
        }
    }
}