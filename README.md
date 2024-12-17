# DeepLearning_QnA_Sejarah_Indonesia
Project Deep Learning "Question and Answering Sejarah Indonesia Menggunakan BERT dan DistilBERT Multilingual"

Project ini bertujuan untuk membantu siswa memperoleh informasi spesifik secara cepat dan akurat terkait topik sejarah Indonesia. Dataset yang digunakan mencakup 2.436 pasangan pertanyaan, konteks, dan jawaban, yang diolah melalui proses preprocessing data seperti lowering, mengubah format menjadi JSON, dan tokenisasi.

Penelitian ini menggunakan pembagian dataset 70% untuk training, 15% untuk validation, dan 15% untuk test. Model dilatih dan dievaluasi menggunakan metrik Exact Match (EM) dan F1-Score, menghasilkan performa model sebagai berikut:

| Model                   | EM     | F1-Score |
|-------------------------|--------|----------|
| BERT Multilingual        | 57.26% | 83.39%   |
| DistilBERT Multilingual  | 53.15% | 81.57%   |

API berbasis FastAPI dikembangkan untuk memfasilitasi penggunaan model dalam skenario nyata. Hasil evaluasi menunjukkan bahwa BERT lebih unggul dalam akurasi, sedangkan DistilBERT lebih efisien dalam penggunaan sumber daya.

Penelitian ini memberikan kontribusi pada pengembangan sistem QA berbasis sejarah Indonesia dengan mendukung aksesibilitas informasi secara efektif.

## Cara Menjalankan API

Untuk menjalankan API ini, ikuti langkah-langkah berikut:

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/gekarii07/DeepLearning_QnA_Sejarah_Indonesia

