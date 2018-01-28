#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface SHOW

def initMenuOuverture(self):
    self.label_Message_Reponse.setText("Débuter la partie ?")
    self.pushButton_ReponseA.setEnabled(True)
    self.pushButton_ReponseA.setText("Début")    
    self.pushButton_ReponseB.setVisible(False)
    self.pushButton_ReponseC.setEnabled(True)    
    self.pushButton_ReponseC.setText("Quitter")
    self.label_X.setText("")
    self.label_Nbr1.setText("")
    self.label_Nbr2.setText("")
    self.label_Reponse_A.setText("")
    self.label_Reponse_B.setText("")
    self.label_Reponse_C.setText("")

def initDebutPartie(self):
    self.label_Message_Reponse.setText("")
    self.pushButton_ReponseA.setEnabled(False)
    self.pushButton_ReponseA.setText("Répondre")
    self.pushButton_ReponseA.setVisible(True) 
    
    self.pushButton_ReponseB.setEnabled(False)    
    self.pushButton_ReponseB.setText("Répondre")
    self.pushButton_ReponseB.setVisible(True) 
    
    self.pushButton_ReponseC.setEnabled(False)    
    self.pushButton_ReponseC.setText("Répondre")    
    self.pushButton_ReponseC.setVisible(True) 
    
    self.label_X.setText("X")
    self.label_Nbr1.setText("?")
    self.label_Nbr2.setText("?")
    self.label_Reponse_A.setText("00")
    self.label_Reponse_B.setText("00")
    self.label_Reponse_C.setText("00")
    
def question(self, listeReponse):
    self.label_Nbr1.setText(str(listeReponse[3]))
    self.label_Nbr2.setText(str(listeReponse[4]))
    self.pushButton_ReponseA.setEnabled(True)
    self.pushButton_ReponseA.setText("Répondre")    
    self.pushButton_ReponseB.setEnabled(True)
    self.pushButton_ReponseB.setText("Répondre")    
    self.pushButton_ReponseC.setEnabled(True)
    self.pushButton_ReponseC.setText("Répondre")
    # Reponse possible
    self.label_Reponse_A.setText(str(listeReponse[0]))
    self.label_Reponse_B.setText(str(listeReponse[1]))
    self.label_Reponse_C.setText(str(listeReponse[2]))
