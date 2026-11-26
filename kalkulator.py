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


def baca_angka(teks):
    while True:
        try:
            return float(input(teks))
        except ValueError:
            print("Input harus berupa angka.")


def tampilkan_menu():
    print("\n=== KALKULATOR ===")
    for nomor, (nama, _, _) in OPERASI.items():
        print(f"{nomor}. {nama}")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Sampai jumpa!")
            break
        if pilihan not in OPERASI:
            print("Pilihan tidak tersedia, pilih sesuai menu.")
            continue
        _, simbol, fungsi = OPERASI[pilihan]
        a = baca_angka("Angka pertama: ")
        b = baca_angka("Angka kedua: ")
        print(f"{a} {simbol} {b} = {fungsi(a, b)}")


if __name__ == "__main__":
    main()
