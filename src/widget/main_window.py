from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QIcon, QFont

from .theme.icon import RATBERT_SVG as RATBERT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(400, 400)
        
        svg_widget = QSvgWidget(RATBERT)
        svg_widget.setFixedSize(200, 200)

        label = QLabel("RATBERT")
        label.setAlignment(Qt.AlignHCenter)

        font = QFont()
        font.setPointSize(24)
        label.setFont(font)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(svg_widget, alignment=Qt.AlignHCenter)
        layout.addWidget(label, alignment=Qt.AlignHCenter)
        layout.addStretch()

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)