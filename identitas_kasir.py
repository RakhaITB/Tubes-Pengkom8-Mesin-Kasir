
class IdentitasKasir:
    daftar_kasir = [
        {
            "nama": "Sanatha",
            "nomor": 1
        },
        {
            "nama": "Cerry",
            "nomor": 2
        },
        {
            "nama": "Yolanda",
            "nomor": 3
        },
        {
            "nama": "Rakha",
            "nomor": 4
        },
        {
            "nama": "Steven",
            "nomor": 5
        },
        {
            "nama": "Henard",
            "nomor": 6
        }
    ]

    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def tambahkan_kasir_ke_daftar(self):
        self.daftar_kasir.append({"nama": self.nama, "nomor": self.nomor})


def tunjukkan_daftar_kasir():
    print("""============================================
Daftar Karyawan
--------------------------------------------""")
    for kasir in IdentitasKasir.daftar_kasir:
        print(str(kasir["nomor"]) + " : " + kasir["nama"])


def cari_kasir(nomor):
    kasir_ditemukan = False
    kasir_bekerja = ""
    for kasir in IdentitasKasir.daftar_kasir:
        if nomor == kasir["nomor"]:
            kasir_ditemukan = True
            kasir_bekerja = kasir["nama"]
            break

    if kasir_ditemukan:
        nomor_shift = int(input("Masukkan Nomor Shift: "))
        print("Kasir on-duty: " + kasir_bekerja)
        print("Shift: " + str(nomor_shift))
        return kasir_bekerja
    else:
        return False


def menu_kasir():
    tunjukkan_daftar_kasir()
    nomor_karyawan = int(input("Masukkan nomor karyawan: "))
    status = cari_kasir(nomor_karyawan)
    while not status:
        nomor_karyawan = int(input("Nomor Karyawan tidak valid, coba lagi: "))
        cari_kasir(nomor_karyawan)
    return status