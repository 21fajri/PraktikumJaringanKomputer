# Laporan Jaringan Komputer Informatika Week 7

## SOCKET PROGRAMMING MEMBUAT APLIKASI JARINGAN
<div align="justify"> Typical network application itu terdiri dari sepasang program program client dan program server yang berada di dua sistem akhir yang berbeda. Ketika kedua program ini dijalankan, proses client dan proses server dibuat, dan proses ini berkomunikasi satu sama lain dengan membaca dari, dan menulis ke, soket. Saat membuat aplikasi jaringan, tugas utama developer adalah menulis kode untuk program klien dan server. Ada dua jenis network applications yaitu implementasi yang operasinya ditentukan dalam standar protokol dan proprietary network application dimana program klien dan server menggunakan protokol an application-layer yang belum dipublikasikan secara terbuka
di RFC atau di tempat lain. developer membuat program klien dan server, dan developer memiliki kendali penuh atas apa yang ada dalam kode. Tetapi karena kode tersebut tidak mengimplementasikan open protocol, developer independen lainnya tidak akan dapat mengembangkan kode yang beroperasi dengan aplikasi tersebut.</div>

### B. Program Socket dengan UDP
<div align="justify"> Melihat interaksi antara dua proses komunikasi yang menggunakan soket UDP. Sebelum proses pengiriman dapat mendorong paket data keluar dari pintu soket, saat menggunakan UDP, terlebih dahulu harus melampirkan alamat tujuan ke paket. Setelah paket melewati soket pengirim, Internet akan menggunakan alamat tujuan ini untuk merutekan paket melalui Internet ke soket dalam proses penerima. Ketika paket tiba di soket penerima, proses
penerima akan mengambil paket melalui soket, dan kemudian memeriksa isi paket dan mengambil tindakan yang tepat. 
</div>

### C UDPClient.py
<div align="justify">Berikut dibawah ini implementasi yang bisa dimuat untuk praktikum week 7 yaitu.</div>
    <img src="../assets/week7/2.png" width="400" height="300">

<div align="justify">Jadi alur program diatas diawali dari mengimport</div>