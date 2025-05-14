import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication(sys.argv)
layout = QVBoxLayout()

# Window setup
window = QWidget()
window.setWindowTitle("Youtube Converter")
window.resize(600,400)
window.setLayout(layout)
window.show()

label = QLabel("Youtube Converter")
label.setStyleSheet("font-size: 20px; font-weight: bold;")
layout.addWidget(label)





sys.exit(app.exec_())