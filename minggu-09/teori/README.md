# 11. Tur Singkat Pustaka Standar --- Bagian II
Tur kedua ini mencakup modul lanjutan yang mendukung kebutuhan pemrograman profesional. Modul-modul ini jarang terjadi dalam skrip kecil.
## 11.1. Pemformatan Output
Modul reprlib menyediakan versi repr() yang disesuaikan untuk tampilan yang disingkat dari wadah containers yang besar atau sangat bersarang
```py
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```
Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh interpreter. Ketika hasilnya lebih dari satu baris, "pretty printer" menambahkan jeda baris dan indentasi untuk lebih jelas mengungkapkan struktur data:
```py
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```
Modul textwrap memformat paragraf teks agar sesuai dengan lebar layar yang diberikan:
```py 
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
Modul locale mengakses basis data format data kultur khusus. Atribut pengelompokan fungsi format lokal locale menyediakan cara langsung memformat angka dengan pemisah grup:
```py
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```
## 11.2. Templating
Modul string menyertakan kelas serbaguna Template dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.

Format ini menggunakan nama penampung yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengitari placeholder dengan kurung kurawal memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ menciptakan satu yang terpisah $
```py
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```
Metode substitute() memunculkan KeyError saat placeholder tidak disertakan dalam dictionary atau argumen kata kunci keyword argument. Untuk aplikasi gaya gabungan-surat mail-merge, data yang diberikan pengguna mungkin tidak lengkap dan metode safe_substitute() mungkin lebih tepat --- itu akan membuat placeholder tidak berubah jika data hilang
```py
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
Subkelas templat dapat menentukan pembatas khusus. Misalnya, utilitas penggantian nama setumpuk batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk penampung seperti tanggal saat ini, nomor urut gambar, atau format berkas:
```py
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```
Aplikasi lain untuk templating adalah memisahkan logika program dari detail berbagai format output. Ini memungkinkan untuk mengganti templat khusus untuk file XML, laporan teks biasa, dan laporan web HTML.
## 11.3. Bekerja dengan Tata Letak Rekam Data Biner
Modul struct menyediakan pack() dan unpack() berfungsi untuk bekerja dengan format rekaman biner yang memiliki panjang variabel. Contoh berikut menunjukkan bagaimana cara loop tajuk header informasi dalam berkas ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" masing-masing mewakili dua dan empat byte angka yang tidak bertanda unsigned. "<" Menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian:
```py
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```
## 11.4. Multi-threading
Threading adalah teknik untuk memisahkan tugas yang tidak tergantung secara berurutan. Utas threads dapat digunakan untuk meningkatkan responsif aplikasi yang menerima masukan pengguna saat tugas lain beroperasi di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan perhitungan di utas thread lainnya.

Kode berikut menunjukkan bagaimana tingkat tinggi modul:mod:threading dapat menjalankan tugas di latar belakang sementara program utama terus beroperasi:
```py
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```
Tantangan utama aplikasi multi-utas multi-threaded adalah mengoordinasikan utas thread yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci locks, peristiwa events, variabel kondisi, dan semafor.

Sementara alat-alat itu berdaya, kesalahan desain kecil dapat menyebabkan masalah yang sulit untuk direproduksi. Jadi, pendekatan yang lebih disukai untuk koordinasi tugas adalah untuk memusatkan semua akses ke sumber daya dalam satu utas thread dan kemudian menggunakan modul queue untuk menyuapi utas thread tersebut dengan permintaan dari utas lainnya. Aplikasi yang menggunakan objek Queue untuk komunikasi dan koordinasi antar-utas inter-thread lebih mudah untuk dirancang, lebih mudah dibaca, dan lebih dapat diandalkan.
## 11.5. Pencatatan
Modul logging menawarkan sistem pencatatan logging yang lengkap dan fleksibel. Paling sederhana, catatan log pesan dikirim ke berkas atau ke sys.stderr:
```py
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
Ini menghasilkan keluaran berikut:
```
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```
Secara bawaan, pesan informasi dan debugging ditutupi suppressed dan keluaran dikirim ke standar kesalahan. Opsi keluaran lainnya termasuk merutekan pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih rute berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.

Sistem pencatatan dapat dikonfigurasikan secara langsung dari Python atau dapat dimuat dari berkas konfigurasi yang dapat diedit pengguna untuk pencatatan yang disesuaikan tanpa mengubah aplikasi.
## 11.6. Referensi yang Lemah
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan garbage collection untuk menghilangkan siklus). Memori dibebaskan tidak lama setelah referensi terakhir untuk itu telah dihilangkan.

Pendekatan ini berfungsi dengan baik untuk sebagian besar aplikasi tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain. Sayangnya, hanya melacak mereka membuat referensi yang membuatnya permanen. Modul weakref menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, itu secara otomatis dihapus dari tabel weakref dan panggilan balik callback dipicu untuk weakref. Aplikasi yang umum termasuk caching objek yang mahal untuk dibuat:
```py
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python38/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```
## 11.7. Alat untuk Bekerja dengan Daftar Lists
Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar list bawaan. Namun, kadang-kadang ada kebutuhan untuk implementasi alternatif dengan mengorbankan kinerja yang menurun.

Modul array menyediakan objek array() yang seperti daftar list dimana hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Contoh berikut menunjukkan array angka yang disimpan sebagai dua byte angka biner yang tidak ditandai (kode tipe "H") daripada 16 byte per entri biasa untuk daftar list reguler objek int Python:
```py
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```
Modul collections menyediakan objek deque() yang seperti daftar list dengan tambahan yang lebih cepat dan muncul dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas breadth first tree searches:
```py
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```
```py
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```
Selain implementasi daftar list alternatif, di pustaka juga menawarkan alat-alat lain seperti modul bisect dengan fungsi untuk memanipulasi daftar list yang diurutkan:
```py
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```
Modul heapq menyediakan fungsi untuk mengimplementasikan heaps berdasarkan daftar list reguler. Entri dengan nilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin mengoperasikan daftar pengurutan list secara penuh:
```py
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```
## 11.8. Aritmatika Pecahan Floating Point Desimal
Modul decimal menawarkan Decimal tipe data untuk aritmatika pecahan desimal. Dibandingkan dengan implementasi bawaan float dari pecahan floating point biner, kelas ini sangat membantu
- aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat,

- kontrol atas presisi,

- kontrol atas pembulatan untuk memenuhi persyaratan sah legal atau peraturan,

- pelacakan tempat desimal yang signifikan, atau

- aplikasi tempat pengguna mengharapkan hasil agar sesuai dengan perhitungan yang dilakukan dengan tangan.

Misalnya, menghitung pajak 5% pada biaya telepon 70 sen memberikan hasil berbeda dalam pecahan floating point desimal dan pecahan floating point biner. Perbedaannya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat:
```py
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
Hasil Decimal menjaga akhiran trailing nol, secara otomatis menyimpulkan empat tempat signifikansi dari multiplicands dengan dua tempat signifikansi. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika pecahan floating point biner tidak dapat secara tepat mewakili jumlah desimal.

Representasi yang tepat memungkinkan kelas Decimal untuk melakukan perhitungan modulo dan tes persamaan yang tidak cocok untuk angka pecahan floating point biner:
```py
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
```
Modul decimal menyediakan aritmatika dengan ketelitian sebanyak yang dibutuhkan:
```py
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```