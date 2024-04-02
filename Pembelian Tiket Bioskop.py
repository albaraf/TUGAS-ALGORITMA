# Program Pembelian Tiket Bioskop
daftar_film = {"Agak Laen": 35000, "Ronggeng Kematian": 40000, "Pemandi Jenazah": 30000, "Mangkujiwo": 45000, "Siksa Neraka": 30000}
print("Selamat datang di Layanan Pembelian Tiket Bioskop!")
print("Daftar Film:") ; [print(film, "- Harga Tiket: Rp", harga) for film, harga in daftar_film.items()] ; film_pilihan = input("Pilih film yang ingin ditonton: ")
if film_pilihan in daftar_film:
    jumlah_tiket = int(input("Berapa jumlah tiket yang ingin dibeli: "));total_harga = daftar_film[film_pilihan] * jumlah_tiket
    print("\nRingkasan Pembelian:")
    print("Film:", film_pilihan)
    print("Jumlah Tiket:", jumlah_tiket)
    print("Total Harga: Rp", total_harga);konfirmasi = input("\nApakah Anda yakin ingin melanjutkan pembelian? (ya/tidak): ")
    if konfirmasi.lower() == "ya": print("Pembelian berhasil! Nikmati film", film_pilihan)
    else:
        print("Pembelian dibatalkan.")
else:
    print("Maaf, film yang Anda pilih tidak tersedia.")