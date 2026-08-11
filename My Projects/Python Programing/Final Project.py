#Final Project_Basic Phython


#Import Library
import os
from datetime import datetime
import pandas as pd
import requests

#Konstanta Program
DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "transactions.txt")

transactions = []

#Class Transaction
class Transaction:

    def __init__(self, date,
                 transaction_type,
                 category,
                 amount,
                 note):

        self.date = date
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {
            "Date": self.date,
            "Type": self.transaction_type,
            "Category": self.category,
            "Amount": self.amount,
            "Note": self.note
        }

    def to_line(self):

        return f"{self.date}|{self.transaction_type}|{self.category}|{self.amount}|{self.note}\n"


#Prepare Storage
def prepare_storage():

    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    if not os.path.exists(DATA_FILE):

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            pass


#Load Data
def load_data():

    try:

        with open(DATA_FILE, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                if len(data) != 5:
                    continue

                transaction = Transaction(
                    data[0],
                    data[1],
                    data[2],
                    float(data[3]),
                    data[4]
                )

                transactions.append(transaction)

    except FileNotFoundError:

        print("Sampai saat ini belum ada data transaksi.")


#menyimpan atau save Transaction
def save_transaction(transaction):

    with open(DATA_FILE, "a", encoding="utf-8") as file:

        file.write(transaction.to_line())

#Tambah Income
def add_income():

    print("\n=== ADD INCOME ===")

    category = input("Sumber pemasukan : ").strip()

    note = input("Keterangan        : ").strip()

    try:

        amount = float(input("Jumlah (Rp)      : "))

    except ValueError:

        print("Jumlah harus berupa angka.")
        return

    if amount <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    transaction = Transaction(
        date,
        "Income",
        category,
        amount,
        note
    )

    transactions.append(transaction)

    save_transaction(transaction)

    print("\nPemasukan berhasil disimpan.")

#Tambah Expense atau pengeluaran
def add_expense():

    print("\n=== ADD EXPENSE ===")

    category = input("Kategori          : ").strip()

    note = input("Keterangan         : ").strip()

    try:

        amount = float(input("Jumlah (Rp)       : "))

    except ValueError:

        print("Jumlah harus berupa angka.")
        return

    if amount <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    transaction = Transaction(
        date,
        "Expense",
        category,
        amount,
        note
    )

    transactions.append(transaction)

    save_transaction(transaction)

    print("\nPengeluaran berhasil disimpan.")


#tampilan main menu
def main_menu():

    while True:

        print("\n==============================")
        print(" STUDENT FINANCIAL ASSISTANT ")
        print("==============================")

        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Histori Transaksi")
        print("4. Dashboard")
        print("5. Spending Advisor")
        print("6. Export CSV")
        print("7. Currency Converter")
        print("8. Keluar")

        choice = input("\nPilih menu : ").strip()

        if choice == "1":

            add_income()

        elif choice == "2":

            add_expense()


        elif choice == "3":

            show_history()

        elif choice == "4":

            dashboard()

        elif choice == "5":

            spending_advisor()

            financial_status()

            money_prediction()

        elif choice == "6":

            export_csv()

        elif choice == "7":

            currency_converter()

        elif choice == "8":

            print("\n==============================")

            print(" TERIMA KASIH ")

            print("==============================")

            print(f"Total Saldo : {rupiah(calculate_balance())}")

            print(f"Jumlah Transaksi : {len(transactions)}")

            print("\nSampai jumpa!")

            break

        else:

            print("\nMenu tidak tersedia mas, baca mas cuma sampai 8.")


#Membuat Fungsi Format Rupiah
def rupiah(amount):
    return f"Rp{amount:,.0f}".replace(",", ".")

#Menghitung saldo
def calculate_balance():

    balance = 0

    for transaction in transactions:

        if transaction.transaction_type == "Income":
            balance += transaction.amount

        else:
            balance -= transaction.amount

    return balance


#Menghitung total Income
def total_income():

    income = 0

    for transaction in transactions:

        if transaction.transaction_type == "Income":

            income += transaction.amount

    return income

#Menghitung Total Expense
def total_expense():

    expense = 0

    for transaction in transactions:

        if transaction.transaction_type == "Expense":

            expense += transaction.amount

    return expense

#Histori Transaksi
def show_history():

    if len(transactions) == 0:

        print("\nBelum ada transaksi.")

        return

    data = []

    for transaction in transactions:

        data.append(transaction.to_dict())

    df = pd.DataFrame(data)

    df["Amount"] = df["Amount"].apply(rupiah)

    print("\n========== HISTORI TRANSAKSI ==========")

    print(df.to_string(index=False))


#Dashboard
def dashboard():

    if len(transactions) == 0:

        print("\nBelum ada transaksi.")

        return

    income = total_income()

    expense = total_expense()

    balance = calculate_balance()

    print("\n==============================")
    print(" FINANCIAL DASHBOARD ")
    print("==============================")

    print(f"Total Income      : {rupiah(income)}")

    print(f"Total Expense     : {rupiah(expense)}")

    print(f"Current Balance   : {rupiah(balance)}")

    print(f"Jumlah Transaksi  : {len(transactions)}")



#Kategorisasi Pengeluaran Terbesar
    expense_category = {}

    for transaction in transactions:

        if transaction.transaction_type == "Expense":

            if transaction.category in expense_category:

                expense_category[transaction.category] += transaction.amount

            else:

                expense_category[transaction.category] = transaction.amount

    if expense_category:

        biggest = max(expense_category,
                      key=expense_category.get)

        print(f"Kategori Terbesar : {biggest}")

        print(f"Total             : {rupiah(expense_category[biggest])}")

#Tambahkan Fungsi zPengeluaran Harian Rata-rata
def average_expense_per_transaction():

    expense = total_expense()

    if len(transactions) == 0:
        return 0

    expense_transaction = 0

    for transaction in transactions:

        if transaction.transaction_type == "Expense":

            expense_transaction += 1

    if expense_transaction == 0:
        return 0

    return expense / expense_transaction

#Buat Spending advisor
def spending_advisor():

    balance = calculate_balance()

    if balance <= 0:

        print("\nSaldo Anda habis.")

        return

    try:

        days = int(input("\nUang ini ingin cukup berapa hari lagi? : "))

        if days <= 0:

            print("Jumlah hari harus lebih dari 0.")

            return

    except ValueError:

        print("Masukkan angka.")

        return

    daily_limit = balance / days

    print("\n==============================")
    print(" SPENDING ADVISOR ")
    print("==============================")

    print(f"Saldo Anda             : {rupiah(balance)}")
    print(f"Target Hari            : {days}")
    print(f"Maksimal per Hari      : {rupiah(daily_limit)}")


    average = average_expense_per_transaction()

    print(f"Rata-rata Pengeluaran  : {rupiah(average)}")

    if average > daily_limit:
        print("\n⚠ PERINGATAN")

        print("Pengeluaran Anda biasanya")

        print("lebih besar dari batas harian.")

        print("Kurangi pengeluaran agar uang cukup.")

#Status Finansial
def financial_status():

    income = total_income()

    expense = total_expense()

    if income == 0:

        return

    saving_rate = ((income - expense) / income) * 100

    print("\n==============================")
    print(" FINANCIAL STATUS ")
    print("==============================")

    print(f"Saving Rate : {saving_rate:.1f}%")

    if saving_rate >= 40:

        print("Excellent! Anda sangat hemat.")

    elif saving_rate >= 20:

        print("Good. Keuangan Anda cukup sehat.")

    elif saving_rate >= 10:

        print("Cukup baik, tetapi masih bisa diperbaiki.")

    else:

        print("Pengeluaran Anda terlalu tinggi.")


#Prediksi Uang akan Habis
def money_prediction():

    average = average_expense_per_transaction()

    balance = calculate_balance()

    if average == 0:

        print("\nBelum ada data pengeluaran.")

        return

    prediction = balance / average

    print("\n==============================")
    print(" MONEY PREDICTION ")
    print("==============================")

    print(f"Saldo Saat Ini : {rupiah(balance)}")

    print(f"Rata-rata Pengeluaran : {rupiah(average)}")

    print(f"Perkiraan uang habis dalam {prediction:.0f} hari.")

#Buat-export CSV
def export_csv():

    if len(transactions) == 0:

        print("\nBelum ada transaksi.")

        return

    data = []

    for transaction in transactions:

        data.append(transaction.to_dict())

    df = pd.DataFrame(data)

    filename = "report.csv"

    df.to_csv(
        filename,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nLaporan berhasil disimpan.")

    print(f"Nama File : {filename}")


#Menggunakan Currency Converter
def currency_converter():

    balance = calculate_balance()

    if balance <= 0:

        print("\nSaldo tidak tersedia.")

        return

    try:

        response = requests.get(
            "https://open.er-api.com/v6/latest/IDR",
            timeout=10
        )

        data = response.json()

        usd_rate = data["rates"]["USD"]

        usd = balance * usd_rate

        print("\n==============================")

        print(" CURRENCY CONVERTER ")

        print("==============================")

        print(f"Saldo Rupiah : {rupiah(balance)}")

        print(f"Saldo USD    : ${usd:.2f}")

    except Exception:

        print("\nGagal mengambil kurs.")



prepare_storage()

load_data()

main_menu()

