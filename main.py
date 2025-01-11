import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import obf
import os



class ObfuscatorGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 200)
        self.setWindowTitle("python-obf-gui")



        self.inputChooserButton = QtWidgets.QPushButton("Select input file")
        self.inputLabel = QtWidgets.QTextEdit("")
        self.inputLabel.setMaximumHeight(33)
        

        self.outputLabel1 = QtWidgets.QLabel("Output filename:")
        self.outputLabel = QtWidgets.QTextEdit("obfuscated.py")
        self.outputLabel.setMaximumHeight(33)

        self.spamfileNameLabel = QtWidgets.QLabel("spamfile name:")
        self.spamfilename = QtWidgets.QTextEdit("md")
        self.spamfilename.setMaximumHeight(33)

        
        
        self.statusLabel = QtWidgets.QLabel("Status: waiting")

        self.inputfile = "none"
        self.outputfile = "none"


        self.obfuscateButton = QtWidgets.QPushButton("Obfuscate")

        self.layout = QtWidgets.QFormLayout(self)
        
        
        self.layout.addRow(self.spamfileNameLabel, self.spamfilename)
        
        self.layout.addRow(self.outputLabel1, self.outputLabel)

        self.layout.addRow(self.inputChooserButton, self.inputLabel)

        self.layout.addRow(self.obfuscateButton, self.statusLabel)
        

        self.inputChooserButton.clicked.connect(self.inputFileChooser)
        
        self.obfuscateButton.clicked.connect(self.obfuscate)


        self.show()
    @QtCore.Slot()
    def inputFileChooser(self):
        self.inputfile = QtWidgets.QFileDialog.getOpenFileName()[0]
        
        self.inputLabel.setText(self.inputfile)
    
    @QtCore.Slot()
    def outputFileChooser(self):
        self.outputfile = QtWidgets.QFileDialog.getOpenFileName()[0]
        
        self.outputLabel.setText(self.outputfile)
    
    @QtCore.Slot()
    def obfuscate(self):

        if not os.path.exists(self.inputfile):
            QtWidgets.QMessageBox.warning(self, "python-obf-gui", "You need to set a valid file path!", buttons=QtWidgets.QMessageBox.StandardButton.Ok)
            return
        
        self.statusLabel.setText("Status: " + "obfuscating")
        try:
            obf.obfuscate(self.inputfile, self.outputfile, self.spamfilename)
        except Exception as c:
            self.statusLabel.setText("Error: " + str(c))
            
            return

        self.statusLabel.setText("Status: " + "obfuscation succesful!")


 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ObfuscatorGui()


    sys.exit(app.exec())