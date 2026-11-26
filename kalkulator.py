# kalkulator.py - Kalkulator interaktif


def tampilkan_menu():
    print("\n=== KALKULATOR ===")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Sampai jumpa!")
            break
        print("Pilihan tidak tersedia, pilih sesuai menu.")


if __name__ == "__main__":
    main()
