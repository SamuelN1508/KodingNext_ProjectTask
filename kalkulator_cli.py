def main():
    print("=" * 35)
    print("   PROGRAM KALKULATOR DISKON")
    print("=" * 35)

    # 1. Mengambil input dari pengguna
    try:
        harga_asli = float(input("Masukkan harga asli (Rp): "))
        diskon = float(input("Masukkan diskon (%): "))
    except ValueError:
        print("Error: Harap masukkan angka yang valid!")
        return

    # 2. Rumus perhitungan diskon
    potongan = harga_asli * (diskon / 100)
    total_bayar = harga_asli - potongan

    # 3. Menampilkan rincian hasil
    print("-" * 35)
    print(f"Harga Asli    : Rp {harga_asli:,.2f}")
    print(f"Diskon ({diskon:.0f}%)   : Rp {potongan:,.2f}")
    print(f"Total Bayar   : Rp {total_bayar:,.2f}")
    print("=" * 35)


if __name__ == "__main__":
    main()
