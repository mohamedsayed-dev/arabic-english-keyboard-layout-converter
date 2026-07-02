
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLabel
)
import sys

# جدول التحويل من عربي إلى إنجليزي
mapping = {
    "لا": "b",
    "ا": "h",
    "ل": "g",
    "ب": "f",
    "ت": "j",
    "ن": "k",
    "م": "l",
    "ي": "d",
    "س": "s",
    "ش": "a",
    "ك": ";",
    "ط": "'",
    "ئ": "z",
    "ء": "x",
    "ؤ": "c",
    "ر": "v",
    "ى": "n",
    "ة": "m",
    "و": ",",
    "ز": ".",
    "ظ": "/",
    "ض": "q",
    "ص": "w",
    "ث": "e",
    "ق": "r",
    "ف": "t",
    "غ": "y",
    "ع": "u",
    "ه": "i",
    "خ": "o",
    "ح": "p",
    "ج": "[",
    "د": "]",
    "ذ": "`",
}

# جدول التحويل العكسي
reverse_mapping = {v: k for k, v in mapping.items()}

def is_arabic(char):
    return '\u0600' <= char <= '\u06FF'

def convert_mixed_text(text):
    result = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i+2] in mapping:
            result += mapping[text[i:i+2]]
            i += 2
        elif is_arabic(text[i]):
            result += mapping.get(text[i], text[i])
            i += 1
        elif text[i] in reverse_mapping:
            result += reverse_mapping[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1
    return result

def launch_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("محوّل الحروف (عربي ⇄ إنجليزي) - PyQt5")
    layout = QVBoxLayout()

    label_input = QLabel("النص الأصلي:")
    input_text = QTextEdit()
    input_text.setStyleSheet("font-size: 16px;")

    button = QPushButton("تحويل")
    button.setStyleSheet("font-size: 16px; background-color: #4CAF50; color: white;")

    label_output = QLabel("النص بعد التحويل:")
    output_text = QTextEdit()
    output_text.setReadOnly(True)
    output_text.setStyleSheet("font-size: 16px;")

    def convert_action():
        text = input_text.toPlainText()
        converted = convert_mixed_text(text)
        output_text.setText(converted)

    button.clicked.connect(convert_action)

    layout.addWidget(label_input)
    layout.addWidget(input_text)
    layout.addWidget(button)
    layout.addWidget(label_output)
    layout.addWidget(output_text)

    window.setLayout(layout)
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_app()

