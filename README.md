# Question and Answering Sejarah Indonesia Menggunakan BERT dan DistilBERT Multilingual
Project ini bertujuan untuk membantu siswa memperoleh informasi spesifik secara cepat dan akurat terkait topik sejarah Indonesia. Dataset yang digunakan mencakup 2.436 pasangan pertanyaan, konteks, dan jawaban, yang diolah melalui proses preprocessing data seperti lowering, mengubah format menjadi JSON, dan tokenisasi.

Penelitian ini menggunakan pembagian dataset 70% untuk training, 15% untuk validation, dan 15% untuk test. Model dilatih dan dievaluasi menggunakan metrik Exact Match (EM) dan F1-Score, menghasilkan performa model sebagai berikut:

| Model                   | EM     | F1-Score |
|-------------------------|--------|----------|
| BERT Multilingual        | 57.26% | 83.39%   |
| DistilBERT Multilingual  | 53.15% | 81.57%   |

Berdasarkan hasil evaluasi, BERT Multilingual merupakan model yang lebih baik dibandingkan DistilBERT Multilingual dalam memberikan jawaban yang akurat berdasarkan evaluasi. BERT Multilingual menunjukkan kinerja yang lebih baik pada test set, yang lebih menggambarkan bagaimana model akan berperforma pada data nyata. Sistem ini diimplementasikan melalui API yang mendukung integrasi dengan berbagai aplikasi, sehingga meningkatkan aksesibilitas informasi sejarah secara cepat dan relevan. Hasil akhir project ini berupa API berbasis FastAPI yang dikembangkan untuk memfasilitasi penggunaan model dalam skenario nyata.

## Cara Menjalankan API

Untuk menjalankan API ini, ikuti langkah-langkah berikut:

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/gekarii07/DeepLearning_QnA_Sejarah_Indonesia
2. **Arahkan ke direktori api:**
   ```bash
   cd DeepLearning_QnA_Sejarah_Indonesia/api
3. **Install dependencies dengan pip:**
   ```bash
   pip install -r requirements.txt
4. **Jalankan API dengan uvicorn:**
   ```bash
   uvicorn api:app --reload

## Hasil Fine Tuning Model 
1. BERT Multilingual: https://huggingface.co/gekkarii07/qna-sejarah-indonesia-bert-multilingual
2. DistilBERT Multilingual: https://huggingface.co/gekkarii07/qna-sejarah-indonesia-distilbert-multilingual

## Kontributor
1. Gusti Ayu Wahyu Whurapsari
2. Luh Putu Ary Purwanthi
3. Ni Putu Jenifer Putri Ariadi

