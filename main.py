import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)


        self.statusBar().showMessage("Ready")

        menubar = self.menuBar()

        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("This is a <B>QWidget</B> widget")

        btn = QPushButton("Quit", self)
        btn.setToolTip("This is a <B>QPushButton</B> widget")

        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("My First Application")
        self.setWindowIcon(QIcon("web.png"))
        # self.move(300, 300)
        #self.resize(400, 200)
        self.setGeometry(600, 300, 600, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
