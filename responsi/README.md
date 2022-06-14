# Responsi

1. Membaca file csv langsung dengan menggunakan link
    ```py
    import pandas as pd

    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
    df = pd.read_csv(url)
    ```

2. menampilkan data
    ```py
    df.head() #pada tutup kurung bisa dimasukan nilai sesuai yang diinginkan
    ```
3. untuk mengecek index data
    ```py
    df.index
    ```
4. untuk mendescribekan data
    ```py
    df.describe
    ```
5. untuk transposing data
    ```py
    df.T
    ```
