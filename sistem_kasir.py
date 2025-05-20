"""Ini adalah sistem kasir yang menggunakan input untuk memasukkan parameter yang dibutuhkan dan terdiri dari menu yang bisa dipilih

Kita bisa mencoba case di test_case.py dengan metode input 
"""

import transaction as tr        # Import transactio.py dan class di dalamnya

print(f"=====Selamat Datang di Super-Cashier Supermarket Andi=====")

id = str(input("Masukkan id Anda: "))
id = tr.Transaction()       # id di sini sama fungsinya sebagai objek class

while True:     # while loop ini akan berjalan terus menerus sampai ada kesalahan
    print(f"\n============Menu Super-Cashier============")
    print("1. Tambah Barang\n2. Update Barang(Nama, Jumlah, Harga)\n3. Delete Barang (Hanya Satu Barang)\n4. Reset Seluruh Barang Belanjaan\n5. Cek Pesanan\n6. Hitung Total Harga Belanjaan")
    # pilihan menu Super-Cashier
    try:
        menu = int(input("Silahkan Masukkan Pilihan Anda(1/2/3/4/5/6): "))      # hanya menerima input berupa integer
        if menu == 1:       # menu no.1 menampilkan method add_item()
            nama_item = str(input("Masukkan nama item: "))
            jumlah = int(input("Masukkan jumlah item: "))
            harga = int(input("Masukkan harga item: "))
            print(id.add_item(nama_item=nama_item, jumlah_item=jumlah, harga_per_item=harga))
        elif menu == 2:     # menu no.2 menampilkan method update_item_name(), update_item_qty(), update_item_price()
            pilihan_update = int(input("1. Update nama barang\n2. Update Jumlah Barang\n3. Update harga\nPilih Menu Update yang diinginkan(1/2/3): "))
            """ Terdapat 3 pilihan update yaitu nama, jumlah dan harga.
            
            untuk menyelaraskan inputan maka digunakan .title() pada branching di bawah 
            sehingga karaketer memiliki huruf kapital di setiap awal kata
            """
            if pilihan_update == 1:
                nama_lama = str(input("Masukkan nama barang yang mau diupdate: ").title())
                barang_baru = str(input("Masukkan nama terbaru: ").title())
                update_nama_barang = id.update_item_nama(nama_item=nama_lama, update_nama_item=barang_baru)
                print(update_nama_barang)
            elif pilihan_update == 2:
                nama_lama = str(input("Masukkan jumlah barang yang mau diupdate: ").title())
                jumlah_barang_baru = int(input("Masukkan jumlah terbaru: "))
                update_jumlah_barang = id.update_item_jumlah(nama_item=nama_lama, update_jumlah_item=jumlah_barang_baru)
                print(update_jumlah_barang)
            elif pilihan_update == 3:
                nama_lama = str(input("Masukkan harga barang yang mau diupdate: ").title())
                harga_barang_baru = int(input("Masukkan harga terbaru: "))
                update_harga_barang = id.update_item_harga(nama_item=nama_lama, update_harga_item=harga_barang_baru)
                print(update_harga_barang)
            else:
                raise Exception("Anda memasukkan pilihan menu yang salah!")

        elif menu == 3:     # menu no. 3 menampilkan Method delete_item()
            nama_barang = str(input("Masukkan nama barang: ").title())
            print(f"Item {nama_barang} berhasil dihapus!")
            print(id.delete_item(nama_item=nama_barang))
        elif menu == 4:     # menu no. 4 menampilkan Method reset_transaction()
            print(id.reset_transaction())
        elif menu == 5:     # menu no. 5 menampilkan Method check_order()
            print(id.check_order())
        elif menu == 6:     # menu no.6 menampilkan Method total_price()
            print("=====Total Belanjaan=====")
            print(id.total_price())
            break
        else:
            raise(ValueError)

    except ValueError:
        print("Format Tidak sesuai. Silahkan isi kembali!")
