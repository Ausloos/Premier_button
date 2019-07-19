
#BUT: faire un bouton qui affiche une line de texte quand on clique dessus.
#On va utiliser une QV Box Layout


#On crée une classe Forme. QWidget est une fenetre
#__init__est le constructeur. Si on ne lui donne pas de parent, il va creer une fenetre a part.
#Si on veut se comporter comme un QWidget, il faut appeler le constructeur de QWidget
# self.setlayout est une fonction de Qt et prend la taille maximale de la fenetre. On lui donne layout comme entrée

import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication, QLabel,
    QVBoxLayout, QWidget)

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.label = QLabel("")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        self.label.setText(self.edit.text());

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())