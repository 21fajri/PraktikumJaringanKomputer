# Laporan Jaringan Komputer Informatika Week 6

## TCP
<div align="justify"> TCP merupakan protokol internet atau IP Suite. jadi gambarannya itu seperti layanan kurir yang menjamin bahwa paket sampai ke tujuan dengan selamat, lengkap, dan sesuai urutan. beberapa karakteristik dari tcp sendiri yaitu Sebelum data dikirim, TCP harus memastikan ada jalur komunikasi yang terbuka antara pengirim dan penerima. Proses ini dikenal dengan sebutan Three-Way Handshake yaitu syn yang merupakan pengirim mengirimkan permintaan sinkronisasi. lalu syn-ack merupakan penerima membalas bahwa mereka siap. dan yang terakhir adalah ack dimana pengirim mengonfirmasi kembali, dan koneksi terjalin.</div>

### B. Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server
<div align="justify"> Disini untuk melakukan implementasi diperlukannya software tambahan yaitu wireshark dimana kita akan melakukan memasukkan nama file yang tersimpan di komputer (file tersebut berisi teks ASCII dari naskah Alice in
Wonderland) dan kemudian mentransfer file tersebut ke server Web dengan menggunakan metode HTTP POST. Kita menggunakan metode POST, bukan metode GET, karena kita ingin mentransfer data dalam jumlah besar dari komputer Anda ke komputer lain. berikut dibawah implementasi yang bisa diterapkan yaitu</div>

1. <div align="justify"> Membuka browser web yaitu http://gaia.cs.umass.edu/wireshark-labs/alice.txt dan mengunduh salinan ASCII dari naskah Alice in Wonderland. dan menyimpan file itu dikomputer.</div>

    <img src="../assets/week 6/1.png" width="400" height="300">
2. <div align="justify"> Selanjutnya menyimpan file seperti pada gambar diatas dan kembali pada website http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html dan melakukan proses upload data pada web tersebut untuk melakukan tracking pergerakan data melalui wireshark nantinya.</div>

    <img src="../assets/week 6/2.png" width="400" height="300">
3. <div align="justify"> Setelah selesai berikut seperti dibawah ini tampilan webnya yang menandakan proses upload telah berhasil dilakukan. dengan pesan Congratulation!</div>

    <img src="../assets/week 6/3.png" width="400" height="300">
4. <div align="justify"> Kemudian menjalankan wireshark dan memulai penangkapan paket dan menghentikan penangkapan paket setelah beberapa detik berlangsung agar proses dapat terlihat lebih mudah. berikut seperti dibawah ini implementasi yang bisa dilakukan.</div>

    <img src="../assets/week 6/4.png" width="400" height="300">
### C. Menampilkan Awal pada Captured Trace
