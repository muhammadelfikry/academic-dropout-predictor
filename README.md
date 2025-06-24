# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

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

Untuk mengunduh seluruh berkas dalam proyek ini, jalankan perintah git pull berikut dan pastikan anda sudah memiliki git:
```bash
git pull https://github.com/muhammadelfikry/academic-dropout-predictor.git
```

Jalankan kode berikut untuk melakukan installasi library yang dibutuhkan untuk menjalankan proyek ini.

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
Sistem prediksi dropout dideploy sebagai aplikasi web interaktif berbasis Streamlit. Aplikasi ini menyediakan dua form input utama:

1. Student Academic Information
2. Student Administrative Data

Setelah kedua form diisi, pengguna dapat menekan tombol prediksi untuk mengetahui apakah mahasiswa tersebut termasuk dalam kategori berisiko dropout atau tidak. Hasil prediksi ditampilkan secara langsung di halaman, beserta probabilitasnya.

Untuk menjalankan sistem ini, arahkan terminal ke folder proyek dan eksekusi perintah berikut:

```bash
streamlit run app.py
```

Selanjutnya, buka browser dan masukkan tautan berikut untuk mengakses aplikasi sistem machine learning ini:

```bash
http://localhost:8501
```

**Streamlit**

![image](https://github.com/user-attachments/assets/a5d1f579-2b5f-44ae-898c-314a6e720e4c)

Prototipe dari sistem machine learning ini juga dapat diakses langsung melalui Streamlit pada tautan berikut:

[Jaya Jaya Institut: Academic Dropout Predictor](https://academic-dropout-predictor.streamlit.app)

## Conclusion
Proyek ini telah menghasilkan sistem machine learning berbasis Logistic Regression yang mampu memprediksi kemungkinan dropout mahasiswa. 
Sistem ini telah diintegrasikan ke dalam prototipe aplikasi Streamlit yang ramah pengguna, serta dilengkapi dengan visualisasi dashboard Tableau yang memberikan pemahaman menyeluruh tentang variabel yang mempengaruhi dropout.

Dengan adanya sistem ini, pihak Jaya Jaya Institut dapat melakukan intervensi lebih awal dan menyusun strategi untuk menekan angka dropout secara signifikan.

### Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang dapat digunakan guna mencapai target spesifik:
- Arahkan kursor ke grafik Course Dropout, kemudian pilih salah satu course untuk memfilter tampilan data berdasarkan course tersebut.
- Pada grafik Students Status, tersedia dropdown filter yang dapat digunakan untuk memfilter data berdasarkan status kepemilikan hutang mahasiswa.
