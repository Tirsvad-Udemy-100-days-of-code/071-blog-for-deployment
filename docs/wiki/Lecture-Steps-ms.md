# Langkah kuliah

🌐 [English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Melayu**

## Langkah 1: Jalankan blog yang siap secara setempat

**Apa yang kita peroleh:** Blog dari hari ke-69 dan ke-70 ialah titik permulaan. Menjalankannya dahulu membuktikan kod berfungsi sebelum apa-apa diubah, supaya masalah yang timbul kemudian diketahui berpunca daripada kerja penempatan.

![Tangkapan skrin 01-blog-home](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/01-blog-home.png)

## Langkah 2: Letakkan projek di bawah kawalan versi

**Apa yang kita peroleh:** Git merekod setiap perubahan dengan mesej. Sejarahnya boleh dibaca, dibandingkan dan dibatalkan, dan itulah yang digunakan oleh platform pengehosan untuk penempatan.

![Tangkapan skrin 02-commit-history](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/02-commit-history.png)

## Langkah 3: Pindahkan rahsia ke pemboleh ubah persekitaran

**Apa yang kita peroleh:** Kunci rahsia, alamat pangkalan data dan log masuk e-mel tidak lagi berada dalam kod sumber. `FLASK_KEY`, `DB_URI` dan `MAIL_*` dibaca daripada persekitaran, jadi kod yang sama berjalan di komputer riba dan di pelayan dan tiada rahsia masuk ke repositori. `debug` dimatikan.

![Tangkapan skrin 03-environment-variables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/03-environment-variables.png)

## Langkah 4: Jalankan aplikasi dengan gunicorn dan Procfile

**Apa yang kita peroleh:** Pelayan terbina dalam Flask hanya untuk pembangunan. Pelayan WSGI seperti gunicorn berhubung dengan dunia luar melalui HTTP dan memanggil `app` Flask. Baris `web: gunicorn main:app` dalam `Procfile` memberitahu hos arahan mana yang memulakan proses web.

![Tangkapan skrin 04-procfile-gunicorn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/04-procfile-gunicorn.png)

## Langkah 5: Tolak projek ke hos git

**Apa yang kita peroleh:** Repositori di hos git ialah satu-satunya sumber untuk membina penempatan. `.gitignore` mengelakkan persekitaran maya, fail pangkalan data dan rahsia daripada masuk.

![Tangkapan skrin 05-repository-files](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/05-repository-files.png)

## Langkah 6: Hoskan aplikasi dalam kontena (container)

**Apa yang kita peroleh:** Heroku tidak lagi mempunyai pelan percuma, jadi Docker mengambil tempatnya. `Dockerfile` membina imej dan `compose.yaml` memulakan blog bersama pangkalan datanya. Imej yang sama boleh berjalan di mana-mana mesin yang ada Docker.

![Tangkapan skrin 06-docker-compose](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/06-docker-compose.png)

## Langkah 7: Naik taraf SQLite kepada PostgreSQL

**Apa yang kita peroleh:** SQLite ialah satu fail dan boleh hilang apabila hos memindahkan sistem fail. PostgreSQL ialah pelayan pangkalan data sebenar. Kerana SQLAlchemy menyembunyikan perbezaan itu, hanya `DB_URI` yang berubah; kod kekal sama. `psycopg` ialah pemacunya.

![Tangkapan skrin 07-postgres-tables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/07-postgres-tables.png)

## Langkah 8: Beroperasi secara langsung – daftar, log masuk dan tulis catatan pertama

**Apa yang kita peroleh:** Pada pangkalan data kosong, pengguna pertama yang mendaftar menjadi pentadbir dan boleh menulis catatan. Pengguna lain boleh membaca dan memberikan komen. Halaman-halaman ini menunjukkan blog berjalan dari kontena dengan PostgreSQL.

![Tangkapan skrin 10-register-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/10-register-form.png)

![Tangkapan skrin 11-login-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/11-login-form.png)

![Tangkapan skrin 12-new-post-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/12-new-post-form.png)

![Tangkapan skrin 13-blog-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/13-blog-post.png)

![Tangkapan skrin 14-about](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/14-about.png)

## Langkah 9: Semak hasilnya dengan ujian

**Apa yang kita peroleh:** Set ujian pytest membuktikan blog, konfigurasi dan Procfile masih berfungsi selepas pemindahan. Jalankannya sebelum setiap push.

![Tangkapan skrin 09-tests](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/09-tests.png)

