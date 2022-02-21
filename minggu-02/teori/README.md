Pengendali Aliran Program

 Program Flow Controller Untuk jenis pengontrol loop ini, mungkin berbeda di setiap bahasa pemrograman. Hal ini berkaitan langsung dengan aturan  bahasa pemrograman itu sendiri. Aturan-aturan ini umumnya disebut sintaks. Jadi karena setiap bahasa pemrograman berbeda,  saya akan memilih bahasa pemrograman Python sebagai contoh, Sekarang di Python, ada 3 jenis pengontrol loop. 3 jenis itu adalah:1.Break statement. 2.Pass statement. 3.Continue statement.Jadi kita bisa menggunakannya untuk memutus loop ketika ada kondisi di mana kita ingin memutusnya. 
 
 for i in range(20): // digunakan untuk membuat loop yang berulang 20 kali. if i == 10 : // ok ini digunakan untuk mengecek apakah nilai i = 10 atau tidak. print("angka telah melebihi nilai 9") // ini untuk mencetak peringatan. yaitu "angka telah melebihi nilai 9" break // digunakan untuk memutus loop. print(i) // untuk mencetak  perubahan nilai i. 
 
 Lanjutkan Pernyataan Sekarang ini digunakan untuk mengulang perulangan.. yaitu program  di bawah pernyataan tidak akan dieksekusi. Atau kita bisa mengatakan untuk melewatkan perintah di bawah ini. 
 
 for i in the range (10): // ini adalah loop yang akan berulang  10 kali. if i == 5: // kode ini digunakan untuk memilih nilai i apakah  5 atau tidak. Jika benar,  program yang mendasarinya akan dieksekusi.Hanya menonjol. print("nomor 5 tidak tercetak karena ada pernyataan continue") // digunakan untuk mencetak kata-kata yang berada  dalam kurung. Continue // sekarang kode ini digunakan untuk melanjutkan sebuah loop. Dan dalam kondisi ini, saya akan mengaktifkan pernyataan ini ketika i adalah 5. print(i) // kode ini digunakan untuk menampilkan setiap perubahan yang terjadi pada nilai i. 
 
 Instruksi lulus. Pada kenyataannya, instruksi ini tidak memiliki fungsi yang sangat penting dan juga sangat sedikit digunakan oleh programmer.Jadi pass ini sebenarnya hanya mengisi kekosongan saja.Agar program tidak eror nantinya. 
 
 Penggunaan else pada perulangan.Nah yang terakhir adalah penggunaan else dalam sebuah perulangan.Nah penggunaan else dalam sebuah perulangan, akan bekerja jika kondisi statement di dalam sebuah perulangan akan bernilai fales. 
 
 a = 1 //pendeklarasian variabel a dengan nilai 0 while a == 0 : //perulangan yang menanyakan apakah nilai a itu 0 ? jika iya maka akan mencetak “perulangan”.Namun jika nilai a bukan 0, maka akan dilanjutkan ke ‘else’ print(“perulangan”) //digunakan menampilka “perulangan” else : //statement yang akan otomatis aktif dan mengerjakan program yang menjadi bagian darinya apabila perulangan tidak dijalankan.Entah kondisi dalam loop tidak lagi terpenuhi. print("else") // digunakan untuk menampilkan teks "else".
