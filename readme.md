# 🌍 Wordy Çeviri Programı

Bu uygulama, Meta'nın NLLB (No Language Left Behind) modelini kullanarak masaüstünde çalışan bir çeviri programıdır.

Arayüz PySide6 ile tasarlanmış olup internet bağlantısıyla ilk çalıştırmada gerekli çeviri modeli indirilir.

| Desteklenen Platform | İndir |
|----------------------|-------|
| Windows 10 ve üzeri için .exe uzantılı | [İndir](https://www.mediafire.com/file/fjj9bwliavgnhgy/Wordy-translate.zip/file) |


---

## 🚀 Özellikler

- Otomatik kaynak dil algılama
- Hedef dili seçme
- Modern koyu tema
- Yazmayı bıraktıktan sonra otomatik çeviri
- Hafif .exe dosyası (model dosyası ayrı indiriliyor)

---

## 💻 Kurulum ve Çalıştırma

İndirdiğiniz zip dosya yapısında şunlar olmalı:

app.exe, uninstall.bat, BENI OKU.txt

!!!!!!! İNDİRDİĞİNİZ DOSYADA BUNLAR YOKSA AÇMAYIN !!!!!!!!
!!!!!!! İLK ÇALIŞTIĞINDA 4 GB MODEL DOSYASI İNDİRECEKTİR !!!!!!!!

### Çalıştırmak için:

1. `app.exe` dosyasına çift tıklayın.
2. Program ilk çalıştırmada gerekli çeviri modelini internetten indirir (Yaklaşık 4GB yer kaplayacaktır).
3. Model dosyaları şuraya kaydedilir:

C:\Users\KULLANICI_ADI\\.cache\huggingface\hub\

---

## ❌ Programı Kaldırmak (Uninstall)

Model dosyası yaklaşık 4 GB yer kaplayabilir.

Programı tamamen kaldırmak ve model dosyalarını silmek için:

1. `uninstall.bat` dosyasına çift tıklayın.

2. Model dosyası otomatik olarak silinecektir.

3. Daha sonra `app.exe` dosyasını manuel olarak silebilirsiniz.

---

## 🛠️ Gereksinimler

- Windows 10 veya üstü
- Python kurulumu gerekmez (.exe hazır)
- İlk çalıştırma için internet bağlantısı (sonraki kullanımlar için offline çalıştırabilirsiniz.)

---

## Lisans

Model dosyasında Meta'nın MIT Lisanslı NLLB Modeli bulunduğu için ticari amaçla kullanımından doğacak herhangi bir sorumluluğum bulunmamaktadır.
