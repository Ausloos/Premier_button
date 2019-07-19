import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication, QLabel,
    QVBoxLayout, QWidget, QHBoxLayout, QDial, QLCDNumber)

class tempCF(QWidget):

    def __init__(self, parent=None):
        super(tempCF, self).__init__(parent)

        # Create widgets
        self.label1 = QLabel("Celsius")
        self.dial1 = QDial()
        self.lcd1 = QLCDNumber()
        self.dial1.setRange(-10, 90)

        self.label2 = QLabel("Fahrenheit")
        self.dial2 = QDial()
        self.lcd2 = QLCDNumber()
        self.dial2.setRange(14, 194)

        # Create layout and add widgets
        layoutV1 = QVBoxLayout()
        layoutV1.addWidget(self.label1)
        layoutV1.addWidget(self.dial1)
        layoutV1.addWidget(self.lcd1)

        layoutV2 = QVBoxLayout()
        layoutV2.addWidget(self.label2)
        layoutV2.addWidget(self.dial2)
        layoutV2.addWidget(self.lcd2)

        layoutPrincipale = QHBoxLayout()
        layoutPrincipale.addLayout(layoutV1)
        layoutPrincipale.addLayout(layoutV2)

        # Set dialog layout
        self.setLayout(layoutPrincipale)

        # Add button signal to greetings slot
        self.dial1.valueChanged.connect(self.lcd1.display)
        self.dial2.valueChanged.connect(self.lcd2.display)

        self.dial1.valueChanged.connect(self.dial1Changed)
        self.dial2.valueChanged.connect(self.dial2Changed)

    def dial1Changed(self):
        self.dial2.valueChanged.disconnect(self.dial2Changed)
        self.dial2.setValue((self.dial1.value()*1.8)+32)
        self.dial2.valueChanged.connect(self.dial2Changed)

    def dial2Changed(self):
        self.dial1.valueChanged.disconnect(self.dial1Changed)
        self.dial1.setValue((self.dial2.value()-32)*0.555)
        self.dial1.valueChanged.connect(self.dial1Changed)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = tempCF()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())