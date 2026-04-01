import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from widget.main_window import MainWindow
from widget.theme.icon import RATBERT

def _set_taskbar_icon(app: QApplication) -> None:
    """Set the taskbar icon for the application."""
    # Windows
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("cz.ratbert.app")
    # macOS
    elif sys.platform == "darwin":
        app.setDesktopFileName("Ratbert")
    # Linux
    else:
        app.setApplicationName("ratbert.desktop")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _set_taskbar_icon(app)
    app.setWindowIcon(QIcon(RATBERT))
    
    window = MainWindow()
    window.setWindowTitle("Ratbert")
    window.show()

    sys.exit(app.exec())
    