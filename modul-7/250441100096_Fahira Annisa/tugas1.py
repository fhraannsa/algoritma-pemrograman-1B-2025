kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nTidak ada kontak yang tersimpan.")
        return
    print("\n=== Daftar Kontak ===")
    for nama in kontak:
        print(f"Nama   : {nama}")
        print(f"Telepon: {kontak[nama][0]}")
        print(f"Email  : {kontak[nama][1]}")
        print("-------------------------")


def cari_kontak():
    nama = input("Masukkan nama yang dicari: ") 
    if nama in kontak:
        print("\nKontak ditemukan!")
        print(f"Nama   : {nama}")
        print(f"Telepon: {kontak[nama][0]}")
        print(f"Email  : {kontak[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")


def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ")
    if nama in kontak:
        print("Kontak sudah ada!")
        return
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    kontak[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!")


def update_email():
    nama = input("Masukkan nama kontak yang ingin diupdate emailnya: ")
    if nama in kontak:
        email_baru = input("Masukkan email baru: ")
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui!")
    else:
        print("Kontak tidak ditemukan.")



def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")



while True:
    print("\n========= MENU =========")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
