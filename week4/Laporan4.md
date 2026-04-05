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

<div align="justify">Hal yang terjadi seperti diatas harusnya terdapat beberapa yang menjadi problem misalnya adalah server bisa jadi tidak merespon </div>




