import pandas as pd  # modul untuk analisis data
from datetime import date  # modul untuk mengambil informasi tanggal pada komputer
from matplotlib import pyplot as plt  # modul untuk menge-plot data

tanggal_hari_ini = date.today()
dataframe = pd.read_csv('database/data_penghasilan.csv')
pemasukan_hari_ini = 0
pelanggan_hari_ini = 0


def update_data():
    data_baru = {"tanggal": tanggal_hari_ini, "jumlah pelanggan": int(pelanggan_hari_ini),
                 "pemasukan": pemasukan_hari_ini}
    # menambahkan data_baru ke data frame
    updated_dataframe = dataframe.append(data_baru, ignore_index=True)
    updated_dataframe.to_csv('database/data_penghasilan.csv', index=False)  # meng-overwrite data frame


def tunjukkan_plot_penghasilan():
    dataframe_penghasilan = dataframe.groupby('tanggal').sum('pemasukan')
    dataframe_penghasilan.to_csv('database/data_penghasilan_per_tanggal.csv')
    dataframe_penghasilan = pd.read_csv('database/data_penghasilan_per_tanggal.csv')
    x, y = dataframe_penghasilan['tanggal'], dataframe_penghasilan['pemasukan']

    plt.bar(x, y)

    plt.xlabel("Tanggal (dd-mm-yyyy)")
    plt.ylabel("Pemasukan (IDR)")
    plt.title("Plot pemasukan setiap tanggal")

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def tunjukkan_plot_pelanggan():
    dataframe_pelanggan = dataframe.groupby('tanggal').sum('pelanggan')
    dataframe_pelanggan.to_csv('database/data_penghasilan_per_tanggal.csv')
    dataframe_pelanggan = pd.read_csv('database/data_penghasilan_per_tanggal.csv')
    x, y = dataframe_pelanggan['tanggal'], dataframe_pelanggan['jumlah pelanggan']

    plt.bar(x, y)

    plt.xlabel("Tanggal (dd-mm-yyyy)")
    plt.ylabel("Jumlah pelanggan")
    plt.title("Plot jumlah pelanggan setiap tanggal")

    plt.grid(True)
    plt.tight_layout()
    plt.show()
