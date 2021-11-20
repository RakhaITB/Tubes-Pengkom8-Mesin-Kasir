import pandas as pd  # modul untuk analisis data
from datetime import date  # modul untuk mengambil informasi tanggal pada komputer

tanggal_hari_ini = date.today()
dataframe_penghasilan = pd.read_csv('data_penghasilan.csv')
pemasukan_hari_ini = 0
pelanggan_hari_ini = 0


def update_data():
    data_baru = {"tanggal": tanggal_hari_ini, "pelanggan": int(pelanggan_hari_ini), "pemasukan": pemasukan_hari_ini}
    # menambahkan data_baru ke data frame
    updated_dataframe = dataframe_penghasilan.append(data_baru, ignore_index=True)
    updated_dataframe.to_csv('data_penghasilan.csv')  # meng-overwrite data frame

