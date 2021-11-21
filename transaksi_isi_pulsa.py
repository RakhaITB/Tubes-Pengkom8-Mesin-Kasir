
class IsiPulsa:
    daftar_provider = [
        {
            "nama": "SimPATI",
            "nomor": 1
        },
        {
            "nama": "IM3 Ooredoo",
            "nomor": 2
        }
    ]

    daftar_nominal = [
        {
            "nominal": 5000,
            "nomor": 1
        },
        {
            "nominal": 10000,
            "nomor": 2
        }
    ]

    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def tambahkan_provider_ke_daftar(self):
        self.daftar_provider.append({"nama": self.nama, "nomor": self.nomor})

    def cari_provider(self):
        ditemukan = False
        provider_yang_ditemukan = {}
        for provider in self.daftar_provider:
            if self.nomor == provider["nomor"]:
                provider_yang_ditemukan = {"nama": provider["nama"], "nomor": provider["nomor"]}
                ditemukan = True
                break

        if ditemukan:
            return provider_yang_ditemukan
        else:
            return False

    def cari_nominal(self):
        ditemukan = False
        nominal_yang_ditemukan = {}
        for nominal in self.daftar_nominal:
            if self.nomor == nominal["nomor"]:
                nominal_yang_ditemukan = {"nominal": nominal["nominal"], "nomor": nominal["nomor"]}
                ditemukan = True
                break

        if ditemukan:
            return int(nominal_yang_ditemukan["nominal"] * 1.1)  # keuntungan 10%
        else:
            return False


def tunjukkan_daftar_provider():
    print("""============================================
Daftar Provider
--------------------------------------------""")
    for provider in IsiPulsa.daftar_provider:
        print(str(provider["nomor"]) + ": " + provider["nama"])


def tunjukkan_daftar_nominal():
    print("""============================================
Daftar Produk
--------------------------------------------""")
    for nominal in IsiPulsa.daftar_nominal:
        print(str(nominal["nomor"]) + ": " + str(nominal["nominal"]))


def provider_isi_pulsa():
    item = {}
    tunjukkan_daftar_provider()

    jenis_provider = int(input("Masukkan nomor provider: "))
    prov = IsiPulsa("", jenis_provider)
    status = prov.cari_provider()
    while status is False:
        print("Provider tidak ditemukan.")
        status = isi_pulsa_lagi()

    if status is True:
        return None
    else:  # jika transaksi berhasil, fungsi cari provider menghasilkan item, bukan boolean
        item["nama"] = "Pulsa " + status["nama"]
        item["harga"] = nominal_isi_pulsa()
        return item


def isi_pulsa_lagi():
    konfirmasi = input("Apakah Anda ingin mencoba memilih provider lagi? (Y/N): ")
    if konfirmasi.upper() == "Y":
        return provider_isi_pulsa()
    else:
        return True


def nominal_isi_pulsa():
    tunjukkan_daftar_nominal()

    jenis_nominal = int(input("Masukkan jenis nominal yang ingin diisi: "))
    nom = IsiPulsa("", jenis_nominal)
    status = nom.cari_nominal()
    while status is False:
        print("ID nominal tidak valid.")
        status = nominal_isi_pulsa_lagi()
    return status


def nominal_isi_pulsa_lagi():
    konfirmasi = input("Apakah Anda ingin mencoba memilih jenis nominal lagi? (Y/N): ")
    if konfirmasi.upper() == "Y":
        return nominal_isi_pulsa()
    else:
        return True


def menu_isi_pulsa():
    input("Masukkan nomor tujuan: ")
    pulsa = provider_isi_pulsa()
    return pulsa
