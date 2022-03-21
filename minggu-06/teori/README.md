# Kesalahan errors dan Pengecualian exceptions
> Pertemuan Minggu 6

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: syntax errors dan exceptions.
# 8.1. Kesalahan Sintaksis
Kesalahan sintaksis, juga dikenal sebagai kesalahan penguraian parsing, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python:
```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
# 8.2. Pengecualian
Bahkan jika suatu pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut exceptions dan tidak fatal tanpa syarat: Anda akan segera belajar cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```
# 8.3. Menangani Pengecualian
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Lihatlah contoh berikut, yang meminta masukan dari pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menghentikan program (menggunakan Control-C atau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya pengecualian KeyboardInterrupt.
```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```
Pernyataan try berfungsi sebagai berikut.

- Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci try dan except) dieksekusi.

- Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: try selesai.

- Jika pengecualian terjadi selama eksekusi klausa try, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai dengan kata kunci exception, klausa except dioperasikan, dan kemudian eksekusi berlanjut setelah pernyataan try.

- Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke luar pernyataan try; jika tidak ada penangan yang ditemukan, ini adalah unhandled exception dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan try mungkin memiliki lebih dari satu klausa except, untuk menentukan penangan dari berbagai pengecualian. Paling banyak satu penangan akan dieksekusi. Penangan hanya menangani pengecualian yang terjadi pada klausa try yang sesuai, bukan pada penangan lain yang sama pernyataan try. Klausa except dapat menyebutkan beberapa pengecualian sebagai tanda kurung tuple, misalnya:
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
# 8.4. Memunculkan Pengecualian
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Sebagai contoh:
```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
Satu-satunya argumen untuk raise menunjukkan pengecualian yang dimunculkan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari Exception). Jika kelas pengecualian dikirimkan, itu akan secara implisit diinstansiasi dengan memanggil pembangunnya constructor tanpa argumen:
```python
raise ValueError  # shorthand for 'raise ValueError()'
```
Jika Anda perlu menentukan apakah pengecualian muncul tetapi tidak bermaksud menanganinya, bentuk yang lebih sederhana dari pernyataan raise memungkinkan Anda untuk memunculkan kembali pengecualian:
```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```
# 8.5. Pengecualian yang Ditentukan Pengguna
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat tut-class untuk informasi lebih lanjut tentang kelas Python). Pengecualian biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa saja yang dapat dilakukan oleh kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan sebagai pengecualian. Saat membuat modul yang dapat menimbulkan beberapa kesalahan berbeda, praktik yang umum adalah membuat kelas dasar untuk pengecualian yang ditentukan oleh modul itu, dan mensubkelaskan kelas itu untuk membuat kelas pengecualian khusus untuk kondisi kesalahan yang berbeda:
```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```
Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan pengecualian standar.
# 8.6. Mendefinisikan Tindakan Pembersihan
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Sebagai contoh:
```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Jika ada klausa finally, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk try selesai. Klausa untuk finally dapat berjalan bai atau tidak apabila pernyataan try menghasilkan suatu pengecualian. Poin-poin berikut membahas kasus yang lebih kompleks saat pengecualian terjadi:

- Jika pengecualian terjadi selama eksekusi klausa untuk :keyword: !try, maka pengecualian tersebut dapat ditangani oleh klausa except. Jika pengecualian tidak ditangani oleh klausa :keyword: !except, maka pengecualian dimunculkan kembali setelah klausa finally dieksekusi.

- Pengecualian dapat terjadi selama pelaksanaan klausa except atau else. Sekali lagi, pengecualian akan muncul kembali setelah klausa finally telah dieksekusi.

- Jika pernyataan klausa untuk try mencapai klausa break, continue atau :keyword:` return` maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.

- Jika klausa untuk :keyword:!finally` telah menyertakan pernyataan return, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan nilai dari try pernayataan untuk return.
# 8.7. Tindakan Pembersihan yang Sudah Ditentukan
Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka berkas dan mencetak isinya ke layar.
```python
for line in open("myfile.txt"):
    print(line, end="")
```
Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan with memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
