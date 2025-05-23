# Super-Cashier-di-Supermarket-Andi

# Latar Belakang Problems
Salah satu supermarket besar di Indonesia ingin melakukan perbaikan proses bisnis. Andi, sebagai pemiliki supermarket tersebut, ingin membuat Sistem Kasir yang self-service sehingga memudahkan pelanggan yang berada di luar kota untuk belanja. Andi membayar beberapa progammer untuk membuat program yang berisi fitur-fitur yang diperlukan.

# Requirements/Objective yang dibutuhkan
Terdapat beberapa Requirements yang dimasukkan di module Transanction, yaitu: <br>
1. id: id customer yang harus diinputkan untuk menggunakan Super-Cashier dalam metode input <br>
2. add_item(): Method untuk menambahkan item <br>
3. update_item...: Method untuk memperbarui rincian informasi barang yang sudah masuk ke keranjang. <br>
   a. update_item_nama(): Method untuk memperbarui nama item <br>
   b. update_item_jumlah(): Method untuk memperbarui jumlah item <br>
   c. update_item_harga(): Method untuk memperbarui harga item <br>
5. delete_item(): Method untuk menghapus salah satu item yang ada di keranjang
6. reset_transaction(): Method untuk menghapus seluruh item yang ada di keranjang
7. total_price(): Method untuk menghitung total harga seluruh item dan memberikan diskon bagi customer yang memenuhi syarat

# Flowchart Program Super-Cashier <br>
![Flowchart Program Super-Cashier](https://github.com/cityardhelaalisya/Super-Cashier-Supermarket/blob/main/flowchart%20super%20cashier.drawio.png)

# Hasil Test Case <br>
1. Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut.  
   a. Nama Item = Ayam Goreng, Qty = 2, Harga = 20000  
   b. Nama Item = Pasta Gigi, Qty = 3, Harga = 15000  

Code:<br>
trnsct_123 = Transaction()  
add_item1 = trnsct_123.add_item(nama_item="Ayam Goreng", jumlah_item=2, harga_per_item=20000)  
add_item2 = trnsct_123.add_item(nama_item="Pasta Gigi", jumlah_item=3, harga_per_item=15000)  
print("=====TEST CASE 1=====")  
print(f"Item yang dibeli adalah: {add_item2}")  

Outputnya menampilkan daftar item yang masuk ke data_keranjang:<br>
![Test Case 1](https://github.com/cityardhelaalisya/Super-Cashier-Supermarket/blob/main/github%20testcase%201.png)

2. Customer ingin menghapus salah satu item dengan Method delete_item() karena terjadi kesalahan. Item yang ingin dihapus adalah Pasta Gigi <br>

Code: <br>
delete_item_user = trnsct_123.delete_item(nama_item="Pasta Gigi")  
print("=====TEST CASE 2=====")  
print(f"{delete_item_user}")  

Ouput dari code di atas akan menghapus salah satu item: <br>
![Test Case 2](https://github.com/cityardhelaalisya/Super-Cashier-Supermarket/blob/main/github%20testcase%202.png)

3. Ternyata setelah dipikir-pikir customer salah memasukkan item yang ingin dibelanjakan!<br>
   Daripada menghapusnya satu-satu, maka customer cukup menggunakan reset_transaction() untuk menghapus semua item yang sudah ditambahkan

Code: <br>
reset_item_user = trnsct_123.reset_transaction()  
print("=====TEST CASE 3=====")  
print(f"{reset_item_user}")  

Dari code di atas menghasilkan ouput:<br>
![Test Case 3](https://github.com/cityardhelaalisya/Super-Cashier-Supermarket/blob/main/github%20testcase%203.png)


4. Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). <br>
   Sebelum mengeluarkan ouput total belanja akan menampilkan item-item yang dibeli.

Code: <br>
belanja_user = trnsct_123.add_item("Ayam Goreng", 2, 20000)  
belanja_user = trnsct_123.add_item("Pasta Gigi", 3, 15000)  
belanja_user = trnsct_123.add_item("Mainan Mobil", 1, 200000)  
belanja_user = trnsct_123.add_item("Mi Instan", 5, 3000)  
print("=====TEST CASE 4=====")  
print(f"Item yang dibeli adalah: {belanja_user}")  
print(trnsct_123.total_price())  

Dari code di atas menghasilkan output: <br>
![Test Case 4](https://github.com/cityardhelaalisya/Super-Cashier-Supermarket/blob/main/github%20testcase%204.png)


# Conclusion<br>
Dari pembuatan program Super-Cashier di supermarket Andi, seluruh fitur yang dibutuhkan dapat berjalan dengan baik.  
Di file github ini, saya membuat 2 file untuk menjalankan program yang ada di module Transaction.py.  
1. test-case.py : di module ini, kita menggunakan object class yang membutuhkan penulisan syntax classnya  
2. sistem_kasir.py : di module ini, kita akan menjalankan program lalu menginputkan pilihan menu yang ada atau sudah dalam bentuk sistemnya
  
