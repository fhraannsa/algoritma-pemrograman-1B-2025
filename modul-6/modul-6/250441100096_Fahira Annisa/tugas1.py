# Sistem Kunjungan Santri 
def tambah_data(kunjungan, id_antrian):
    print("\n--- Tambah Data Pengunjung ---")
    nama_pengunjung = input("Nama Pengunjung     : ")
    nama_santri = input("Nama Santri Dijenguk: ")


    while True:
        daerah = input("Daerah Asal (sumatra/kalimantan/jawa): ").lower()
        if daerah in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print("Masukkan hanya: sumatra, kalimantan, atau jawa.")

    
    kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID Antrian: {id_antrian}")

    return id_antrian + 1             


def tampilkan_data(kunjungan):
    print("\n=== Daftar Pengunjung Berdasarkan Daerah ===")

    if not kunjungan:
        print("Belum ada data kunjungan.")
        return

    urutan_daerah = ["sumatra", "kalimantan", "jawa"]

    for daerah in urutan_daerah:
        print(f"\n-- Pengunjung dari {daerah} --")
        for data in kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")


def hapus_data(kunjungan):
    print("\n--- Hapus Data Pengunjung ---")
    hapus_id = int(input("Masukkan ID Antrian yang akan dihapus: "))
    for data in kunjungan:
        if data[0] == hapus_id:
            kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")
                                       
def main():
    kunjungan = [] #list utama
    id_antrian = 1

    while True:
        print("\n======= SISTEM KUNJUNGAN SANTRI =======")
        print("1. Tambah Data Pengunjung")
        print("2. Tampilkan Daftar Pengunjung")
        print("3. Hapus Data Pengunjung")
        print("4. Keluar") 

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            id_antrian = tambah_data(kunjungan, id_antrian)
        elif pilihan == "2":
            tampilkan_data(kunjungan)
        elif pilihan == "3":
            hapus_data(kunjungan)
        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


main()
