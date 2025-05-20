from transaction import Transaction
from opsi_pengiriman import OpsiPengiriman

"""Test Case 1
Menambahkan barang belanjaan berupa Ayam Goreng : [2, 20000] dan Pasta gigi : [3, 15000]
"""
trnsct_123 = Transaction()
add_item1 = trnsct_123.add_item(nama_item="Ayam Goreng", jumlah_item=2, harga_per_item=20000)
add_item2 = trnsct_123.add_item(nama_item="Pasta Gigi", jumlah_item=3, harga_per_item=15000)
print("=====TEST CASE 1=====")
print(add_item2, "\n")

"""Test Case 2
Menghapus salah satu barang yang sudah diinput di data keranjang yaitu Pasta gigi
"""
delete_item_user = trnsct_123.delete_item(nama_item="Pasta Gigi")
print("=====TEST CASE 2=====")
print(f"{delete_item_user}\n")

"""Test Case 3
Menghapus seluruh barang di data_keranjang
"""
reset_item_user = trnsct_123.reset_transaction()
print("=====TEST CASE 3=====")
print(f"{reset_item_user}\n")

"""Test Case 4 
Menambahkan 4 barang ke dalam data keranjang untuk dihitung total harganya beserta diskon yang didapatkan
"""
belanja_user = trnsct_123.add_item("Ayam Goreng", 2, 20000)
belanja_user = trnsct_123.add_item("Pasta Gigi", 3, 15000)
belanja_user = trnsct_123.add_item("Mainan Mobil", 1, 200000)
belanja_user = trnsct_123.add_item("Mi Instan", 5, 3000)
print("=====TEST CASE 4=====")
print(f"Item yang dibeli adalah: {belanja_user}")
print(trnsct_123.total_price())
