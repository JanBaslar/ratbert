from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QFont, QPixmap

from .theme.icon import RATBERT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(400, 400)

        pixLabel = QLabel()
        pixmap = QPixmap(RATBERT)
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixLabel.setPixmap(pixmap)
        pixLabel.setFixedSize(200, 200)

        label = QLabel("RATBERT")
        label.setAlignment(Qt.AlignHCenter)

        font = QFont()
        font.setPointSize(24)
        label.setFont(font)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(pixLabel, alignment=Qt.AlignHCenter)
        layout.addWidget(label, alignment=Qt.AlignHCenter)
        layout.addStretch()

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)