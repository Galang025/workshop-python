# Akses ke basis data CockroachDB menggunakan psycopg2 dan menggunakan SQLAlchemy
## psycopg2

### Langkah pertama menginstall CockroachDB
 1. Install CockroachDB binary 
 
 ```
$ curl https://binaries.cockroachdb.com/cockroach-v21.2.10.linux-amd64.tgz | tar -xz && sudo cp -i cockroach-v21.2.10.linux-amd64/cockroach /usr/local/bin/
 ```
 2. Memasukan libarary GEOS
 - Membuat direktori untuk menyimpan library
 ```
 $ mkdir -p /usr/local/lib/cockroach
 ```
 - Masukan library kedalam direktori yang telah dibuat
 ```
 $ cp -i cockroach-v21.2.10.linux-amd64/lib/libgeos.so /usr/local/lib/cockroach/
 ```
 ```
 $ cp -i cockroach-v21.2.10.linux-amd64/lib/libgeos_c.so /usr/local/lib/cockroach/
 ```
 Jika terjadi error tinggal tambahkan sudo, berikut contoh perintahnya :
 ```
 $ sudo mkdir -p /usr/local/lib/cockroach
 ```
 3. Konfirmasi CockroachDB apakah bisa mengeksekusi spesial query
 - pastikan bahwa Cockroach binary berhasil terinstall
 ```
 $ which cockroach
 ```
 ```
 /usr/local/bin/cockroach
 ```
 - Memulai cluster untuk melakukan demo 
 ``` 
 $ cockroach demo
 ```
 - Pada cluster jalankan perintah di bawah untuk menguji apakah library telah berhasil di install
 ```
 > SELECT ST_IsValid(ST_MakePoint(1,2));
 ```
 Berikut hasil outputnya jika berhasil
 ```
 st_isvalid
--------------
true
(1 row)
```
Berikut hasil output jika library di install pada direktori yang salah
```
ERROR: st_isvalid(): geos: error during GEOS init: geos: cannot load GEOS from dir "/usr/local/lib/cockroach": failed to execute dlopen
          Failed running "sql"
```
### Langkah kedua memulai CockroachDB
1. Menjalakan Cockroach dengan menggunakan perintah
```
$  cockroach start-single-node --advertise-addr 'localhost' --insecure
```
Berikut output yang keluar jika berhasil menjalankan CockroachDB
```
CockroachDB node starting at 2022-05-10 14:14:06.164365127 +0000 UTC (took 1.1s)
build:               CCL v21.2.10 @ 2022/05/02 17:38:58 (go1.16.6)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257/defaultdb?sslmode=disable
sql (JDBC):          jdbc:postgresql://localhost:26257/defaultdb?sslmode=disable&user=root
RPC client flags:    cockroach <client cmd> --host=localhost:26257 --insecure
logs:                /home/galang/cockroach-data/logs
temp dir:            /home/galang/cockroach-data/cockroach-temp263191760
external I/O path:   /home/galang/cockroach-data/extern
store[0]:            path=/home/galang/cockroach-data
storage engine:      pebble
status:              initialized new cluster
clusterID:           aa115fa6-d58d-4152-843d-6c30493871b2
nodeID:              1
```
### Langkah ketiga mengambil sampel code 
clone sampel code yang terdapat pada Github repo :
```
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```
### langkah keempat menginstall psycopg2 driver
```
$ pip install psycopg2-binary
```
### langkah kelima menjalankan kode
1. jalakan perintah berikut untuk mengatur koneksi dengan CockroachDB cloud cluster
```
$ export DATABASE_URL="postgresql://root@localhost:26257/defaultdb?sslmode=disable"
```
> Catatan gunakan koneksi db yang terdapat pada komputer anda

Jalankan perintah berikut
```
$ cd hello-world-python-psycopg2
```
```
$ python example.py
```
Berikut outputnya
```bash
galang@Aether:~/hello-world-python-psycopg2$ python3 example.py
Balances at Tue May 10 21:57:28 2022:
(1, 1000)
(2, 250)
Balances at Tue May 10 21:57:28 2022:
(1, 900)
(2, 350)
```
## SQLAlchemy
### Langkah pertama dapatkan code
Clone code yang terdapat pada github 
```
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
### Langkah kedua install virtualenv
1. Jalankan perintah berikut
```
$ pip install virtualenv
```
2. Buat dan jalankan virtual envirotment
```
$ virtualenv env
```
```
$ source env/bin/activate
3. Install moduls
```
```
$ pip install -r requirements.txt
```
### Langkah ketiga inisialisai database
1. Jalakan perintah berikut untuk mengatur koneksi cluster
```
export DATABASE_URL="{connection-string}"
```
2. Untuk inisialisasi sampel database menggunakan Cockroach sql
```
$ cat dbinit.sql | cockroach sql --url $DATABASE_URL
```
Berikut outputnya
```
CREATE TABLE

Time: 19ms
```
### Langkah keempat menjalankan code
1. Jalankan perintah berikut
```
$ python main.py
```
Berikut hasil outputnya
```bash
(env) galang@Aether:~/example-app-python-sqlalchemy$ python main.py
Creating new accounts...
Created new account with id 805240c1-241d-41dc-85a6-b7fe1109bb79 and balance 849964.
Created new account with id 8012c16d-d551-4557-8ba1-007d54ea0036 and balance 38461.
Created new account with id ed827cf9-b45a-4c3b-9141-84a0d7eb54b4 and balance 939731.
Created new account with id d9ff4bd3-4d44-407b-aade-57d0052cf41d and balance 172378.
Created new account with id aa33b487-3b90-408f-bc08-ecdbb9c40cb3 and balance 569115.
Created new account with id fe781250-1bb7-47fa-bf43-aed64a3a8b59 and balance 335594.
Created new account with id 824f61e9-2421-4a6b-864e-0deacc6ade3e and balance 163496.
Created new account with id 6f1cfb30-b691-47a4-9daa-bd71baccaac3 and balance 952238.
Created new account with id 4e95af9d-ce0d-4f4f-b67d-5e45b98cb365 and balance 718966.
Created new account with id 07da7733-d133-4881-80cc-e35c576fe7dd and balance 917063.
Created new account with id 49356d15-0075-46d4-b9b0-83cb58eaacbe and balance 664961.
Created new account with id 0aad1174-a541-473b-8b74-a267fcafc8f2 and balance 552043.
Created new account with id 5527f6aa-a8e0-49c3-aeae-fdd04985196c and balance 611384.
Created new account with id a4553ccc-991e-4ce5-a6ca-efe9e5da880e and balance 965715.
Created new account with id 0d69323f-604d-4597-8613-c291a655680d and balance 793929.
Created new account with id 49c31b10-fb55-4f9e-93d6-6d9f642d6a2c and balance 954568.
Created new account with id b0ac3f8b-ee0e-4bb4-aa3b-774362e49505 and balance 224281.
Created new account with id d68346f5-2d5e-49e2-8c27-83bba9ccf4cf and balance 647342.
Created new account with id 534fe2fd-824b-4ea3-a8f8-5f7d6e8e51a3 and balance 675410.
Created new account with id 6c2d71ab-180b-4608-9045-7df461a01701 and balance 535972.
Created new account with id aed6c03b-4b4f-42d6-9c13-b7de02b528e7 and balance 817291.
Created new account with id cb2211ad-623c-444a-9273-6b7487d5e13c and balance 324682.
Created new account with id b669b31b-c991-4563-a11a-f9f0728c086b and balance 616039.
Created new account with id f46fb5e3-781a-4b9c-b6eb-cd6ed0bb3c94 and balance 551587.
Created new account with id a27bca32-cc27-4e23-8261-73486437943e and balance 485417.
Created new account with id cf8b925b-357b-465c-b8e9-b0581101e058 and balance 969032.
Created new account with id 843733ca-7990-4645-9ea5-233e53f70afb and balance 996335.
Created new account with id 02b2f1f3-8fcc-4772-aced-52146ed75da8 and balance 489843.
Created new account with id 040c3384-2276-4aec-bf80-83c8b250c396 and balance 737816.
Created new account with id a406c82f-2f3b-4ade-9a13-dba590f32589 and balance 911628.
Created new account with id 6cf53271-bbbb-4997-8060-9ae692cfe719 and balance 137792.
Created new account with id c751a04b-4b75-4585-93d8-6cd0126e190f and balance 559838.
Created new account with id fc196243-dd45-4782-ac48-e45f5318c68d and balance 697344.
Created new account with id 4d326eec-8820-4e39-980a-35ecdd2da5e5 and balance 455798.
Created new account with id 8b19913f-f9bc-4006-bf12-0948f4ba2b5a and balance 633767.
Created new account with id 110a9cde-d4d8-4e57-b366-187d9f82f9b3 and balance 201836.
Created new account with id b723abd3-b500-4924-9cc5-72bcc9d2c28d and balance 772378.
Created new account with id 18bff727-4519-4d9c-890e-628d1852a0aa and balance 642710.
Created new account with id 5440ab43-9e21-4c24-a73f-45a31ba25911 and balance 985566.
Created new account with id e8e5300b-7993-4f8c-b698-5b5f1d8dedbf and balance 374064.
Created new account with id b135c7cd-69d4-46e7-bbfc-3d3c8fcabc03 and balance 114514.
Created new account with id c7fb9426-ae32-4bc0-9776-b5454bf42879 and balance 348545.
Created new account with id 3fd32d8d-b4d0-47f8-b9e5-5d843c39cfb6 and balance 570353.
Created new account with id c7212d76-889f-4d5b-a34e-26975a8d39bf and balance 17355.
Created new account with id b61f9f16-9217-4cb2-9c0a-f1f00c5bfbc7 and balance 152439.
Created new account with id 3725a107-b846-48b5-853e-e35462320bcf and balance 513792.
Created new account with id d93e6438-671a-4a12-8795-35a81a847b0e and balance 768977.
Created new account with id 70008a99-6f61-4f9d-b2e1-1d9f0150ca59 and balance 321618.
Created new account with id 6ca28490-55d8-4ec0-be16-e08ad74f5eb3 and balance 948973.
Created new account with id 60d0df4d-8ae8-493f-8e8b-510dd8dcff68 and balance 417027.
Created new account with id ff8c67bb-e367-415f-9b95-d1b4c137d2c4 and balance 354745.
Created new account with id 72cff8c6-8309-4862-8f49-bf43ac7b902d and balance 253150.
Created new account with id ee1b4b82-cb92-4b32-a9dd-08fb12e2194e and balance 621984.
Created new account with id 0772e289-df3b-4c8c-b17d-1b39adf03fee and balance 900982.
Created new account with id 9035dc22-7bac-4979-a763-0cd537dab2a4 and balance 857875.
Created new account with id 0c23525d-d768-4793-82f8-631475d422f8 and balance 918946.
Created new account with id 18874431-3c09-4639-b226-fac0bed2c97c and balance 689803.
Created new account with id 5e748ec8-703c-4c44-8b5b-7402b29124dc and balance 339296.
Created new account with id 862c220d-b7c7-4901-a5ce-5a7f77a54c21 and balance 928343.
Created new account with id a8703492-dfdd-4422-9d1d-61fc64e0a26e and balance 779846.
Created new account with id 0c7c8de4-9635-47ce-bbdd-9123a5b8fea1 and balance 682240.
Created new account with id efcaef77-75ba-4f14-bda3-26fd2ddcad70 and balance 26968.
Created new account with id 8d44aa81-956e-4d37-b5bb-581ec731cada and balance 646485.
Created new account with id bdb8b860-3dbb-4cea-9257-e473a75aba68 and balance 184159.
Created new account with id 10dadfd9-e605-4ab2-9194-27c758f9c2b2 and balance 555727.
Created new account with id 8c3785a2-4ec3-44e9-bd0c-9af825f74ad2 and balance 258164.
Created new account with id eaa5fe38-17f8-48b7-8a4a-f38353c14089 and balance 652554.
Created new account with id 836222e5-5a61-4197-97e3-18294ce77b6e and balance 735095.
Created new account with id 908ee0f8-4ca3-468b-854f-d2a158a489d7 and balance 29053.
Created new account with id 535c4dfc-51c8-419f-bb65-adf4320f1710 and balance 571735.
Created new account with id ee55af62-f203-4e87-aa9a-5a80ff8a4f4b and balance 525149.
Created new account with id f7975a73-dd99-4450-bb43-15b24cb24cb8 and balance 886865.
Created new account with id 2c39f720-1fb6-4c92-a1c3-1a2006c833b4 and balance 523206.
Created new account with id 558329d2-4065-41a7-8b0f-8f0c478d3096 and balance 540019.
Created new account with id 7a347e3c-f39f-4cec-9807-2f559d9bbc86 and balance 518010.
Created new account with id fd9441e3-d5cd-4351-928c-0f86ccf655c1 and balance 536040.
Created new account with id b66351d4-a629-41c9-ac4e-8d6ffc153ab0 and balance 332106.
Created new account with id b93142f9-a553-4272-886f-b839f978b482 and balance 704088.
Created new account with id b5cb0b18-520f-45db-b5ec-0141575a7536 and balance 799197.
Created new account with id 7f6361a3-1891-462e-bc6c-f289f77fd4c0 and balance 991466.
Created new account with id 601f4ba7-cad7-47c6-ae6c-b191b01fe456 and balance 335073.
Created new account with id 6c55e9cb-71b5-46d9-8f29-644c6ba3e9d4 and balance 43538.
Created new account with id f74df446-9c67-4a9f-aa26-4369ab581357 and balance 192923.
Created new account with id 2e20d57a-b837-499e-931f-f3140c7d2132 and balance 214557.
Created new account with id 3f78aec5-b53e-41b3-899b-7a428b0f0ffb and balance 918274.
Created new account with id 32960614-b758-4d77-8924-1d70c17f9cf0 and balance 56111.
Created new account with id 1ff4085d-ef3f-4479-9884-1ece0f29afdf and balance 307868.
Created new account with id 57ac6278-3923-4aa6-9410-146b10ca757b and balance 626501.
Created new account with id d04dbbb1-b179-4212-b10e-fa55d93f3fd8 and balance 618857.
Created new account with id b317f058-c58e-40fc-85d0-6c60ed4f6bb9 and balance 94551.
Created new account with id c2d3b7a6-118a-4a9d-8d62-d82428b9281b and balance 634961.
Created new account with id 5f407fcd-212f-4dec-931e-889de47685a4 and balance 287292.
Created new account with id bd127a38-5c37-43ca-be42-6962be3f54c8 and balance 112253.
Created new account with id fbd70f14-39c8-4df2-9b78-d79aece12b8a and balance 800977.
Created new account with id dfa311b7-82e4-4e45-891e-43ef53175d8a and balance 842080.
Created new account with id 42341848-4692-4a9f-bd41-fb80f2be9505 and balance 249601.
Created new account with id 40ed0a6d-478d-4a7a-9976-7043dfd804b0 and balance 378935.
Created new account with id 5d064a2f-70a8-46b0-a141-5bf24403e705 and balance 758206.
Created new account with id 0a6c3c52-1d33-4906-8839-966e2a3e6694 and balance 12816.
Created new account with id fba335ee-ba3b-4719-9b2f-8e0cb09ca677 and balance 54862.
Random account balances:
Account 8c3785a2-4ec3-44e9-bd0c-9af825f74ad2: 258164
Account 0aad1174-a541-473b-8b74-a267fcafc8f2: 552043
Transferring 129082 from account 8c3785a2-4ec3-44e9-bd0c-9af825f74ad2 to account 0aad1174-a541-473b-8b74-a267fcafc8f2...
Transfer complete.
New balances:
Account 8c3785a2-4ec3-44e9-bd0c-9af825f74ad2: 129082
Account 0aad1174-a541-473b-8b74-a267fcafc8f2: 681125
Deleting existing accounts...
Deleted account 18bff727-4519-4d9c-890e-628d1852a0aa.
Deleted account 1ff4085d-ef3f-4479-9884-1ece0f29afdf.
Deleted account 5527f6aa-a8e0-49c3-aeae-fdd04985196c.
Deleted account 9035dc22-7bac-4979-a763-0cd537dab2a4.
Deleted account bd127a38-5c37-43ca-be42-6962be3f54c8.
```
Masuk ke sql cockroach lalu jalankan perintah berikut
```
SELECT COUNT(*) FROM accounts;
```
berikut outputnya
```bash
root@:26257/defaultdb> SELECT COUNT(*) FROM accounts;
  count
---------
     95
(1 row)


Time: 1ms total (execution 1ms / network 0ms)

root@:26257/defaultdb>
```