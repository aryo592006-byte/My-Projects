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


print("=== Asisten Keuangan dan Investasi Pribadi Sederhana ===")


nama = input("Masukan nama: ").strip()

print(f"\nHalo: {nama}!")
print("Selamat datang di Asisten Keuangan dan Investasi Pribadi Sederhana :).")
print("Asisten ini hanya akan membantu simulasi keuangan dan investasi secara super sederhana untuk per bulannya.")
print("Tolong masukkan angkanya tanpa koma, misal saya ingin menulis lima ribu, maka tuliskanlah 5000 bukan 5,000 atau 5.000\n\n")

#State Variables
menu_digunakan = 0
simulasi_digunakan = 0
tips_dibaca = 0

while True:
    print("\n===")
    print(f"Halo {nama}")
    print(f"Menu yang digunakan: {menu_digunakan}")
    print(f"Jumlah simulasi digunakan: {simulasi_digunakan}")
    print("===")

    print("Pilih Menu")
    print("1. Simulasi Investasi")
    print("2. Hitung Target Tabungan")
    print("3. Cek Pebgeluaran Bulanan")
    print("4. Tips Investasi")
    print("5. Status Saya")
    print("6. Keluar")


    pilihan = input("\nMasukan pilihan:").strip().lower()

    if pilihan == "1":

        modal = float(input("Masukan modal investasi (Rp): "))
        return_investasi = float(input("Masukan estimasi return (%): "))

        keuntungan = modal * (return_investasi/100)
        total = modal + keuntungan


        print("\n=== HASIL SIMULASI ===")
        print(f"modal investasi : Rp {modal:,.0f}")
        print(f"Estimasi Return : {return_investasi:,.2f}%")
        print(f"Keuntungan atau Laba : {keuntungan:,.0f}")
        print(f"Total Dana : Rp {total:,.0f}")

        konfirmasi_1 = input("\nketik 'ya' jika anda sudah melihat hasilnya: ").strip().lower()

        if konfirmasi_1 == "ya":
            simulasi_digunakan += 1
            menu_digunakan += 1

        else:
            print("\n hayo harusnya sudah dong...\n kuanggap anda sudah mengetik 'ya'")



    elif pilihan =="2":

        target = float(input("Masukan target tabungan (Rp): "))
        tabungan = float(input("Masukan tabungan setiap bulan (Rp): "))
        suku_bunga = float(input("Masukan tingkat suku bunga dan jangan ketik '%' hanya angkanya saja (kita asumsikan suku bunga konstan): "))

        tabungan_dengan_bunga = tabungan + (tabungan * (suku_bunga/100))
        bulan = target/tabungan_dengan_bunga


        print("\n=== TARGET TABUNGAN ===")
        print(f"Target Tabungan : Rp {target:,.0f}")
        print(f"Tabungan per bulan: Rp {tabungan:,.0f}")
        print(f"Estimasi Waktu dalam Bulanan: {bulan:.1f}")

        konfirmasi_2 = input("\nKetik 'ya' jika anda sudah melihat hasilnya: ").strip().lower()

        if konfirmasi_2 == "ya":
            menu_digunakan += 1

        else:
            print("\n hayo harusnya sudah dong...\n kuanggap anda sudah mengetik 'ya'")



    elif pilihan =="3":

        pendapatan = float(input("Masukan pendapatan bulanan (Rp) :"))
        pengeluaran = float(input("Masukan pengeluaran bulanan (Rp) :"))

        sisa = pendapatan - pengeluaran


        print("\n=== SISA pendapatan bulanan ===")
        print(f"Pendapatan bulanan: {pendapatan:,.0f}")
        print(f"Pengeluaran bulanan: {pengeluaran:,.0f}")
        print(f"Sisa pendapatan bulanan : {sisa:,.0f}")

        konfrimasi_3 = input("\nKetik 'ya' jika anda sudah melihat hasilnya: ").strip().lower()

        if konfrimasi_3 == "ya":
            menu_digunakan += 1

        else:
            print("\n hayo harusnya sudah dong...\n kuanggap anda sudah mengetik 'ya'")


    elif pilihan =="4":

        print("\n===== TIPS INVESTASI =====")
        print("1. Investasikan dana secara rutin.")
        print("2. Jangan menaruh seluruh dana pada satu aset.")
        print("3. Siapkan dana darurat sebelum berinvestasi.")
        print("4. Pahami risiko sebelum membeli instrumen investasi.")

        konfirmasi_4 = input("\nKetik 'ya' jika anda sudah melihat hasilnya: ").strip().lower()

        if konfirmasi_4 == "ya":
            tips_dibaca += 1
            menu_digunakan += 1

        else:
            print("\n hayo harusnya sudah dong...\n kuanggap anda sudah mengetik 'ya'")


    elif pilihan =="5":

        print("\n===STATUS PENGGUNA===")
        print(f"Nama : {nama}")
        print(f"Menu digunakan : {menu_digunakan}")
        print(f"Simulasi digunakan : {simulasi_digunakan}")
        print(f"Tips telah di baca : {tips_dibaca}")

        konfirmasi_5 = input("\nKetik 'ya' jika anda sudah melihat hasilnya:  ").strip().lower()

        if konfirmasi_5 == "ya":
            menu_digunakan += 1

        else:
            print("\nhayo harusnya sudah dong...\n kuanggap anda sudah mengetik 'ya' ")

    elif pilihan =="6" or pilihan == "exit" or pilihan == "quit" or pilihan == "keluar" or pilihan == "metu":

        print("\n===Terima kasih telah mencoba menggunakan=== \n===Asisten Keuangan dan Invetasi Pribadi Sederhana===")
        print("\n===RINGKASAN PERILAKU PENGGUNA===")
        print(f"Nama : {nama}")
        print(f"Menu digunakan : {menu_digunakan}")
        print(f"Simulasi digunakan : {simulasi_digunakan}")
        print(f"Tips telah di baca : {tips_dibaca}")

        print("\n\n Sampai jumpa lagi, kalau anda butuh asistensi keuangan pribadi datanglah kemari lagi!!!")
        break

    else:

        print("\n Maaf mas/mbak, mbok ya dibaca pilihan hanya tersedia diantara menu 1 sampai 6 saja...")