
# Retail Management System

## Deskripsi Aplikasi
Aplikasi ini dirancang untuk membantu staf usaha retail skala kecil dalam mengelola produk dan mencatat transaksi penjualan.

## Cara Menjalankan Aplikasi
1. Pastikan MySQL telah terinstal di komputer Anda dan buat database dengan menggunakan file `dump.sql` yang telah disediakan.
2. Pastikan Python 3.x telah terinstal, bersama dengan pustaka:
   - `tkinter`
   - `mysql-connector-python`
3. Jalankan file Python utama menggunakan perintah:
   ```
   python main.py
   ```

## Struktur Tabel Database
1. **Tabel Products**
   - `id`: Primary Key, Auto Increment
   - `name`: Nama produk
   - `price`: Harga produk

2. **Tabel Transactions**
   - `id`: Primary Key, Auto Increment
   - `product_id`: Foreign Key ke tabel `products`
   - `quantity`: Jumlah produk yang dibeli
   - `total_price`: Total harga transaksi
   - `transaction_date`: Tanggal transaksi
