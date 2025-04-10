import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QComboBox, QLabel
)
from PySide6.QtCore import QTimer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langdetect import detect

# Model ve dil haritası
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

lang_map = {
    "tr": "tur_Latn",
    "en": "eng_Latn",
    "de": "deu_Latn",
    "fr": "fra_Latn",
    "ar": "arb_Arab",
    "es": "spa_Latn",
    "ru": "rus_Cyrl"
}

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wordy Çeviri Programı")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: Arial;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #555;
                border-radius: 6px;
                padding: 8px;
            }
            QComboBox {
                background-color: #3e3e3e;
                border-radius: 6px;
                padding: 4px;
            }
        """)

        # Ana layout
        layout = QVBoxLayout()

        # Giriş kutusu
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Metni yazmaya başlayın...")
        self.input_text.textChanged.connect(self.schedule_translation)
        layout.addWidget(QLabel("Çevrilecek metin:"))
        layout.addWidget(self.input_text)

        # Hedef dil seçimi
        layout.addWidget(QLabel("Hedef Dil:"))
        self.lang_select = QComboBox()
        self.lang_select.addItems(["en", "tr", "de", "fr", "ar", "es", "ru"])
        self.lang_select.setCurrentText("en")
        layout.addWidget(self.lang_select)

        # Çıktı kutusu
        layout.addWidget(QLabel("Çeviri sonucu:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

        # Timer ayarlanıyor (1000 ms = 1 saniye)
        self.translation_timer = QTimer()
        self.translation_timer.setInterval(1000)
        self.translation_timer.setSingleShot(True)
        self.translation_timer.timeout.connect(self.translate_text)

    def schedule_translation(self):
        # Her yazıda timer sıfırlanır
        self.translation_timer.start()

    def translate_text(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.clear()
            return

        try:
            src_lang_code = detect(text)
        except:
            src_lang_code = "tr"

        tgt_lang_code = self.lang_select.currentText()
        src_lang = lang_map.get(src_lang_code, "tur_Latn")
        tgt_lang = lang_map.get(tgt_lang_code, "eng_Latn")

        try:
            translator = pipeline("translation", model=model, tokenizer=tokenizer, src_lang=src_lang, tgt_lang=tgt_lang)
            result = translator(text, max_length=512)
            self.output_text.setPlainText(result[0]["translation_text"])
        except Exception as e:
            self.output_text.setPlainText(f"Hata: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())
