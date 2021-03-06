
from identitas_kasir import *  # file untuk kegunaan mencatat identitas kasir yang bekerja
from transaksi import *  # file untuk menunjukkan menu transaksi yang tersedia
from transaksi_belanja import ProdukBelanja  # file yang menyimpan data produk
from transaksi_isi_pulsa import *  # file untuk kegunaan transaksi isi pulsa
from transaksi_topup import *  # file untuk kegunaan transaksi top-up
from Checkout import Checkout  # file untuk kegunaan interface checkout
import analisis_data  # file untuk mendefinisikan metode untuk mengolah data pemasukan

from os import system, name  # modul untuk memakai perintah system('cls')

wishlist = []  # wishlist yang menyimpan daftar barang


def clear_screen():  # fungsi untuk membersihkan terminal
    if name == 'nt':  # jika pengguna memakai OS Windows
        system('cls')
    else:  # jika bukan OS Windows (Mac, Linux)
        system('clear')


def ambil_identitas_kasir():  # subprogram pengambilan identitas kasir
    kasir_pilihan = menu_kasir()  # menunjukkan menu kasir
    input("Tekan ENTER untuk melanjutkan")
    return kasir_pilihan


def scan_barang():  # interface scan barang
    # subprogram untuk mengecek apakah barang yang di-scan ada di wishlist
    def barang_ada_di_wishlist(barang):
        ditemukan = False
        for benda in wishlist:
            if benda["nama"] == barang["nama"]:
                ditemukan = True
                break
        return ditemukan

    # subprogram untuk mencari indeks barang apabila sudah ada di wishlist
    def cari_indeks_barang_di_wishlist(properti, nilai):
        for indeks, barang in wishlist:
            if barang[properti] == nilai:
                return indeks
        return None

    barcode = int(input("Masukkan barcode barang: "))
    p = ProdukBelanja("", "", barcode)
    produk_ditemukan = p.cari_produk()  # mencari barcode produk di katalog

    if not produk_ditemukan:  # apabila barcode tidak ditemukan di katalog
        print("Barcode ini tidak ditemukan di katalog.")
        scan_lagi()  # menawarkan untuk scan lagi
    else:  # jika barcode barang ditemukan di katalog
        jumlah_barang_dibeli = int(input("Berapa barang yang ingin dibeli?: "))
        produk_ditemukan["jumlah"] = jumlah_barang_dibeli

        if barang_ada_di_wishlist(produk_ditemukan):  # jika barang sudah ada di wishlist
            # mencari indeks barang di wishlist
            indeks_barang = cari_indeks_barang_di_wishlist("nama", produk_ditemukan["nama"])
            wishlist[indeks_barang]["jumlah"] += jumlah_barang_dibeli  # menambahkan jumlah barang yang dibeli
        else:  # jika barang belum ada di wishlist
            wishlist.append(produk_ditemukan)

        scan_lagi()


def scan_lagi():  # penawaran untuk scan lagi
    konfirmasi = input("Apakah Anda ingin menge-scan barang lagi? (Y/N): ")
    if konfirmasi.upper() == "Y":
        scan_barang()


def main():  # interface utama
    # menambahkan wishlist, tanggal, dan kasir ke class Checkout
    c1 = Checkout(wishlist, analisis_data.tanggal_hari_ini, kasir_on_duty)
    analisis_data.pelanggan_hari_ini += 1

    transaksi_selesai = False
    while not transaksi_selesai:  # looping selama user belum meminta checkout
        clear_screen()
        c1.tunjukkan_keranjang()  # menunjukkan keranjang
        tunjukkan_daftar_menu()  # menunjukkan daftar menu transaksi
        jenis_menu = int(input("Masukkan transaksi yang diinginkan: "))
        while not ((1 <= jenis_menu <= 5) or None):  # jika pilihan menu tidak valid
            jenis_menu = int(input("Kode transaksi tidak valid. Coba lagi: "))

        if jenis_menu == 1:  # pilihan belanja
            scan_barang()
        elif jenis_menu == 2:  # pilihan isi pulsa
            wishlist.append(menu_isi_pulsa())
        elif jenis_menu == 3:  # pilihan topupfj
            wishlist.append(menu_topup())
        else:  # pilihan checkout
            transaksi_selesai = True

    # user memilih checkout
    clear_screen()
    c1.tunjukkan_keranjang()
    bayaran = c1.hitung_bayaran()  # menghitung total bayaran
    c1.terima_pembayaran(bayaran)  # meminta bayaran pelanggan

    clear_screen()
    c1.cetak_struk()  # mencetak struk

    analisis_data.pemasukan_hari_ini += c1.pemasukan_sesi_ini()  # memperbarui pemasukan ke file analisis_data

    selanjutnya = input("(P)elanggan selanjutnya atau (S)elesai?: ")   # konfirmasi transaksi selanjutnya
    if selanjutnya.upper() == "P":
        wishlist[:] = []  # mengosongkan wishlist
        main()  # mengulang proses transaksi
    else:
        analisis_data.update_data()  # memperbarui file data_penghasilan.csv
        exit()  # menghentikan program


def lihat_statistik():
    print("Statistik mana yang ingin Anda lihat?\n"
          "[1] Statistik pemasukan\n"
          "[2] Statistik jumlah pelanggan\n"
          "[3] Kembali ke menu sebelumnya")
    pilihan_stat = int(input("Silahkan pilih menu: "))

    if pilihan_stat == 1:
        analisis_data.tunjukkan_plot_penghasilan()  # menunjukkan plot pemasukan
    elif pilihan_stat == 2:
        analisis_data.tunjukkan_plot_pelanggan()  # menunjukkan plot jumlah pelanggan
    else:
        return False


# OUTPUT
while True:  # mengulang program sampai user memilih transaksi atau sudah memilih statistik yang dilihat
    clear_screen()
    print("Selamat datang! Apa yang ingin Anda lakukan?\n"
          "[1] Transaksi\n"
          "[2] Lihat statistik")
    pilihan = int(input("Silahkan pilih menu: "))
    while not (pilihan == 1 or pilihan == 2):
        pilihan = int(input("Pilihan tidak valid, coba lagi: "))

    if pilihan == 1:
        clear_screen()
        kasir_on_duty = ambil_identitas_kasir()  # mengambil identitas kasir yang bekerja
        main()  # menunjukkan interface utama
    else:
        clear_screen()
        output = lihat_statistik()  # menunjukkan menu statistik
        if output is False:
            continue  # kembali ke daftar menu sebelumnya
        else:
            exit()  # program selesai
