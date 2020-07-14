# project-daa by Puji
Created on Linux Ubuntu 2020. Using python 3.8.2, Django 3.0.8

Online Library named GhouLibrary. 
Feature: add, manage, dan read literature.

Guide to run the project
1. Pastikan komputer sudah terhubung dengan internet dan juga sudah terinstall python versi 3.8.2 / 3.8.3, jika belum silakan download terlebih dahulu.
-	Bagi pengguna Linux dapat mendownload via terminal dengan perintah "sudo apt install python3"
-	Untuk pengguna windows dapat mengunduh di situs https://www.python.org/downloads/windows/ dan memilih versi terbaru 3.8.3, atau dapat juga mengunduh python melalui Microsoft Store.
Note: Ketika menginstall python via executable file, checklist bagian Add Python to PATH agar mempermudah pembuatan virtual environment.

2. Kemudian buat folder baru untuk mempermudah pembuatan environment. Misalnya buat folder dengan nama "Dev" pada direktori C:/ di Windows atau home/ pada Linux

3. Ekstrak project-daa-master ke folder Dev yang sudah dibuat sebelumnya.

4. Jalankan terminal/cmd. Pada Windows, biasanya direktori default di cmd yakni folder Users, sehingga tampilannya adalah C:/Users/NamaUser>. Untuk pindah ke direktori C:/ gunakan perintah "cd.." sebanyak 2 kali hingga masuk ke direktori C:/
Masuk ke folder project-daa-master dengan perintah "cd". Contoh: "cd Dev/project-daa-master"

5. Cek versi package pip menggunakan perintah "pip list". Upgrade pip jika masih menggunakan versi lama.
-	Di Linux menggunakan perintah "pip install --upgrade pip"
-	Di Windows menggunakan perintah "python -m pip install --upgrade pip"

6. Pastikan lagi versi pip sudah upgrade, cek dengan perintah "pip list".

7. Buat virtual environment dengan perintah, "python -m venv env"

8. Aktifkan virtual environment yang sudah dibuat.
-	Di Linux menggunakan perintah "source env/bin/activate"
-	Di Windows menggunakan perintah "env\Scripts\activate.bat"

9. Ketika sudah masuk ke dalam virtual environment dan jika ada package pip yang sebelumnya terinstall, maka akan hilang, dan pip menjadi default. Selanjutnya upgrade kembali pip seperti step nomor 5.

10. Install Django versi 3.0.8 dengan perintah "pip install Django==3.0.8"

11. Setelah selesai, masuk ke folder django-project dengan perintah "cd django-project"

12. Jalankan server agar dapat membuka website.
-	Di Linux menggunakan perintah "python manage.py runserver"
-	Di Windows menggunakan perintah "manage.py runserver"

13. Jalankan browser Chrome pada komputer.
14. Ketik alamat default server Django, yaitu: "http://127.0.0.1:8000/" atau "localhost:8000"
