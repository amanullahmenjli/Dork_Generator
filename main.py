#needed modules
from os import remove   #for deleting dork.txt
import sys  #for argv
from PyQt5.QtWidgets import QDialog, QApplication   #for  interface
from interface import *   #interface made by qt designer



#used search functions
search_functions = ['inurl:',
                                    'intitle:',
                                    'intext:',
                                    'inbody:',
                                    'related',
                                    'cache:',
                                    'book:',
                                    'maps:']


#Application class
class MyApplication(QDialog):
    
    #clear function
    def clear(self):
        self.ui.kl.clear() #clear keywords list
        self.ui.pfl.clear() #clear page formats list
        self.ui.ptl.clear() #clear page types list
        self.ui.del_.clear() #clear domain extansions list
        self.ui.list.clear() #clear generated list
    
    #Dork Generation Function (Most Important Function! )
    def gen(self):
        remove('dork.txt') #delete dork.txt file to make new one later ( line 48)
        self.ui.list.clear() #clear function
        for word in search_functions: 
            t1 = self.ui.kl.toPlainText().splitlines()
            for line1 in t1:
                t2 = self.ui.pfl.toPlainText().splitlines()
                for line2 in t2:
                    t3 = self.ui.ptl.toPlainText().splitlines()
                    for line3 in t3:
                        t4 = self.ui.del_.toPlainText().splitlines()
                        for line4 in t4:
                            txt = [word,line1,' inurl:',line2,'?',line3,'= site:.',line4,'\n']
                            str1 = ""
                            self.ui.list.insertPlainText(str1.join(txt))
                            with open('dork.txt','a') as dork:
                                dork.writelines(txt)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.gen_btn.clicked.connect(self.gen)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyApplication()
    w.show()
    sys.exit(app.exec_())