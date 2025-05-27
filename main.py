import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)


# Window
window = QWidget()
window.setWindowTitle("Youtube Converter")
window.resize(600,400)

layout = QVBoxLayout()
layout.setAlignment(Qt.AlignTop)

window.setLayout(layout)
window.show()

#Title
label_layout = QHBoxLayout()

label = QLabel("ConvLoad")
label.setStyleSheet("font-size: 20px; font-weight: bold;")
label_layout.addWidget(label)

dev_label = QLabel("developer build v0.1")
dev_label.setStyleSheet("font-size: 12px; color: grey;")
dev_label.setAlignment(Qt.AlignRight)
label_layout.addWidget(dev_label)

layout.addLayout(label_layout)

line = QFrame()
line.setFrameShape(QFrame.HLine)
line.setFrameShadow(QFrame.Sunken)
layout.addWidget(line)


sys.exit(app.exec_())