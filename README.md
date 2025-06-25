# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
**Jaya Jaya Institut** merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, belakangan ini institusi menghadapi tantangan serius berupa **tingginya angka dropout** mahasiswa. Tingginya tingkat dropout tidak hanya merugikan mahasiswa secara individu, tetapi juga berpotensi menurunkan kredibilitas dan citra institusi di mata masyarakat. Untuk mengatasi permasalahan ini, diperlukan sebuah sistem yang dapat melakukan deteksi dini terhadap mahasiswa yang berisiko mengalami dropout, sehingga intervensi atau bimbingan khusus dapat segera diberikan.

### Permasalahan Bisnis
- Tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikannya (dropout).
- Belum adanya sistem yang mampu melakukan deteksi dini terhadap mahasiswa berisiko dropout.
- Kebutuhan akan visualisasi data dropout mahasiswa agar pihak institusi dapat memahami pola dan tren secara menyeluruh.

### Cakupan Proyek
- Membangun sistem **machine learning** menggunakan algoritma **Logistic Regression** untuk memprediksi kemungkinan mahasiswa mengalami dropout.
- Mengembangkan **business dashboard interaktif menggunakan Tableau** untuk memvisualisasikan data mahasiswa dropout berdasarkan berbagai variabel.
- Mendeploy sistem prediksi menggunakan **Streamlit** sebagai prototipe yang dapat digunakan oleh pengguna non-teknis.

### Persiapan

**Sumber data**: [Students Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup environment**:

Untuk mengunduh seluruh berkas dalam proyek ini, gunakan perintah berikut. Pastikan Git telah terinstal di sistem:

```bash
git pull https://github.com/muhammadelfikry/academic-dropout-predictor.git
```

Setelah repositori berhasil diunduh, masuk ke direktori proyek dan buat lingkungan virtual menggunakan ```venv``` untuk menjaga kestabilan dan isolasi dependensi:

```bash
cd academic-dropout-predictor
python -m venv venv
```

Aktifkan environment sesuai dengan sistem operasi yang digunakan:

- Windows (Command Prompt):

  ```bash
  venv\Scripts\activate.bat
  ```

- macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

Install seluruh library yang diperlukan melalui file ```requirements.txt```:

```bash
pip install requirements.txt
```

## Business Dashboard
Business dashboard dibuat menggunakan Tableau untuk menyajikan visualisasi mahasiswa dropout berdasarkan berbagai variabel 
Dashboard ini bertujuan membantu pihak institusi dalam mengidentifikasi kelompok mahasiswa dengan risiko tertinggi. Dashboard ini menyajikan:
- Course Dropout
  Grafik batang ini menunjukkan jumlah mahasiswa yang dropout berdasarkan kode mata kuliah. Misalnya, mata kuliah dengan kode 9500 memiliki angka dropout tertinggi, yaitu 766 mahasiswa. Hal ini dapat menjadi acuan untuk evaluasi kurikulum atau metode pengajaran.

- Dropout by Gender
  Diagram lingkaran ini menunjukkan bahwa proporsi dropout antara pria dan wanita relatif seimbang, dengan pria sedikit lebih banyak yaitu 50,67%, dan wanita 49,33%.

- Students Status
  Diagram pie ini menampilkan status keseluruhan mahasiswa: sekitar 49,93% telah lulus, 32,12% mengalami dropout, dan 17,95% masih aktif. Angka dropout yang mencakup hampir sepertiga dari total mahasiswa menunjukkan urgensi masalah ini.

- Indebted Students by Scholarship Status
  Visualisasi ini menunjukkan bahwa mahasiswa non-penerima beasiswa memiliki jumlah utang yang lebih tinggi. Ini mengindikasikan bahwa masalah keuangan bisa menjadi salah satu penyebab utama dropout.

- Student Status by Scholarship Holder
  Grafik ini membandingkan status mahasiswa berdasarkan kepemilikan beasiswa. Terlihat bahwa mahasiswa yang menerima beasiswa memiliki angka dropout yang lebih rendah dibandingkan dengan yang tidak menerima beasiswa. Ini menguatkan temuan bahwa bantuan finansial berdampak signifikan dalam mengurangi dropout.

**Tableau**

![muhammadelfikry-dashboard](https://github.com/user-attachments/assets/293fc01d-ca71-4e83-81bf-67e22716d61a)

**Link Dashboard Tableau**:
https://public.tableau.com/views/JayaJayaInstitutStudentsDropoutDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Menjalankan Sistem Machine Learning
Sistem prediksi dropout telah dideploy sebagai aplikasi web interaktif berbasis Streamlit. Aplikasi ini dirancang untuk memudahkan pengguna dalam melakukan prediksi tanpa perlu memahami detail teknis pemodelan.

Aplikasi menyediakan dua form input utama:

1. Student Academic Information
2. Student Administrative Data

Setelah kedua form diisi, tombol "Prediksi" dapat ditekan untuk menghasilkan klasifikasi apakah mahasiswa tersebut berisiko mengalami dropout atau tidak. Hasil prediksi disajikan secara langsung di halaman, lengkap dengan nilai probabilitas yang dihitung oleh model Logistic Regression.

**Cara Menjalankan Aplikasi Secara Lokal**
1. Arahkan terminal ke direktori proyek.
2. Jalankan perintah berikut:

  ```bash
  streamlit run app.py
  ```

3. Buka browser dan akses aplikasi melalui alamat lokal berikut:

  ```bash
  http://localhost:8501
  ```

**Tampilan Streamlit**

![image](https://github.com/user-attachments/assets/a5d1f579-2b5f-44ae-898c-314a6e720e4c)

**Akses Aplikasi Online**

Prototype sistem machine learning juga tersedia secara daring melalui Streamlit Cloud pada tautan berikut:

[Jaya Jaya Institut: Academic Dropout Predictor](https://academic-dropout-predictor.streamlit.app)

## Conclusion
Proyek ini telah menghasilkan sistem machine learning berbasis Logistic Regression yang mampu memprediksi kemungkinan dropout mahasiswa. 
Sistem ini telah diintegrasikan ke dalam prototype aplikasi Streamlit yang ramah pengguna, serta dilengkapi dengan visualisasi dashboard Tableau yang memberikan pemahaman menyeluruh tentang variabel yang mempengaruhi dropout. 

Berdasarkan hasil analisis, ditemukan bahwa faktor keuangan dan status beasiswa memiliki pengaruh signifikan terhadap risiko dropout. Mahasiswa yang tidak menerima beasiswa cenderung memiliki kemungkinan lebih tinggi untuk mengalami dropout. Hal ini menunjukkan bahwa dukungan finansial seperti beasiswa memainkan peran penting dalam mencegah mahasiswa putus studi. Selain itu, ditemukan pula bahwa mahasiswa non-penerima beasiswa umumnya memiliki jumlah utang yang lebih tinggi, yang semakin memperkuat indikasi bahwa masalah keuangan merupakan salah satu penyebab utama terjadinya dropout.

Dengan adanya sistem ini, Jaya Jaya Institut dapat melakukan deteksi dini dan intervensi secara tepat sasaran terhadap mahasiswa yang berisiko tinggi, sehingga strategi pencegahan dapat dirancang secara lebih efektif guna menekan angka dropout secara signifikan.

### Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang dapat dilakukan oleh pihak Jaya Jaya Institut untuk menekan angka dropout mahasiswa:

- **Berikan intervensi finansial bagi mahasiswa tanpa beasiswa yang memiliki utang tinggi.** Berdasarkan temuan dari hasil analisis, mahasiswa tanpa beasiswa menunjukkan tingkat dropout yang lebih tinggi. Pihak institusi dapat menyediakan program bantuan seperti beasiswa internal, cicilan biaya pendidikan, atau subsidi UKT.
- **Tawarkan program pendampingan akademik atau konseling kepada mahasiswa berisiko tinggi.** Mahasiswa yang teridentifikasi dari model prediktif sebagai berisiko dropout dapat diikutkan dalam program mentoring atau bimbingan belajar yang dipersonalisasi.
- **Gunakan dashboard sebagai alat monitoring berkala.** Tim akademik dan bagian kemahasiswaan dapat menggunakan dashboard Tableau untuk memantau pola dropout berdasarkan variabel seperti course yang diambil, status beasiswa, dan status keuangan, lalu menyusun strategi per fakultas atau per angkatan.
- **Lakukan sosialisasi data dan temuan secara internal.** Sampaikan hasil visualisasi dan prediksi dropout secara berkala kepada dosen wali dan pihak manajemen agar keputusan intervensi dapat dilakukan secara proaktif, bukan reaktif. 

### Petunjuk Penggunaan Dashboard
- Gunakan grafik **Course Dropout** untuk memfilter data berdasarkan mata kuliah tertentu.
- Gunakan dropdown pada grafik **Students Status** untuk memfilter data berdasarkan kepemilikan utang mahasiswa.
