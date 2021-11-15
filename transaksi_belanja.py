
class ProdukBelanja:
    daftar_produk = [
        {
            "nama": "KitKat",
            "harga": 8000,
            "barcode": 1234
        },
        {
            "nama": "Ultra Milk 210 ml",
            "harga": 6000,
            "barcode": 5678
        }
    ]

    def __init__(self, nama, harga, barcode):
        self.nama = nama
        self.harga = harga
        self.barcode = barcode

    def tambahkan_produk_ke_daftar(self):
        self.daftar_produk.append({"nama": self.nama, "harga": self.harga, "barcode": self.barcode})

    def cari_produk(self):
        ditemukan = False
        produk_yang_ditemukan = {}
        for produk in self.daftar_produk:
            if self.barcode == produk["barcode"]:
                produk_yang_ditemukan = {"nama": produk["nama"], "barcode": produk["barcode"], "harga": produk["harga"]}
                ditemukan = True
                print(produk["nama"] + ": Rp" + str(produk["harga"]))
                break

        if ditemukan:
            return produk_yang_ditemukan
        else:
            return False


def tunjukkan_daftar_produk():
    print("""============================================
Daftar Produk
--------------------------------------------""")
    for produk in ProdukBelanja.daftar_produk:
        print(produk["nama"] + ": Rp" + str(produk["harga"]))
