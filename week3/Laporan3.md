# Laporan Jaringan Komputer Informatika Week 3

## HTTP
<div align="justify">Di karenakan sebelumnya telah mempelajari atau perkenalan dengan wireshark pada praktikum di week 3 ini akan masuk pada materi HTTP. Di dalam wireshark sering kali melihat beberapa protocol yang berjalan. Tugasnya pada praktikum ini adalah mengimplementasikan atau menganalisa basic dari HTTP tentang interaksi GET/Response, pesan HTTP, dan beberapa hal yang berkaitan dengan HTML. Sebelum melanjutkan implementasi mungkin sedikit penjelasan mengenai tentang HTTP yang merupakan protocol yang berfungsi untuk tempat pertukaran data di World Wide Web atau biasa disebut dengan WWW. Di sini HTTP mengatur client dan server dalam meminta dan menerima material dari sisi server. Karakteristiknya sendiri ia mereka berjalan di atas model permintaan – respon. Setelah mengetahui definisinya masu pada tahap praktikum.</div>

### A. Basic HTTP GET
<div align="justify">Pada basic HTTP ini saat ingin mengetikkan URL browser mengirimkan permintaan GET. cara ini digunakan untuk mengambil data dari server. Server menerima permintaan dan mencari file yang diminta, lalu mengirimnya Kembali. Berikut mungkin beberapa tanggapan  atau respon dengan paket informasi yang berisi dua bagian.</div>

* **Status Code**: Angka tiga digit yang memberi tahu apakah permintaan berhasil.
    * 200: Menandakan bahwa datanya ada dan berhasil.
    * 400: Error atau datanya tidak dapat dijangkau atau tidak ditemukan.
    * 500: Biasanya pada sisi ini kesalahan pada server itu sendiri ntah karena server down karena kebanyakan permintaan atau lain sebagainya.
* **Content**: biasanya berisikan data yang diminta berupa kode HTML, gambar, atau data seperti contohnya JSON. 