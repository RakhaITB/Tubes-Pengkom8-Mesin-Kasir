
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

    def __init__(self, nama, nomor):  # inisiasi kelas kasir dimulai dengan properti nama dan nomor kasir
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


def cari_kasir(nomor):  # mencari apakah kasir ada di produk
    kasir_ditemukan = False
    kasir_bekerja = None
    for kasir in IdentitasKasir.daftar_kasir:
        if nomor == kasir["nomor"]:  # apabila nomor kasir ada di daftar
            kasir_ditemukan = True
            kasir_bekerja = kasir["nama"]
            break

    if kasir_ditemukan:  # apabila kasir ditemukan
        nomor_shift = int(input("Masukkan momor shift: "))
        print("\nKasir on-duty: " + kasir_bekerja)
        print("Shift: " + str(nomor_shift))
        return kasir_bekerja
    else:
        return False


def menu_kasir():  # subprogram interface kasir
    tunjukkan_daftar_kasir()
    nomor_karyawan = int(input("Masukkan nomor karyawan: "))
    status = cari_kasir(nomor_karyawan)
    while status is False:  # jika kasir tidak ditemukan, status akan bernilai False
        nomor_karyawan = int(input("Nomor Karyawan tidak valid, coba lagi: "))
        status = cari_kasir(nomor_karyawan)
    return status
