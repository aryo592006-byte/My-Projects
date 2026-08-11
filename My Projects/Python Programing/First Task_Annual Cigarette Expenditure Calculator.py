# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm shelp at https://www.jetbrains.com/help/pycharm/

print("== PERBANDINGAN PENGELUARAN UNTUK ROKOK TAHUN LALU DAN TAHUN INI ==")
print("Mengasumsikan anda membeli produk rokok yang identik dan frekuensi pembelian yang sama selama dua tahun penuh")

#Input Data
nama = input("Masukan nama: ")
harga_rokok_tahun_lalu = float(input("Masukan harga rokok tahun lalu (tanpe menulis Rp.):"))
harga_rokok_tahun_ini = float(input("Masukan harga rokok tahun ini (tanpa menulis Rp.):"))
frekuensi_beli_rokok = int(input("Masukan berapa kali anda membeli rokok dalam satu tahun? "))

#Perhitungan Perubahan Harga Rokok
perubahan_harga_rokok = ((harga_rokok_tahun_ini-harga_rokok_tahun_lalu)/harga_rokok_tahun_lalu)*100

#Total Pengeluaran
total_pengeluaran_rokok_tahun_lalu = harga_rokok_tahun_lalu * frekuensi_beli_rokok
total_pengeluaran_rokok_tahun_ini = harga_rokok_tahun_ini * frekuensi_beli_rokok
total_pertambahan_uang_yang_harus_dikeluarkan = total_pengeluaran_rokok_tahun_ini - total_pengeluaran_rokok_tahun_lalu


#Output
print("\n== HASIL PERHITUNGAN ==")
print(f"nama: {nama}")
print(f"Harga rokok tahun lalu (tanpe menulis Rp.): {harga_rokok_tahun_lalu:,.0f}")
print(f"Harga rokok tahun ini (tanpa menulis Rp.): {harga_rokok_tahun_ini:,.0f}")
print(f"Persentase perubahan harga rokok: {perubahan_harga_rokok:,.2f}%")
print(f"Total pengeluaran tahun lalu: {total_pengeluaran_rokok_tahun_lalu:,.0f}")
print(f"Total pengeluaran tahun ini: {total_pengeluaran_rokok_tahun_ini:,.0f}")
print(f"Total pertambahan uang yang harus dikeluarkan: {total_pertambahan_uang_yang_harus_dikeluarkan:,.0f}")

#Type test
print("\n== Type Test ==")
print("Tipe harga rokok tahun lalu: ", type(harga_rokok_tahun_lalu))
print("Tipe harga rokok tahun ini:", type(harga_rokok_tahun_ini))
print("Tipe frekuensi beli rokok:", type(frekuensi_beli_rokok))