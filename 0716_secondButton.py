import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

#Dans ce programme, le signal est "clique"

#@Slot()
#def say_hello():
 #print("Button clicked, Hello!")

@Slot()
def buttonIsPressed():
    print("button is pressed")

@Slot()
def buttonIsReleased():
    print("button is released")

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
#Quand on clique sur le bouton on va executer la fonction say_hello
#button.clicked.connect(say_hello)
button.pressed.connect(buttonIsPressed)
button.released.connect(buttonIsReleased)
button.show()
# Run the main Qt loop
app.exec_()
