# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
import usual_signal
import matplotlib.pyplot as plt   
import numpy as np


# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'main1.ui'))
# class MessageBox(QMessageBox):
#     def __init__(self):
#         QMessageBox.__init__(self)
#         self.setText("Add new fonction.")
#         self.setInformativeText("Coming soon !!")
#         self.setIcon(QMessageBox.Information)
#         self.setStandardButtons(QMessageBox.Close)
    
class mainApp1(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp1,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui()
        self.check()
        self.hundle_button()
        self.check_signal()
    
    def okbutton(self):
        self.OK.clicked.connect(self.check_signal())
       
    def hundle_button(self):
        self.show_fonction.clicked.connect(self.action)
    def combobox_changed(self):
        combobox = self.combo_usuel_signals
        text = combobox.currentIndex()
        print(text)
        return text
    def newindex(self):
        combobox = self.combo_usuel_signals
        combobox.currentIndexChanged.connect(self.combobox_changed)
        print("new index is ",combobox.currentIndex())
        return combobox.currentIndex()
    def check_signal(self):
        i = 5
        c = self.newindex()
        print("c = ", c)
        while i != 0 :
            
            if c == 0 :
                self.run_button.clicked.connect(usual_signal.R)
            elif c == 1 :
                self.run_button.clicked.connect(usual_signal.U)
            elif c == 2:
                self.run_button.clicked.connect(usual_signal.Sgn)
            elif c == 3:
                self.run_button.clicked.connect(usual_signal.Rect)
            elif c == 4:
                self.run_button.clicked.connect(usual_signal.Tri)
            elif c == 5:
                self.run_button.clicked.connect(usual_signal.td1)
            elif c == 6:
                self.run_button.clicked.connect(usual_signal.exo1_td2)
            elif c == 7:
                self.run_button.clicked.connect(usual_signal.exo2_td2)
            elif c == 8:
                self.run_button.clicked.connect(usual_signal.exo3_td2)
            else :
                self.run_button.clicked.connect(self.error)
            i = 0
        
    def error(self):
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setText("Ther is an error!")
        msg1.setInformativeText("We are workning on that ...")
        msg1.setWindowTitle("Error")
        msg1.exec_()    

    
    
    def action(self):
        print("L'affichage de l'image de la fonction ...")
        

        #image = QImage(QImageReader(":/images/test.png").read())

    def check(self):
        self.add_button.clicked.connect(lambda:self.test(self.add_button))
        
    def test(self,b):
        if b.isChecked() == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Coming soon !!!")
            msg.setInformativeText("We are working on that!")
            msg.setWindowTitle("Add new foction")
            self.usuel_signal_button.setChecked(True)
            msg.exec_()
        

    def handle_ui(self):
        self.setWindowIcon(QIcon('line-graph.png'))
    

    
    

    
        
    
def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

