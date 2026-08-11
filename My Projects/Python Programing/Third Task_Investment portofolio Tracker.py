print("==============================================")
print("      INVESTMENT PORTFOLIO TRACKER")
print("==============================================")

nama_user = input("Masukkan nama Anda: ").strip().title()

portfolio = []


# =========================
# FUNCTION TAMBAH DATA
# =========================
def add_investment(collection):

    print("\n=== TAMBAH INVESTASI ===")

    nama = input("Nama investasi : ").strip().title()
    kategori = input("Kategori (Saham/Reksadana/Obligasi/Emas): ").strip().title()
    modal = float(input("Modal investasi (Rp): "))
    estimasi_return = float(input("Estimasi return (%): "))
    risiko = input("Risiko (Rendah/Sedang/Tinggi): ").strip().title()

    investasi = {
        "nama": nama,
        "kategori": kategori,
        "modal": modal,
        "return": estimasi_return,
        "risiko": risiko
    }

    collection.append(investasi)

    print("\nInvestasi berhasil ditambahkan.")


# =========================
# FUNCTION TAMPILKAN DATA
# =========================
def show_investments(collection):

    print("\n========== DAFTAR INVESTASI ==========")

    if len(collection) == 0:
        print("Portfolio masih kosong.")
        return

    for i, item in enumerate(collection, start=1):

        print(f"\nInvestasi ke-{i}")
        print(f"Nama            : {item['nama']}")
        print(f"Kategori        : {item['kategori']}")
        print(f"Modal           : Rp {item['modal']:,.0f}")
        print(f"Return          : {item['return']:.2f}%")
        print(f"Risiko          : {item['risiko']}")


# =========================
# FUNCTION CARI DATA
# =========================
def search_investment(collection):

    if len(collection) == 0:
        print("\nPortfolio masih kosong.")
        return

    keyword = input("\nMasukkan nama investasi: ").strip().lower()

    ditemukan = False

    for item in collection:

        if item["nama"].lower() == keyword:

            print("\n=== DATA DITEMUKAN ===")
            print(f"Nama      : {item['nama']}")
            print(f"Kategori  : {item['kategori']}")
            print(f"Modal     : Rp {item['modal']:,.0f}")
            print(f"Return    : {item['return']:.2f}%")
            print(f"Risiko    : {item['risiko']}")

            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")


# =========================
# FUNCTION SUMMARY
# =========================
def portfolio_summary(collection):

    if len(collection) == 0:
        return 0, 0, 0

    total_modal = 0
    total_return = 0

    for item in collection:
        total_modal += item["modal"]
        total_return += item["return"]

    rata_return = total_return / len(collection)

    return len(collection), total_modal, rata_return


# =========================
# FUNCTION UPDATE RETURN
# =========================
def update_return(collection):

    if len(collection) == 0:
        print("\nPortfolio masih kosong.")
        return

    nama = input("Nama investasi yang ingin diubah: ").strip().lower()

    ditemukan = False

    for item in collection:

        if item["nama"].lower() == nama:

            print(f"Return lama : {item['return']} %")

            item["return"] = float(input("Return baru (%): "))

            print("Return berhasil diperbarui.")

            ditemukan = True

    if not ditemukan:
        print("Investasi tidak ditemukan.")


# =========================
# MENU
# =========================
while True:

    print("\n================================")
    print(f"Halo, {nama_user}")
    print("================================")
    print("1. Tambah Investasi")
    print("2. Lihat Portfolio")
    print("3. Cari Investasi")
    print("4. Statistik Portfolio")
    print("5. Update Return Investasi")
    print("6. Keluar")

    pilihan = input("\nMasukkan pilihan: ").strip()

    if pilihan == "1":

        add_investment(portfolio)

    elif pilihan == "2":

        show_investments(portfolio)

    elif pilihan == "3":

        search_investment(portfolio)

    elif pilihan == "4":

        jumlah, modal, rata = portfolio_summary(portfolio)

        print("\n======= STATISTIK =======")
        print(f"Jumlah investasi     : {jumlah}")
        print(f"Total modal          : Rp {modal:,.0f}")
        print(f"Rata-rata return     : {rata:.2f}%")

    elif pilihan == "5":

        update_return(portfolio)

    elif pilihan in ["6", "exit", "quit", "keluar"]:

        jumlah, modal, rata = portfolio_summary(portfolio)

        print("\n================================")
        print("Terima kasih telah menggunakan")
        print("Investment Portfolio Tracker")
        print("================================")
        print(f"Nama pengguna        : {nama_user}")
        print(f"Jumlah investasi     : {jumlah}")
        print(f"Total modal          : Rp {modal:,.0f}")
        print(f"Rata-rata return     : {rata:.2f}%")
        print("\nSampai jumpa kembali.")

        break

    else:

        print("\nPilihan tidak tersedia.")