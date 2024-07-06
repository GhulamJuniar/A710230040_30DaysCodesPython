import sys
from PyQt5 import QtWidgets
from form import Ui_MainWindow 


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonHitung.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        try:
            harga = float(self.lineEditHarga.text())
            pajak_str = self.comboBoxPajak.currentText()
            pajak = float(pajak_str.strip('%')) / 100
            total = harga + (harga * pajak)
            self.labelHasil.setText(f"Rp {total:,.2f}")
        except ValueError:
            self.labelHasil.setText("Input tidak valid")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())
