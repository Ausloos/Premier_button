import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication, QLabel,
    QVBoxLayout, QWidget, QHBoxLayout)

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Say my name")
        self.button1 = QPushButton("Clic")
        self.button2 = QPushButton("Clear")
        self.label = QLabel("")
        # Create layout and add widgets
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.button1)
        layoutH.addWidget(self.button2)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addLayout(layoutH)
        layout.addWidget(self.label)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button1.clicked.connect(self.copie)
        self.button2.clicked.connect(self.effacer)
        #on peut utiliser la fonction clear de python
        #self.button2.clicked.connect(self.label.clear)
        # jamais de parenthèse aux fonctions dans un Connect

    def copie(self):
        self.label.setText(self.edit.text());

    def effacer(self):
        self.label.setText("");

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())