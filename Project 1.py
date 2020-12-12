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
print("     Warung Makan Sejahtera      ")
print("           KASIR A               ")
print("      Nama kasir = Mba Ayu       ")
print("-------------------------------")
pelanggan = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")

def daftar_menu():
    print(color.BLUE + " No | Nama Barang | Harga" + color.END)
    print(color.RED + "-------------------------------")
    print(" 1  | Nasi goreng   | 10000")
    print(" 2  | Ayam Geprek   | 12000")
    print(" 3  | Nasi rames    | 13000")
    print(" 4  | Soto Ayam     | 10000")
    print(" 5  | Es Teh        | 2000")
    print(" 6  | Teh hangat    | 1500")
    print(" 7  | Es Jeruk      | 2000")
    print(" 8  | Jeruk Hangat  | 1500")

    print("-------------------------------" + color.END)
    kode = int(input("Angka pesanan : "))
    if kode == 1:
        jumlah1 = int(input("jumlah pesanan : "))
        total1 = 10000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("jumlah pesanan : "))
        total2 = 12000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("jumlah pesanan : "))
        total3 = 13000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("jumlah pesanan : "))
        total4 = 10000 * jumlah4 
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("jumlah pesanan : "))
        total5 = 2000 * jumlah5
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah6 = int(input("jumlah pesanan : "))
        total6 = 1500 * jumlah6   
        total.append(total6)
        tanya()
    elif kode == 7:
        jumlah7 = int(input("jumlah pesanan : "))
        total7 = 2000 * jumlah7
        total.append(total7)
        tanya()
    elif kode == 8:
        jumlah8 = int(input("jumlah pesanan : "))
        total8 = 1500 * jumlah8   
        total.append(total8)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("ingin menambah pesanan? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_menu()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("customer :",pelanggan)
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
        
daftar_menu()
