import sys

from PyQt5.QtCore import QCoreApplication, QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, \
    QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        grid.addWidget(QLabel("Title:"), 0, 0)
        grid.addWidget(QLabel("Author:"), 1, 0)
        grid.addWidget(QLabel("Review:"), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        okButton.setEnabled(False)
        cancelButton.setCheckable(True)
        cancelButton.toggle()

        hbox = QHBoxLayout()
        # 여백 추가
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        title = QLabel("First Label")
        title.setAlignment(Qt.AlignVCenter)
        font1 = title.font()
        font1.setBold(True)
        font1.setPointSize(30)
        title.setFont(font1)

        lbl_red = QLabel("Red")
        lbl_green = QLabel("Green")
        lbl_blue = QLabel("Blue")

        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px"
                              )

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(lbl_red)
        layout.addWidget(lbl_green)
        layout.addWidget(lbl_blue)
        layout.addLayout(hbox)
        layout.addLayout(grid)
        # layout.addWidget(btn)

        self.setLayout(layout)
        self.setGeometry(600, 300, 600, 600)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        date = QDate.currentDate()

        self.statusBar().showMessage(date.toString(Qt.DefaultLocaleLongDate))

        menubar = self.menuBar()

        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("This is a <B>QWidget</B> widget")

        # btn = QPushButton("Quit")
        # btn.setToolTip("This is a <B>QPushButton</B> widget")
        #
        # btn.move(50, 100)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # self.move(300, 300)
        #self.resize(400, 200)

        self.setWindowTitle("My First Application")
        self.setWindowIcon(QIcon("web.png"))

        self.setCentralWidget(MyWidget())
        self.setGeometry(600, 600, 600, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
