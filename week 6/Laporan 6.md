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
<div align="justify"> Selanjutnya melakukan filter terhadap paket yang ditampilkan pada jendela Wireshark dengan
cara memasukkan ”tcp” dan nama seperti contains dan menambahkan tanda petik 2  ke dalam kolom filter yang terdapat di bagian atas. Kemudian hasil yang seharusnya ditampilkan adalah serangkaian pesan TCP dan HTTP antara komputer. Disini akan terlihat juga inisiasi ”tree-way handshake” yang berisi pesan SYN. berikut dibawah ini contoh pertanyaan - pertanyaan yang bisa di implementasikan sesuai praktikum yang diberikan yaitu.</div>

1. <div align="justify"> Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien untuk mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk membawa pesan HTTP tersebut. Jadi IP dan nomor port sumber adalah 10.218.14.174 dan port 57168</div>

    <img src="../assets/week 6/4.png" width="400" height="300">
2. <div align="justify">Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini? Jadi seperi pada gambar dibawh destinasi tujuan port IP yaitu 128.119.245.12 dan portnya adalah 80 standarisasi keamanan browser untuk HTTP.</div>

    <img src="../assets/week 6/4.png" width="400" height="300">
3. <div align="justify"> Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien Anda (sumber) untuk mentransfer ke gaia.cs.umass.edu? Jadi alamat IPnya adalah 10.217.7.77 dan port yang digunakan adalah 57168.</div>

    <img src="../assets/week 6/SOAL 3.png" width="400" height="300">
### D. Dasar TCP