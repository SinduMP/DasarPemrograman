import sys
total = []

#class color
class color:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'


print("-------------------------------")
print("KASIR A")
print("-------------------------------")

def daftar_barang():
    print(color.BLUE + " No | Nama Barang | Harga" + color.END)
    print(color.RED + "-------------------------------")
    print(" 1  | Nasgor        | 10000")
    print(" 2  | Geprek        | 12000")
    print(" 3  | Nasi Padang   | 13000")
    print(" 4  | Es Teh        | 2000")
    print(" 5  | Teh hangat    | 1500")
    print(" 6  | Es Jeruk      | 2000")
    print(" 7  | Jeruk Hangat  | 1500")
    print("-------------------------------" + color.END)
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 10000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 12000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 13000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 2000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 1500 * jumlah5   
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 2000 * jumlah4
        total.append(total6)
        tanya()
    elif kode == 7:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 1500 * jumlah5   
        total.append(total7)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print(color.RED + "SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        totalakhir = a
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------" + color.RED )

daftar_barang()
