
class Checkout:
    def __init__(self, keranjang, sisa_bayaran=0):
        self.keranjang = keranjang
        self.sisa_bayaran = sisa_bayaran

    def tambahkan_barang_ke_keranjang(self, barang):
        self.keranjang.append(barang)

    def hitung_bayaran(self):
        bayaran_total = 0
        for produk in self.keranjang:
            try:  # jika barang memiliki kunci "jumlah", yakni benda dari kelas ProdukBelanja
                bayaran_total += produk["harga"] * produk["jumlah"]
            except KeyError:  # jika barang dari kelas IsiPulsa atau TopUp, maka tidak ada kunci "jumlah"
                bayaran_total += produk["harga"]
        self.sisa_bayaran += bayaran_total
        return self.sisa_bayaran

    def pembayaran(self, bayaran):
        jumlah_yang_harus_dibayar = bayaran
        print("\nJumlah yang harus dibayarkan: Rp" + str(jumlah_yang_harus_dibayar))
        kembalian = self.terima_pembayaran(jumlah_yang_harus_dibayar)
        return kembalian

    def terima_pembayaran(self, jumlah_yang_harus_dibayar):
        bayaran_pelanggan = 0.0
        sisa_yang_harus_dibayar = True
        total_yang_harus_dibayar = jumlah_yang_harus_dibayar

        print("Total: Rp" + str(total_yang_harus_dibayar))
        while sisa_yang_harus_dibayar:
            try:
                terbayar = float(input("\nMasukkan jumlah yang akan dibayar: "))
                if terbayar < 0:
                    print("Maaf, kami tidak menerima hutang")
                    continue
                else:
                    bayaran_pelanggan += terbayar
                    self.bayaran_pelanggan = bayaran_pelanggan
                    if terbayar < total_yang_harus_dibayar:
                        sisa_yang_harus_dibayar = total_yang_harus_dibayar - terbayar
                        total_yang_harus_dibayar = sisa_yang_harus_dibayar
                        print("Sisa yang harus dibayar: Rp" + str(sisa_yang_harus_dibayar))
                        sisa_yang_harus_dibayar = True
                        continue
                    else:
                        kembalian = terbayar - total_yang_harus_dibayar
                        self.kembalian = kembalian
                        return kembalian
            except ValueError:
                print("Masukkan angka yang valid!")

    def kasir_di_struk(self, kasir):
        self.kasir = kasir

    def tunjukkan_keranjang(self):
        print("===== KERANJANG =====")
        for benda in self.keranjang:
            try:
                print(benda["nama"] + " (jumlah: " + str(benda["jumlah"]) + ")" +
                      " Rp" + str(benda["harga"] * benda["jumlah"]))
            except KeyError:
                print(benda["nama"] + " Rp" + str(benda["harga"]))

    def cetak_struk(self):
        print("\n====== STRUK ======")
        print("Kasir: " + self.kasir)
        print("===================")

        for benda in self.keranjang:
            try:
                print(benda["nama"] + " (jumlah: " + str(benda["jumlah"]) + ")" +
                      " Rp" + str(benda["harga"] * benda["jumlah"]))
            except KeyError:
                print(benda["nama"] + " Rp" + str(benda["harga"]))

        print("\n")
        print("TOTAL:", "          Rp" + str(self.sisa_bayaran))
        print("DITERIMA:", "       Rp" + str(self.bayaran_pelanggan))
        print("KEMBALIAN:", "      Rp" + str(self.kembalian))

    def pemasukan_sesi_ini(self):
        return self.sisa_bayaran
