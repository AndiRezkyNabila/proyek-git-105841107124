# kalkulator.py - Kalkulator interaktif


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return a / b


OPERASI = {
    "1": ("Tambah", "+", tambah),
    "2": ("Kurang", "-", kurang),
    "3": ("Kali", "x", kali),
    "4": ("Bagi", ":", bagi),
}


def tampilkan_riwayat(riwayat):
    if not riwayat:
        print("Riwayat masih kosong.")
    for baris in riwayat:
        print(baris)


def tampilkan_menu():
    print("\n=== KALKULATOR ===")
    for nomor, (nama, _, _) in OPERASI.items():
        print(f"{nomor}. {nama}")
    print("5. Riwayat")
    print("0. Keluar")


def main():
    riwayat = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Sampai jumpa!")
            break
        if pilihan == "5":
            tampilkan_riwayat(riwayat)
            continue
        if pilihan not in OPERASI:
            print("Pilihan tidak tersedia, pilih sesuai menu.")
            continue
        _, simbol, fungsi = OPERASI[pilihan]
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        baris = f"{a} {simbol} {b} = {fungsi(a, b)}"
        riwayat.append(baris)
        print(baris)


if __name__ == "__main__":
    main()
