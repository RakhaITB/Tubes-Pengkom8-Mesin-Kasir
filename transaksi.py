
daftar_jenis_transaksi = [
    {
        "nama": "Belanja",
        "nomor": 1
    },
    {
        "nama": "Isi Pulsa",
        "nomor": 2
    },
    {
        "nama": "Top-up",
        "nomor": 3
    },
    {
        "nama": "Checkout",
        "nomor": 4
    }
]


def tunjukkan_daftar_menu():
    print("""============================================
Daftar Transaksi
--------------------------------------------""")
    for transaksi in daftar_jenis_transaksi:
        print(str(transaksi["nomor"]) + ": " + transaksi["nama"])