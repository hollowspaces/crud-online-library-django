# project-daa UAS by Sri Puji Astuti
Created on Linux Ubuntu 2020. Using python 3.8.2, Django 3.0.8

Online Library named GhouLibrary. 
Feature: add, manage, dan read literature.

Project download link: https://github.com/hollowspaces/project-daa

Guide to run the project
1. Pastikan komputer sudah terhubung dengan internet dan juga sudah terinstall python versi 3.8.2 / 3.8.3, jika belum silakan download terlebih dahulu.
-	Bagi pengguna Linux dapat mendownload via terminal dengan perintah "sudo apt install python3"
-	Untuk pengguna windows dapat mengunduh di situs https://www.python.org/downloads/windows/ dan memilih versi terbaru 3.8.3, atau dapat juga mengunduh python melalui Microsoft Store.
Ketika menginstall python di Windows dengan installer berjenis executable file, checklist bagian Add Python to PATH agar mempermudah pembuatan virtual environment.

2. Kemudian buat folder baru pada direktori C:/ di Windows atau home/ pada Linux. Misalnya folder dengan nama "Dev"

3. Ekstrak project-daa-master ke folder Dev yang sudah dibuat sebelumnya.

4. Jalankan terminal/cmd. Pada Windows, direktori default di cmd yakni folder Users, sehingga tampilannya adalah C:\Users\NamaUser\>. Maka kita harus pindah ke direktori C: gunakan perintah "cd.." sebanyak 2 kali hingga masuk ke direktori C:\>

5. Masuk ke folder project-daa-master dengan perintah "cd". Contoh: "cd Dev/project-daa-master"

6. Buat virtual environment dengan perintah, "python -m venv env", jika tidak bisa coba dengan perintah "python3 -m venv env"

7. Aktifkan virtual environment yang sudah dibuat.
-	Di Linux menggunakan perintah "source env/bin/activate"
-	Di Windows menggunakan perintah "env\Scripts\activate.bat"

8. Cek versi package pip menggunakan perintah "pip list". Upgrade pip jika masih menggunakan versi lama.
-	Di Linux menggunakan perintah "pip install --upgrade pip"
-	Di Windows menggunakan perintah "python -m pip install --upgrade pip"

9. Pastikan lagi versi pip sudah upgrade, cek dengan perintah "pip list".

10. Install Django versi 3.0.8 dengan perintah "pip install Django==3.0.8"

11. Setelah selesai install, masuk ke folder C:\Dev\project-daa-master\django-project>, dengan perintah "cd django-project"

12. Jalankan server agar dapat membuka website.
-	Di Linux menggunakan perintah "python manage.py runserver"
-	Di Windows menggunakan perintah "manage.py runserver"

NOTE : Jika pada percobaan pertama runserver gagal, maka quit server dengan mengetik CTRL-C di terminal/cmd, kemudian lakukan perintah runserver kembali.

13. Jalankan browser Chrome pada komputer.
14. Ketikkan alamat default server Django pada browser, yaitu: "http://127.0.0.1:8000/" atau "localhost:8000"
15. Tunggu hingga tampilan web muncul.
