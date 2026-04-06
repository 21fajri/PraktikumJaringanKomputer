# Laporan Jaringan Komputer Informatika Week 4

## DNS
<div align="justify">Domain name system itu berguna untuk mentranslasikan nama host ke bentuk alamat IP. Jadi pada praktikum minggu ini hanya menggunakan client untuk mengirimkan permintaan ke server DNS lokal dan menerima respons balik.</div>

### A. Nslookup
<div align="justify">Nslookup sendiri memiliki kegunaan untuk menguji atapun mengdiagnosa infrastruktur DNS. atau secara sederhananya ini merupakan alat untuk semacam tanya jawab antara komputer kamu dengan server DNS untuk menerjemahkan nama domain menjadi alamat IP, atau sebaliknya. kegunaan lainnya biasanya seorang teknisi akan mempergunakannya seperti Mengetahui Alamat IP Situs Web dan Melakukan Reverse Lookup. berikut dibawah ini contoh praktikum yang bisa diimplementasikan.</div>
    <img src="../assets/week4/1.png" width="400" height="300">

<div align="justify">Jadi diatas merupakan contoh sederhana untuk bisa melihat alamat IP ataupun nama domain. contoh  yang digunakan adalah alamat dari website www.mit.edu sesuai dengan modul. selanjutnya akan membuat eksperimen dengan menggunakan opsi "-type=NS" dan domain "mit.edu". disini akan menyebabkan nslookup mengirimkan permintaan untuk record tipe-NS ke default server DNS lokal. berikut contoh yang bisa di implementasikan</div>
    <img src="../assets/week4/2.png" width="400" height="300">

<div align="justify">Selanjutnya kita ingin permintaan dikirim ke server DNS bitsy.mit.edu, bukan ke default server
DNS. Dengan ini, pertukaran informasi akan terjadi secara langsung antara host yang mengajukan permintaan dan bitsy.mit.edu. Dalam contoh ini, server DNS bitsy.mit.edu memberikan alamat IP dari host www.aiit.or.kr yang merupakan server web di Advanced Institute of Information Technology. Berikut contoh yang bisa dimuat.</div>
    <img src="../assets/week4/3.png" width="400" height="300">

<div align="justify">Hal yang terjadi seperti diatas harusnya terdapat beberapa yang menjadi problem misalnya adalah server bisa jadi tidak merespon ataupun konfigurasi firewall oleh sebuah instansi. jadi pada study kasus diatas tersebut kita ingin permintaan dikirim ke server DNS bitsy.mit.edu, bukan ke default server DNS. Oleh karena itu pertukaran informasi akan terjadi secara langsung antara host yang mengajukan permintaan dan bitsy.mit.edu.</div>
    <img src="../assets/week4/4.png" width="400" height="300">

<div align="justify"> Selanjutnya mencoba syntax yaitu nslookup –option1 –option2 host-to-find dns-server. dimana ini merupakan cara untun mendiagnosa ataupun mengambil informasi dari DNS. jadi strukturnyanya itu nslookup itu nama program/perintahnya sendiri, lalu –option1 –option2 merupakan argumen tambahan untuk memodifikasi hasil pencarian, selanjutnya host-to-find dimana ini merupakan domain atau alamat yang ingin dicari informasinya contohnya www.mit.edu. dan terakhir dns-server, ini bagian yang bisa bertanya ke server DNS secara spesifik.</div>

<div align="justify"> Selanjutnya masuk pada tahap pengujian mandiri. terdapat beberapa pertanyaan pada modul yang bisa di implementasikan yaitu.</div>

* **Pertanyaan**
    * 1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP server tersebut?
    * 2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
    * 3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
* **Implementasi/Jawaban**  
    * 1. Jadi IP yang bisa di dapat adalah 114.4.166.189 dimana ini merupakan lokasi fisik server Alibaba. sementara 192.168.0.1 merupakan alamat IP dari router lokal yang bertindak sebagai DNS resolver.
         
         <img src="../assets/week4/5.png" width="400" height="300">
    * 2. implementasi untuk mengetahui server DNS otoritatif untuk universitas di Eropa. salah satu contoh yang bisa di buat adalah oxford. untuk mencarinya disini menggunakan -type=ns untuk melihat server mana yang memegang otoritas. selain itu didapat salah satu contohnya adalah "ox.ac.uk nameserver = dns0.ox.ac.uk"
         
         <img src="../assets/week4/6.png" width="400" height="300">
    * 3. Karena oxford dikonfigurasi sebagai Authoritative DNS ia hanya mau menjawab pertanyaan tentang domain mereka sendiri. mereka menolak atau disebut refused karena mereka tidak mau melayani pencarian domain luar bagi pengguna publik. namun misal menggunakan domain google yaitu 8.8.8.8 ia akan memproses seperti dibawah ini. maka kita telah mendapatkan informasi mengenai server email dari Yahoo.

         <img src="../assets/week4/7.png" width="400" height="300">
        * Contoh dibawah ini milik google.

             <img src="../assets/week4/8.png" width="400" height="300">
### B. IPConfig       
<div align="justify">Masuk pada sub-bab IPConfig, IPConfig sendiri merupakan perintah dasar untuk menampilkan semua rincian konfigurasi jaringan yang sedang aktif pada komputer. biasanya kegunaannya untuk melihat IPv4 ataupun IPv6, mengecek gateway, ataupun identifikasi koneksi. berikut contoh implementasi yang bisa dibuat dengan menggunakan syntax ipconfig /all untuk melihat semua jaringan yang terhubung pada perangkat.</div>
    <img src="../assets/week4/9.png" width="400" height="300">

<div align="justify">Selain itu IPConfig berguna untuk mengelola informasi DNS yang tersimpan dalam host dan mengirimnya berupa document. berikut tahapan awal yang bisa diimplementasikan. membuat syntax ipconfig /displaydns seperti pada gambar dibawah ini.</div>
    <img src="../assets/week4/10.png" width="400" height="300">

