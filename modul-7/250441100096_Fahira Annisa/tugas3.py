kupon = {
    "KAYU10": 10,
    "LANTAI20": 20,
    "KASUR30": 30
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.")
        return
     
    print("\n=== Daftar Kupon Tersedia ===")
    for kode, diskon in kupon.items():
        print(f"Kode Kupon : {kode} | Diskon : {diskon}%")
    print("-------------------------------")


def proses_transaksi():
    try:
        total_belanja = float(input("Masukkan total belanja: "))
    except ValueError:
        print("Input total belanja tidak valid!")
        return

    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total_belanja * (diskon / 100)
        total_akhir = total_belanja - potongan

        print("\nKupon valid! Diskon berhasil diterapkan.")
        print(f"Total Belanja   : Rp {total_belanja}")
        print(f"Diskon ({diskon}%): Rp {potongan}")
        print(f"Total Akhir     : Rp {total_akhir}")

     
        del kupon[kode]
        print("Kupon telah dihapus dan tidak bisa dipakai lagi.")
    else:
        print("Kupon tidak valid atau sudah digunakan!")


while True:
    print("\n======= MENU KUPON DISKON =======")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi Menggunakan Kupon")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")



