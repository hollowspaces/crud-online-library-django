# project-daa by Puji
Created on Linux Ubuntu 2020. Using python 3.8.2, Django 3.0.8

Online Library named GhouLibrary. 
Feature: add, manage, dan read literature.

Guide to run the project
1. Pastikan komputer sudah terhubung dengan internet dan juga sudah terinstall python versi 3.8.2 / 3.8.3, jika belum silakan download terlebih dahulu.
-	Bagi pengguna Linux dapat mendownload via terminal dengan perintah sudo apt install python3
-	Untuk pengguna windows dapat mengunduh di situs https://www.python.org/downloads/windows/ dan memilih versi terbaru 3.8.3, atau dapat juga mengunduh python melalui Microsoft Store.
Note: Ketika menginstall python via executable file, checklist Add Python to PATH agar mempermudah pembuatan virtual environment.
2. Kemudian buat folder baru untuk mempermudah pembuatan environment. Misalnya buat folder dengan nama Dev di direktori C: pada Windows atau home pada Linux.
3. Ekstrak project-daa-master ke folder Dev yang sudah dibuat sebelumnya.
4. Jalankan terminal/cmd, kemudian masuk ke folder project-daa-master dengan perintah cd. Contoh: cd Dev/project-daa-master
5. Cek versi package pip dengan menggunakan perintah pip list. Upgrade pip jika masih menggunakan versi lama.
-	Bagi pengguna Linux menggunakan perintah pip install --upgrade pip
-	Bagi pengguna Windows menggunakan perintah python -m pip install --upgrade pip
6. Kemudian pastikan lagi versi pip sudah upgrade, kita dapat cek dengan perintah pip list. Kita juga dapat melihat package apa saja yang terinstall.
7. Buat virtual environment dengan perintah, python -m venv env
8. Aktifkan virtual environment yang sudah dibuat
-	Bagi pengguna Linux menggunakan perintah source env/bin/activate
-	Bagi pengguna Windows menggunakan perintah env\Scripts\activate.bat
9. Ketika kita sudah masuk ke dalam virtual environment dan jika ada package pip yang sebelumnya terinstall, maka akan hilang dan pip menjadi default. Selanjutnya upgrade kembali pip seperti step nomor 5.
10. Install Django versi 3.0.8 dengan perintah pip install Django==3.0.8
11. Setelah selesai, masuk ke folder django-project dengan mengetikkan perintah cd django-project
12. Jalankan server agar dapat membuka website.
-	Bagi pengguna Linux menggunakan perintah python manage.py runserver
-	Bagi pengguna Windows menggunakan perintah manage.py runserver
13. Jalankan browser Chrome pada computer, dan ketik alamat IP default server Django, yaitu: http://127.0.0.1:8000/ atau localhost:8000.

