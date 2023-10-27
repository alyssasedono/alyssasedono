kendaraan=["mobil", "SUV", "toyota", 1500]
kendaraan.append("hitam")
kendaraan.append("4 buah ban")
kendaraan.append("694 juta")
kendaraan.remove("mobil")

print(kendaraan)

pilih = input("masukan pilihan: ")
match pilih:
    case "luas kotak":
       print("sisi*sisi*sisi")
    case "luas lingkaran":
       print("22/7*pi*r*r")
    case "luas segitiga":
       print("1/2*alas*tinggi")
    case _:
       print("masukan kembali pilihan")