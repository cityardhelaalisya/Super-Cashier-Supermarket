from tabulate import tabulate

class Transaction:
    # Class Variabel dari class Transaction yang akan menampung seluruh data belanjaan
    data_keranjang = {}


    def add_item(self, nama_item, jumlah_item, harga_per_item):
        """Menampilkan method add_item untuk menambahkan barang yang ingin di beli ke dalam data_keranjang"""
        self.data_keranjang.update({nama_item : [jumlah_item, harga_per_item]})
        return f"Item yang dibeli adalah: {self.data_keranjang}"

    def update_item_nama(self, nama_item, update_nama_item):
        """Method update nama yang akan memperbarui nama barang yang keliru
        
        (Nama) dikategorikan key di data_keranjang dictionary maka kita harus memperbarui key tersebut
        """
        self.data_keranjang[update_nama_item] = self.data_keranjang.pop(nama_item)
        return self.data_keranjang

    def update_item_jumlah(self, nama_item, update_jumlah_item):
        """Method update jumlah yang akan memperbarui jumlah barang yang keliru saat penginputan
        
        (Jumlah) termasuk value yang bertipe list urutan pertama di dictionary data_keranjang maka updatenya menggunakan Indeks[0]
        """
        self.data_keranjang[nama_item][0] = update_jumlah_item 
        return self.data_keranjang

    def update_item_harga(self, nama_item, update_harga_item):
        """Method update harga yang akan memperbarui harga barang yang keliru saat penginputan

        (Harga) termasuk value yang bertipe list urutan kedua di dictionary data_keranjang maka updatenya menggunakan Indeks[1]
        """
        self.data_keranjang[nama_item][1] = update_harga_item
        return self.data_keranjang

    def delete_item(self, nama_item):
        """Method delete ini menghapus salah satu barang dengan parameter nama barang"""
        del self.data_keranjang[nama_item]
        return self.data_keranjang

    def reset_transaction(self):
        """Method reset ini berfungsi menghapus seluruh barang yang ada di data_keranjang"""
        self.data_keranjang.clear()
        return f"Semua item berhasil di delete!"
        
    
    def check_order(self):
        """Method check_order untuk mengecek apakah input barang belanjaan ada yang bernilai 0 atau ("") """
        table_data = [
                        [index, name, qty, price, qty * price]
                        for index, (name, (qty, price)) in enumerate(self.data_keranjang.items(), start=1)
                    ]       # membuat table data belanjaan dengan index
        print(tabulate(table_data, headers=["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"], tablefmt="grid"))
       
        for key, value in self.data_keranjang.items():      # membuat for loop dan branching untuk memfilter data yang bernilai 0 atau ""
            if key != "" and value[0] > 0 and value[1] > 0:
                print("Pemesanan Benar")
            else:
                print("Terdapat kesalahan dipesanan!")
    
    
    def total_price(self):
        """Method Total_price untuk menghitung total harga belanjaan"""
        try:
            
            info_item_keranjang = self.data_keranjang.values()      # variabel info_item_keranjang menampung values berupa jumlah dan harga dalam type list dari data_keranjang
            total_harga = 0
            for info in info_item_keranjang:            # menggunakan for loop untuk mengakses list
                total_harga += (info[0] * info[1])      # total_harga = Info[0] berisi jumlah barang x info[1] berisi harga barang
                                                        
        
            """Pengelompokkan diskon berdasarkan kriteria total belanja"""
            if total_harga > 500000 :       # pelanggan akan mendapatkan diskon 10% setiap pembelian dengan total harga melebihi 500.000
                diskon = 0.1
                total_harga_setelah_diskon = total_harga - (total_harga * diskon)
                return f"Selamat, Anda mendapatkan Diskon 10%.\nTotal belanja yang harus dibayarkan adalah Rp.{total_harga_setelah_diskon}"
            elif total_harga > 300000 and total_harga <=500000:         # pelanggan akan mendapatkan diskon 8% setiap pembelian dengan total harga melebihi 300.000,- dan di bawah 500.000,-
                diskon = 0.08
                total_harga_setelah_diskon = total_harga - (total_harga * diskon)
                return f"Selamat, Anda mendapatkan Diskon 8%.\nTotal belanja yang harus dibayarkan adalah Rp.{total_harga_setelah_diskon}"
            elif total_harga > 200000 and total_harga <=300000:     # pelanggan akan mendapatkan diskon 5% setiap pembelian dengan total harga melebihi 200.000,- dan di bawah 300.000,-
                diskon = 0.05
                total_harga_setelah_diskon = total_harga - (total_harga * diskon)
                return f"Selamat, Anda mendapatkan Diskon 5%.\nTotal belanja yang harus dibayarkan adalah Rp.{total_harga_setelah_diskon}"
            
            else:       # pelanggan tidak mendapatkan diskon setiap pembelian dengan total harga di bawah 200.000,
                return f"Total belanja yang harus dibayarkan adalah Rp.{total_harga}"
        except ValueError:
            print("ERROR!")


