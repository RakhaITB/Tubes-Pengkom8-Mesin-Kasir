
from identitas_kasir import *
from transaksi import *
from transaksi_belanja import ProdukBelanja
from transaksi_isi_pulsa import *
from Checkout import Checkout
from transaksi_topup import *

wishlist = []


def scan_barang():  # pendefinisian interface scan barang
    barcode = int(input("Masukkan barcode barang: "))
    p = ProdukBelanja("", "", barcode)
    produk_ditemukan = p.cari_produk()
    if not produk_ditemukan:
        print("Barcode ini tidak ditemukan di katalog.")
        scan_lagi()
    else:
        wishlist.append(produk_ditemukan)
        scan_lagi()


def scan_lagi():  # penawaran untuk scan lagi
    konfirmasi = input("Apakah Anda ingin menge-scan barang lagi? (Y/N): ")
    if konfirmasi.upper() == "Y":
        scan_barang()


def main():  # interface utama
    c1 = Checkout(wishlist)
    kasir = menu_kasir()  # menunjukkan menu kasir
    c1.kasir_di_struk(kasir)  # menambahkan nama kasir di struk

    transaksi_selesai = False
    while not transaksi_selesai:  # looping selama user belum meminta checkout
        tunjukkan_daftar_menu()  # menunjukkan daftar menu transaksi
        jenis_menu = int(input("Masukkan transaksi yang diinginkan: "))
        while jenis_menu not in [i for i in range(1, 5)]:  # meminta ulang input jika tidak valid
            jenis_menu = int(input("Kode transaksi tidak valid. Coba lagi: "))

        if jenis_menu == 1:  # pilihan belanja
            scan_barang()
        elif jenis_menu == 2:  # pilihan isi pulsa
            wishlist.append(menu_isi_pulsa())
        elif jenis_menu == 3:  # pilihan topup
            wishlist.append(menu_topup())
        elif jenis_menu == 4:  # pilihan checkout
            transaksi_selesai = True

    bayaran = c1.hitung_bayaran()  # menghitung total bayaran
    c1.terima_pembayaran(bayaran)  # meminta bayaran pelanggan
    c1.cetak_struk()  # mencetak struk
    selanjutnya = input("(P)elanggan selanjutnya atau (S)elesai?: ")   # konfirmasi transaksi selanjutnya
    if selanjutnya.upper() == "P":
        wishlist[:] = []
        main()  # mengulang proses transaksi
    else:
        exit()  # menghentikan program


main()
