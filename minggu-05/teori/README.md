# Input dan Output Python
> Pertemuan Minggu 5

Ada beberapa cara untuk mempresentasikan keluaran suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke berkas untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan.

# 7.1. Pemformatan Keluaran yang Lebih Menarik

Sejauh ini telah ditemukan dua cara penulisan nilai: expression statements dan fungsi print(). (Cara ketiga menggunakan write() metode objek berkas; berkas standar keluaran dapat dirujuk sebagai sys.stdout. Lihat Referensi Pustaka untuk informasi lebih lanjut tentang ini.)

- Untuk menggunakan formatted string literals, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, kita bisa menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

- Metode str.format() dari string membutuhkan lebih banyak upaya manual. kita masih akan menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi kita juga harus memberikan informasi yang akan diformat.

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

Ketika kita tidak membutuhkan keluaran yang menarik tetapi hanya ingin tampilan cepat dari beberapa variabel untuk keperluan debugging, kita dapat mengonversi nilai apa pun menjadi string dengan fungsi repr() atau str().

Beberapa contoh terdapat pada src/Bab7.py

# 7.1.1. Literal String Terformat

Formatted string literals (juga disebut f-string) memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}.

contoh terdapat pada src/Bab7.py

# 7.1.2. Metode String format()

Penggunaan dasar metode str.format() terlihat seperti ini:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter di dalamnya (disebut fields format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode str.format().

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

Jika argumen kata kunci keyword argument digunakan dalam metode str.format(), nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Argumen posisi dan kata kunci dapat dikombinasikan secara bergantian:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred'
other='Georg'))
The story of Bill, Manfred, and Georg.
```

Jika Anda memiliki string format yang sangat panjang yang tidak ingin Anda pisahkan, alangkah baiknya jika Anda bisa mereferensikan variabel yang akan diformat berdasarkan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewatkan dict dan menggunakan tanda kurung siku '[]' untuk mengakses kunci dari dict

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini juga bisa dilakukan dengan memberikan tabel sebagai argumen kata kunci keyword argument dengan notasi '**'.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

contoh terdapat pada src/Bab7.py

# 7.1.3. Pemformatan String Manual

Inilah tabel kotak dan kubus yang sama, yang diformat secara manual: dari contoh program 7.1.3.

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara print() berfungsi: selalu menambah spasi di antara argumennya.)

Metode str.rjust() dari objek string merata-kanan-kan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada metode serupa str.ljust() dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda, tetapi itu biasanya lebih baik daripada alternatif, yang akan berbohong tentang nilai.

Ada metode lain, str.zfill(), yang melapisi string numerik di sebelah kiri dengan nol. Itu mengerti tentang tanda plus dan minus:

```python
Ada metode lain, str.zfill(), yang melapisi string numerik di sebelah kiri dengan nol. Itu mengerti tentang tanda plus dan minus:
```

# 7.1.4. Pemformatan string lama

Operator % (modulo) juga dapat digunakan untuk pemformatan string. Diberikan 'string' % values, instansiasi dari % in string diganti dengan nol atau elemen yang lebih dari values. Operasi ini umumnya dikenal sebagai interpolasi string. Sebagai contoh:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

# 7.2. Membaca dan Menulis Berkas

open() mengembalikan sebuah file object, dan paling umum digunakan dengan dua argumen: open(filename, mode).

```python
>>> f = open('workfile', 'w')
```

Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menggambarkan cara berkas akan digunakan. mode dapat 'r' ketika file hanya akan dibaca, 'w' untuk hanya menulis (berkas yang ada dengan nama yang sama akan dihapus), dan 'a' membuka berkas untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir. 'r+' membuka berkas untuk membaca dan menulis. Argumen mode adalah opsional; 'r' akan diasumsikan jika dihilangkan.

Dalam mode teks, standar saat membaca adalah mengonversi akhir baris spesifik platform (\n pada Unix, \r\n pada Windows) menjadi hanya \n. Saat menulis dalam mode teks, defaultnya adalah mengonversi kemunculan \n kembali ke akhir baris spesifik platform. Modifikasi di balik layar ini untuk mengarsipkan data baik untuk file teks, tetapi akan merusak data biner seperti itu di JPEG atau berkas EXE. Berhati-hatilah untuk menggunakan mode biner saat membaca dan menulis file seperti itu.

Ini adalah praktik yang baik untuk menggunakan kata kunci with saat berurusan dengan objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika suatu pengecualian muncul di beberapa titik. Menggunakan with juga jauh lebih pendek daripada penulisan yang setara try-blok finally:

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Jika anda tidak menggunakan kata kunci with, maka anda harus memanggil f.close() untuk menutup file dan membebaskan sumber daya sistem yang digunakan secara langsung.

Setelah objek file ditutup, baik dengan pernyataan with atau dengan memanggil f.close(), upaya untuk menggunakan objek file akan secara otomatis gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

# 7.2.1. Metode Objek Berkas

Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Ketika size dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file tersebut dua kali lebih besar dari memori mesin Anda. Kalau tidak, paling banyak size karakter (dalam mode teks) atau size byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read() akan mengembalikan string kosong ('').

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

f.readline() membaca satu baris dari file; karakter baris baru (\n) dibiarkan di akhir string, dan hanya dihapus pada baris terakhir file jika file tidak berakhir pada baris baru. Ini membuat nilai pengembalian tidak ambigu; jika f.readline() mengembalikan string kosong, akhir file telah tercapai, sementara baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, Anda dapat mengulangi objek berkas. Ini hemat memori, cepat, dan mengarah ke kode sederhana

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
Jika Anda ingin membaca semua baris file dalam daftar list, Anda juga dapat menggunakan list(f) atau f.readlines().

f.write(string) menulis konten string ke berkas, mengembalikan jumlah karakter yang ditulis.

```python
>>> f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi -- baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) -- sebelum menulisnya:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```
f.tell() mengembalikan integer yang memberikan posisi objek file saat ini dalam berkas yang direpresentasikan sebagai jumlah byte dari awal berkas ketika dalam mode biner dan angka buram opaque ketika dalam mode teks.

Untuk mengubah posisi objek file, gunakan f.seek(offset, whence). Posisi dihitung dari menambahkan offset ke titik referensi; titik referensi dipilih oleh argumen whence. Nilai A whence dari 0 mengukur dari awal berkas, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. whence dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```
Dalam file teks (yang dibuka tanpa b dalam mode string), hanya mencari relatif ke awal file yang diizinkan (pengecualian sedang mencari sampai akhir file dengan seek(0, 2)) dan satu-satunya nilai offset yang valid adalah yang dikembalikan dari f.tell(), atau nol. Nilai offset lainnya menghasilkan perilaku tidak terdefinisi.

Objek file memiliki beberapa metode tambahan, seperti isatty() dan truncate() yang lebih jarang digunakan; bacalah Referensi Pustaka untuk panduan lengkap untuk objek berkas.

# 7.2.2. Menyimpan data terstruktur dengan json

String dapat dengan mudah ditulis dan dibaca dari file. Angka membutuhkan sedikit usaha, karena metode read() hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil string seperti '123' dan mengembalikan nilai numerik 123. Ketika Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar list dan dictionary bersarang, penguraian dan pembuatan serialisasi dengan tangan menjadi rumit.

Alih-alih membuat pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke berkas, Python memungkinkan Anda untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation). Modul standar bernama json dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serializing. Merekonstruksi data dari representasi string disebut deserializing. Antara serializing dan deserializing, string yang mewakili objek mungkin telah disimpan dalam berkas atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

Varian lain dari fungsi dumps(), disebut dump(), dengan mudah membuat serialisasi objek menjadi :term: text file. Jadi jika f adalah objek text file dibuka untuk menulis, kita dapat melakukan ini:

```python
json.dump(x, f)
```
Untuk menerjemahkan decode objek lagi, jika f adalah objek text file yang telah dibuka untuk membaca:

```python
x = json.load(f)
```
Teknik serialisasi sederhana ini dapat menangani daftar list dan dictionary, tetapi membuat serialisasi instance kelas yang berubah-ubah arbitrary di JSON membutuhkan sedikit usaha ekstra. Referensi untuk modul json berisi penjelasan tentang ini.

contoh terdapat pada src/Bab7.py