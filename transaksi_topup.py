
class TopUp:
    daftar_topup = [
        {
            "nama": "GO-PAY",
            "nomor": 1
        },
        {
            "nama": "OVO",
            "nomor": 2
        }
    ]

    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def tambahkan_topup_ke_daftar(self):
        self.daftar_topup.append({"nama": self.nama, "nomor": self.nomor})

    def cari_topup(self):
        ditemukan = False
        topup_yang_ditemukan = {}
        for topup in self.daftar_topup:
            if self.nomor == topup["nomor"]:
                topup_yang_ditemukan = {"nama": topup["nama"], "nomor": topup["nomor"]}
                ditemukan = True
                break

        if ditemukan:
            return topup_yang_ditemukan
        else:
            return False


def tunjukkan_daftar_topup():
    print("""============================================
Daftar Provider
--------------------------------------------""")
    for topup in TopUp.daftar_topup:
        print(str(topup["nomor"]) + ": " + topup["nama"])


def pencari_topup():
    item = {}
    tunjukkan_daftar_topup()

    jenis_topup = int(input("Masukkan kode top-up: "))
    top = TopUp("", jenis_topup)
    status = top.cari_topup()
    while not status:  # jika cari_topup() gagal, maka status = False
        print("Top-up tidak ditemukan.")
        status = topup_lagi()
    if status is not True:  # jika transaksi berhasil, fungsi cari_topup() menghasilkan dict, bukan bool
        item["nama"] = "Top-up " + status["nama"]
        item["harga"] = nominal_topup()
        return item
    else:
        return None


def topup_lagi():
    konfirmasi = input("Apakah Anda ingin mencoba top-up lagi? (Y/N) ")
    if konfirmasi.upper() == "Y":
        pencari_topup()
    else:
        return True


def nominal_topup():
    nominal_isian = int(input("Masukkan jumlah yang ingin di-top-up: "))
    return int(nominal_isian * 1.1)  # keuntungan 10%


def menu_topup():
    topup = pencari_topup()
    return topup
