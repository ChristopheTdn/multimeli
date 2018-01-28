# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from Ui_MainUI import Ui_Form
import multiMeli

class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        multiMeli.core.initApplication(self)
    
    @pyqtSlot()
    def on_pushButton_ReponseA_clicked(self):
        """
        Slot documentation goes here.
        """
        # Action par defaut quand on appuis sur le Bouton A
        # TODO: Ajouter un effet sonore bouton A
        multiMeli.action.Push_ButtonA(self,self.pushButton_ReponseA.text())
    
    @pyqtSlot()
    def on_pushButton_ReponseB_clicked(self):
        """
        Slot documentation goes here.
        """
        # Action par defaut quand on appuis sur le Bouton B
        # TODO: Ajouter un effet sonore bouton B
        multiMeli.action.Push_ButtonB(self,self.pushButton_ReponseB.text())
    
    @pyqtSlot()
    def on_pushButton_ReponseC_clicked(self):
        """
        Slot documentation goes here.
        """
        # Action par defaut quand on appuis sur le Bouton C
        # TODO: Ajouter un effet sonore bouton C
        multiMeli.action.Push_ButtonC(self,self.pushButton_ReponseC.text())
