# ! /usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from MainUI import Form
import sys
global nbrFaute
global nbrTour

global myapp

if __name__ == "__main__":
      app = QtWidgets.QApplication(sys.argv)  
      myapp = Form()
      myapp.show()     
      sys.exit(app.exec_())
