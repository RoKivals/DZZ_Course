import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
#from PIL.ImageQt import QPixmap


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("dzz.ui", self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'aboba files (*.jpg, *.png *.raw)')
        print(fname)
        self.filename.setText(fname[0])
        qimg = QPixmap(fname[0])
        self.rezult.setPixmap(qimg)


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(800)
    widget.setFixedHeight(700)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
