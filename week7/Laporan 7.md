# Laporan Jaringan Komputer Informatika Week 7

## SOCKET PROGRAMMING
<div align="justify">   Typical network application itu terdiri dari sepasang program program client dan program server yang berada di dua sistem akhir yang berbeda. Ketika kedua program ini dijalankan, proses client dan proses server dibuat, dan proses ini berkomunikasi satu sama lain dengan membaca dari, dan menulis ke, soket. Saat membuat aplikasi jaringan, tugas utama developer adalah menulis kode untuk program klien dan server. Ada dua jenis network applications yaitu implementasi yang operasinya ditentukan dalam standar protokol dan proprietary network application dimana program klien dan server menggunakan protokol an application-layer yang belum dipublikasikan secara terbuka
di RFC atau di tempat lain. developer membuat program klien dan server, dan developer memiliki kendali penuh atas apa yang ada dalam kode. Tetapi karena kode tersebut tidak mengimplementasikan open protocol, developer independen lainnya tidak akan dapat mengembangkan kode yang beroperasi dengan aplikasi tersebut.</div>

### B. Program Socket dengan UDP
<div align="justify">   Melihat interaksi antara dua proses komunikasi yang menggunakan soket UDP. Sebelum proses pengiriman dapat mendorong paket data keluar dari pintu soket, saat menggunakan UDP, terlebih dahulu harus melampirkan alamat tujuan ke paket. Setelah paket melewati soket pengirim, Internet akan menggunakan alamat tujuan ini untuk merutekan paket melalui Internet ke soket dalam proses penerima. Ketika paket tiba di soket penerima, proses
penerima akan mengambil paket melalui soket, dan kemudian memeriksa isi paket dan mengambil tindakan yang tepat. 
</div>

#### C UDP-Client.py
<div align="justify">Berikut dibawah ini implementasi yang bisa dimuat untuk praktikum week 7 yaitu.</div>
    <img src="../assets/week7/2.png" width="400" height="300">

<div align="justify">Jadi alur program diatas diawali dari mengimport socket untuk kebutuhan komunikasi jaringan dan sys untuk fungsionalitas sistem. kemudian Program menetapkan identitas server melalui IP dan port dan juga membuat objek socket dengan AF_INET untuk IPv4 dan SOCK_DGRAM untuk protokol UDP. Selain itu ada juga fitur settimeout(5) untuk mencegah program macet. Selanjutnya Program masuk kedalam perulangan menggunakan while True agar user dapat mengirim pesan berulang kali. di dalam loop ini program mengambil input teks dari pengguna. Jika inputnya adalah 'exit' atau 'keluar', program akan mengirimkan pesan itu ke server terlebih dahulu, kemudian menghentikan loop dengan break untuk menutup program. Jika inputnya itu teks biasa, pesannya akan diubah menjadi format byte menggunakan encode() dan dikirimkan ke alamat server yang telah ditentukan dengan fungsi sendto. Setelah data terkirim, program masuk ke try-except internal untuk menunggu balasan dari server menggunakan recvfrom(2048). Jika server merespons, pesan yang diterima akan didekode kembali menjadi teks dan ditampilkan ke layar. tapi, jika dalam 5 detik tidak ada jawaban, program akan melakukan timeout an menampilkan pesan kesalahan tanpa menghentikan program. dan semua proses akan dijadikan satu didalam finally.</div>

#### D UDP-Server.py
<div align="justify">Berikut dibawah ini implementasi yang bisa dimuat.</div>
    <img src="../assets/week7/3.png" width="400" height="300">

<div align="justify"></div>