
from identitas_kasir import *
from transaksi import *
from transaksi_belanja import ProdukBelanja
from transaksi_isi_pulsa import *
from Checkout import Checkout
from transaksi_topup import *

import pandas as pd
import time
import os

wishlist = []


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
    def ambil_identitas_kasir():  # subprogram pengambilan identitas kasir
        check = Checkout(wishlist)  # menambahkan wishlist ke class Checkout
        kasir = menu_kasir()  # menunjukkan menu kasir
        check.kasir_di_struk(kasir)  # menambahkan nama kasir di struk
        return check
    c1 = ambil_identitas_kasir()

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
