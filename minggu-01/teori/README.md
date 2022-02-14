# Instalasi dan Penggunaan _Interpreter_ Python
> Pertemuan Minggu 1

## Sekilas tentang Python

Python adalah _interpreter_ bahasa pemrograman tingkat tinggi.

Mudah untuk digunakan, Bahasa pemrograman script, _fungsional_, Berorientasi Objek, serta dapat membantu programmer dalam proyek dengan skala kecil hingga besar.

Pembuatan aplikasi Desktop GUI, Website, Otomatisasi, Pengembang Game, Seorang _Data Analytics_, _Machine Learning_, AI, dan masih banyak lagi contoh kasus yang menggunakan Python sebagai solusi dari masalah tersebut.

Dalam pertemuan ini akan dibahaskan tentang tahap pertama diantaranya adalah installasi dan beberapa contoh dari penggunaan dari _interpreter_ Python.

## Installasi Python

Proses installasi python menggunakan Ubuntu

Berikut adalah langkah-langkah installasi dengan package manager:

1. Buka terminal ubuntu dan ketikan perintah berikut untuk refresh update list repository

```bash
sudo apt update
```

2. Menginstall library pendukung

```bash
sudo apt install software-properties-common
```

3. Menambahkan library secara personal, akan terdapat memunculkan konfirmasi untuk menambahkan library, tekan `[y]` dan tekan enter untuk melanjutkan

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

4. jalankan ulang perintah di bawah untuk mengrefresh update list repository yang telah di tambahkan dengan library personal

```bash
sudo apt update
```

5. Menginstal pustaka python versi 3.10 dengan perintah berikut

```bash
sudo apt install python3.10
```

> Versi python dapat di instal sesuai dengan versi yang kita inginkan tapi pada instalasi kali ini saya menginstal python 3.10

6. Mengecek versi python yang telah berhasil terinstall

```bash
python3.10 --version
```
Berikut output yang akan  ditampilkan

![Version Ubuntu](https://firebasestorage.googleapis.com/v0/b/galangbelajar.appspot.com/o/ubuntu.png?alt=media&token=f5017821-e329-4edd-b45b-2c6a4ae4418d)


## Penggunaan _Interpreter_ Python

#TODO