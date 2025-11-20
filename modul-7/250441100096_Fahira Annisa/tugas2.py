inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("\nTidak ada data barang.")
        return

    print("\n=== Daftar Barang di Gudang ===")
    for id_barang in inventaris:
        print(f"ID     : {id_barang}")
        print(f"Nama   : {inventaris[id_barang][0]}")
        print(f"Harga  : {inventaris[id_barang][1]}")
        print(f"Stok   : {inventaris[id_barang][2]}")
        print("-----------------------------")


def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ")
    if id_barang in inventaris:
        print("\nBarang ditemukan:")
        print(f"Nama  : {inventaris[id_barang][0]}")
        print(f"Harga : {inventaris[id_barang][1]}")
        print(f"Stok  : {inventaris[id_barang][2]}")
    else:
        print("Barang tidak ditemukan.")


def tambah_barang():
    id_barang = input("Masukkan ID barang baru: ")
    if id_barang in inventaris:
        print("ID barang sudah ada!")
        return
    
    nama = input("Masukkan nama barang: ")
    
    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
    except ValueError:
        print("Harga atau stok tidak valid!")
        return
    
    if stok < 0:
        print("Stok tidak boleh negatif!")
        return
    
    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diupdate stoknya: ")
    
    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
        return
    
    try:
        perubahan = int(input("Masukkan perubahan stok (misal +5 atau -3): "))
    except ValueError:
        print("Input stok tidak valid!")
        return
    
    stok_baru = inventaris[id_barang][2] + perubahan
    
    if stok_baru < 0:
        print("Gagal! Stok tidak boleh menjadi negatif.")
        return
    
    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui!")


def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")


while True:
    print("\n========= MENU INVENTARIS =========")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang() 
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
