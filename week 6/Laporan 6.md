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
1. <div align="justify"> Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN? Nomor urut SYN adalah 1 Segmen seperti pada gambar dibawah bahwa SYN = 1 dan  ACK = 0. ini merupakan 3-way handshake</div>

    <img src="../assets/week 6/SOAL 2 - 1.png" width="400" height="300">
2. <div align="justify"> Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK? Jadi nomor urut SYNACK yaitu 213, yang berarti 23 + 1 = 24 untuk nilai acknowledgement. disini Gaia menentukan nilai karena setiap flag SYN mengonsumsi 1 nomor urut</div>

    <img src="../assets/week 6/SOAL 2 - 2.png" width="400" height="300">
3. <div align="justify">  Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATAnya. nomor urutnya adalah 199</div>

    <img src="../assets/week 6/SOAL 2 - 3.png" width="400" height="300">
4. <div align="justify"> Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time Graph). jadi nomor urut 6 segmen pertama sekisar 7865 dimana ia dihitung sesuai urutan seperti gambar dibawah ini. dan terdapat beberapa data tambahan yaitu nilai RTT dihitung dari Waktu ACK diterima - Waktu segmen terkirim sekitar 300 MS yang dimana hasilnya adalah Nilai estimasi</div>

    <img src="../assets/week 6/SOAL 4.png" width="400" height="300">
4. <div align="justify">Round Trip Time Graph</div>

    <img src="../assets/week 6/SOAL 2 - 3 - 1.png" width="400" height="300">
5. <div align="justify"> Berapa panjang setiap enam segmen TCP pertama? Jadi panjang TCP yang pertama adalah 7865 ini dihitung melalui data yang ada yaitu 1460 dan hanya 565 </div>

    <img src="../assets/week 6/SOAL 4.png" width="400" height="300">
6. <div align="justify"> Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah menghambat pengiriman? Seperti pada gambar dibawah nilai diambil dari window sebesar 5840. Jawabannya tidak karena tidak akan mempengaruhi kecepatan pengiriman.</div>

    <img src="../assets/week 6/SOAL 5.png" width="400" height="300">
7. <div align="justify"> Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di dalam file trace) untuk menjawab pertanyaan ini? Sesuai pada praktikum kemarin tidak ada segmen yang dikirimkan ulang</div>

    <img src="../assets/week 6/SOAL 7.png" width="400" height="300">
8. <div align="justify"> Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang diterima? Seperti pada gambar dibawah ini dimana misal jika nilai ack sebesar 7866 ke 9013 maka nilai yang di ACK adalah 1147 byte. disini menggunakan selisih nomor pada ACK.</div>

    <img src="../assets/week 6/SOAL 8.png" width="400" height="300">
9. <div align="justify"> Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? Jelaskan bagaimana Anda menghitung nilai ini. Seperti pada gmabar dibawah ini bahwasannya average Throughput berkisaran 170-270 kbps sesuai pada diagram yang dihasilkan.</div>

    <img src="../assets/week 6/SOAL 9.png" width="400" height="300">
### E. Congestion Control pada TCP
<div align="justify"> Disini akan melakukan implementasi pemeriksaan jumlah data yang dikirim per satuan waktu dari klien ke server. Kita akan menggunakan salah satu fitur grafik TCP Wireshark ‒Time-Sequence-Graph(Stevens)‒ untuk
memplot data. seperti gambar dibawah ini memilih segmen TCP yang dikirim klien di jendela "daftar paket yang diambil" Wireshark. Kemudian memilih menu Statistics->TCP Stream Graph-> Time-Sequence-Graph (Stevens). disini maka setiap titik mewakili segmen TCP yang dikirim, memplot nomor urut segmen dibandingkan dengan waktu pengirimannya. berikut implementasi yang bisa dimuat adalah.</div>
    <img src="../assets/week 6/SOAL 3 - 1.png" width="400" height="300">