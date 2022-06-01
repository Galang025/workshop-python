# Pandas
## Instruksi instalasi
Langkah selanjutnya menyediakan cara termudah dan direkomendasikan untuk mengatur lingkungan Anda agar menggunakan panda. Opsi instalasi lainnya dapat ditemukan di halaman instalasi lanjutan.

1. Unduh Anaconda untuk sistem operasi Anda dan versi Python terbaru, jalankan penginstal, dan ikuti langkah-langkahnya. Harap dicatat :

   - Tidak diperlukan untuk menginstal Anaconda sebagai root atau administrator.

   - Ketika ditanya apakah Anda ingin menginisialisasi Anaconda3, jawab ya.

   - Restart terminal setelah menyelesaikan instalasi.

2. Di prompt Anaconda (atau terminal di Linux atau MacOS), mulai JupyterLab:

    ```
    jupyterlab
    ```

3. Di JupyterLab, buat notebook baru (Python 3):

4. Di cell pertama pada notebook, Anda bisa mengimpor pandas dan memeriksa versinya dengan:

    ```
    import pandas
    pandas.__version__
    ```

5. Sekarang Anda siap menggunakan pandas, dan Anda dapat menulis kode Anda.
    
    Membuat DataFrame dengan  meneruskan array NumPy, dengan indeks datetime dan kolom berlabel:
    ```
    dates = pd.date_range("20130101", periods=6)
    dates
    ```

    ```
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    df
    ```

    Membuat DataFrame dengan meneruskan kamus objek yang dapat dikonversi menjadi struktur seperti series:
    ```
    pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
        }
    )
    ```

    Berikut adalah cara melihat baris atas:
    ```
    df.head()
    ```

    Untuk melihat frame baris bawah
    ```
    df.tail()
    ```

    Menampilkan indeks
    ```
    df.index
    ```
    [Link Kode](../src/praktik13.ipynb)