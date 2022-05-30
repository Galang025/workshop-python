# Jupyter
## JupyterLab
Instal JupyterLab dengan pip:
```
$ pip install jupyterlab
```
> Catatan: Jika Anda menginstal JupyterLab dengan conda atau mamba, kami sarankan menggunakan saluran conda-forge.

Setelah terinstal, luncurkan JupyterLab dengan:
```
$ jupyter-lab
```
Jupyter Notebook
Instal Jupyter Notebook klasik dengan:
```
$ pip install notebook
```
untuk menjalankan notebook
```
$ jupyter notebook
```
# praktikum minggu ke 3 (struktur data) menggunakan Jupyter.

## 5.1. More on Lists 

Tipe data daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar:

list. append(x)
Menambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x].

list. extend (dapat diulang)
Perluas daftar dengan menambahkan semua item dari yang dapat diulang. Setara dengan a[len(a):] = iterable.

list. insert(i, x)
Menyisipkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang sebelumnya disisipkan, sehingga a.  insert(0, x) menyisipkan di bagian depan daftar, dan a. insert(len(a), x) setara dengan a.append(x).

list. remove(x)
Hapus item pertama dari daftar yang nilainya sama dengan x. Ini meningkatkan ValueError jika tidak ada item seperti itu.

list. pop([i])
Hapus item pada posisi tertentu dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() akan menghapus dan mengembalikan item terakhir dalam daftar. (Tanda kurung siku di sekitar  i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetik tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)

list. clear()
Hapus semua item dari daftar. Setara dengan del a[:].

list. index(x[, start[, end]])
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Meningkatkan ValueError jika tidak ada item seperti itu.
Argumen opsional mulai dan berakhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke subsekuensi tertentu dari daftar. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada  argumen awal.

list. count(x)
Kembalikan berapa kali x muncul dalam daftar.

list. sort(*, key=None, reverse=False)
Mengurutkan item daftar di tempat (argumen dapat digunakan untuk kustomisasi pengurutan, lihat diurutkan() untuk penjelasannya).

list. reverse()
Membalikkan elemen daftar di tempatnya.

list. copy()
Kembalikan salinan daftar yang dangkal. Setara dengan a[:].

## 5.1.1. Using Lists as Stacks
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke bagian atas tumpukan, gunakan tambahkan(). Untuk mengambil item dari bagian atas tumpukan, gunakan pop() tanpa indeks eksplisit. Misalnya:

## 5.1.2. Using Lists as Queues

Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara penambahan dan letupan dari akhir daftar cepat, melakukan sisipan atau letupan dari awal daftar lambat (karena semua elemen lain harus digeser oleh satu).

Untuk menerapkan antrean, gunakan collections.deque yang dirancang untuk memiliki penambahan dan letupan cepat dari kedua ujungnya. Misalnya:

## 5.1.3. List Comprehensions

Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota urutan lain atau dapat diulang, atau untuk membuat subsequence dari elemen-elemen yang memenuhi kondisi tertentu.

Misalnya, asumsikan kita ingin membuat daftar kotak, seperti:

## 5.1.4. Nested List Comprehensions

Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi sewenang-wenang, termasuk pemahaman daftar lainnya.

Pertimbangkan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar 3 daftar panjang 4:

[Link kode](../src/5.1..ipynb) 
## 5.2. The del statement

Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: pernyataan del. Ini berbeda dari  metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kami lakukan sebelumnya dengan menetapkan daftar kosong ke irisan). Misalnya:

[Link kode](../src/5.2..ipynb) 
## 5.3. Tuples and Sequences

Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh  tipe data urutan (lihat Jenis Urutan — daftar, tupel, rentang). Karena Python adalah bahasa yang berkembang, jenis data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tupel.

Tupel terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:

[Link kode](../src/5.3..ipynb) 
## 5.4. Sets

Python juga menyertakan tipe data untuk set. Satu set adalah koleksi yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Objek yang ditetapkan juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

Kurung kurawal keriting atau fungsi set() dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang kita bahas di bagian selanjutnya.

Berikut adalah demonstrasi singkatnya:

[Link kode](../src/5.4..ipynb) 
## 5.5. Dictionaries

Tipe data berguna lainnya yang dibangun ke dalam Python adalah kamus (lihat Jenis Pemetaan — dikte). Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "kenangan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa jenis yang tidak dapat diubah; string dan angka selalu dapat menjadi kunci. Tupel dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika tupel berisi objek yang dapat diubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append() dan extend().

Yang terbaik adalah menganggap kamus sebagai satu set kunci: pasangan nilai, dengan persyaratan bahwa kuncinya unik (dalam satu kamus). Sepasang kawat gigi membuat kamus kosong: {}. Menempatkan daftar pasangan key:value yang dipisahkan koma di dalam kurung kurawal akan menambahkan pasangan key:value awal ke kamus; ini juga cara kamus ditulis pada output.

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci. Dimungkinkan juga untuk menghapus pasangan key:value dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan dilupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.

Melakukan list(d) pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin mengurutkannya, cukup gunakan sorted(d) sebagai gantinya). Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan  kata kunci dalam.

Berikut adalah contoh kecil menggunakan kamus:

[Link kode](../src/5.5..ipynb) 
## 5.6. Looping Techniques

Saat mengulang kamus, kunci dan nilai yang sesuai dapat diambil secara bersamaan menggunakan metode items().

[Link kode](../src/5.6..ipynb) 
## 5.7. More on Conditions

Kondisi yang digunakan dalam pernyataan sementara dan jika dapat berisi operator apa pun, bukan hanya perbandingan.

Operator pembanding di dalam dan tidak masuk adalah tes keanggotaan yang menentukan apakah suatu nilai berada dalam (atau tidak dalam) suatu kontainer. Operator adalah dan  tidak membandingkan apakah dua objek benar-benar objek yang sama. Semua operator perbandingan memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.

Perbandingan dapat dirantai. Misalnya,  a < b == c menguji apakah a kurang dari b dan apalagi b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan tidak. Ini memiliki prioritas yang lebih rendah daripada operator perbandingan; di antara mereka, tidak memiliki prioritas tertinggi dan atau terendah, sehingga A dan bukan B atau C setara dengan (A dan (bukan B)) atau C. Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean dan dan atau disebut  operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C benar tetapi B salah, A dan B dan C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai pengembalian operator hubung singkat adalah argumen terakhir yang dievaluasi.

Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Misalnya

[Link kode](../src/5.7..ipynb) 
## 5.8. Comparing Sequences and Other Types

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutannya dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih rendah). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antara urutan dengan jenis yang sama:

[Link kode](../src/5.8..ipynb) 

