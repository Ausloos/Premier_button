import sys
from PySide2.QtWidgets import (QApplication, QWidget)
from PySide2 import QtCore, QtUiTools


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("Avec_designer.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(file,self)
        file.close()

# Add button signal to greetings slot
        self.ui.dial1.valueChanged.connect(self.ui.lcd1.display)
        self.ui.dial2.valueChanged.connect(self.ui.lcd2.display)

        self.ui.dial1.valueChanged.connect(self.dial1Changed)
        self.ui.dial2.valueChanged.connect(self.dial2Changed)

        self.setLayout(self.ui.gridLayout) #pour agrandir les formes en meme temps que la fenetre

    def dial1Changed(self):
        self.ui.dial2.valueChanged.disconnect(self.dial2Changed)
        self.ui.dial2.setValue((self.ui.dial1.value()*1.8)+32)
        self.ui.dial2.valueChanged.connect(self.dial2Changed)

    def dial2Changed(self):
        self.ui.dial1.valueChanged.disconnect(self.dial1Changed)
        self.ui.dial1.setValue((self.ui.dial2.value()-32)*0.555)
        self.ui.dial1.valueChanged.connect(self.dial1Changed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())