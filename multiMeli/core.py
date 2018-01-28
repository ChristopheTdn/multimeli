#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE

from . import show
from PyQt5.QtCore import QTimer
import random

def initApplication(self):
    global myapp
    myapp = self
    global optionTable
    optionTable = [0, self.checkBox_1,self.checkBox_2,self.checkBox_3,self.checkBox_4,self.checkBox_5,self.checkBox_6,self.checkBox_7,self.checkBox_8,self.checkBox_9,self.checkBox_10]
    global nbrFaute
    global nbrTour
    nbrFaute = 0
    nbrTour = 0
    show.initMenuOuverture(self)   
     
def TimingEnd():
    global myapp
    global timing
    myapp.label_Message_Reponse.setText(str(timing)+" Sec.")
    timing -= 1   
    if timing == -1:
        myapp.timer.stop()
        Answer(myapp, 0)
        
def TimingNextTurn():
    global myapp
    myapp.timer.stop()
    tourDeJeu(myapp)
    
def bouclePrincipale(self):
    show.initDebutPartie(self)
    tourDeJeu(self)

def tourDeJeu(self):
    show.question(self, listeQuestion())
    # Init Timer 20 seconde
    global timing
    timing = 20
    self.timer= QTimer()
    self.timer.timeout.connect(TimingEnd)
    self.timer.start(1000)
    
def Answer(self, reponseJoueur):
    global nbrTour   
    global nbrFaute
    
    bonneReponse= str(int(self.label_Nbr1.text())*int(self.label_Nbr2.text()))   
    listeReponse=[self.label_Reponse_A.text(), self.label_Reponse_B.text(), self.label_Reponse_C.text()] 
    indexBonneReponse=listeReponse.index(bonneReponse)
    self.label_Reponse_A.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#998877;\">"+listeReponse[0]+"</span></p></body></html>")
    self.label_Reponse_B.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#998877;\">"+listeReponse[1]+"</span></p></body></html>")
    self.label_Reponse_C.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#998877;\">"+listeReponse[2]+"</span></p></body></html>")

    if indexBonneReponse==0:
        self.label_Reponse_A.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#338855;\"><b>"+bonneReponse+"</b></span></p></body></html>")
    elif indexBonneReponse==1:
        self.label_Reponse_B.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#338855;\"><b>"+bonneReponse+"</b></span></p></body></html>")
    else:
        self.label_Reponse_C.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;color:#338855;\"><b>"+bonneReponse+"</b></span></p></body></html>")

    if int(reponseJoueur) == int(bonneReponse):        
        self.label_Message_Reponse.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;color:#338855;\">Bonne Réponse</span></p></body></html>")
    else:
        nbrFaute += 1
        self.label_Message_Reponse.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#aa8877;\">Oups...</span></p></body></html>")
    

    nbrTour += 1
    MajScore(self)
    self.timer.timeout.connect(TimingNextTurn)
    self.timer.start(4000)    
    
def listeQuestion():
    x=0    
    while (x==0):
        xx = random.randrange(2, 11)
        if(optionTable[xx].isChecked()):
            x=xx        
    y = random.randrange(2, 11)
    listeReponse = [x*y,(x+1)*y, x*(y-1)]
    random.shuffle(listeReponse)
    return listeReponse+[x, y]
    
def MajScore(self):
    self.progressBar_Cool.setProperty("value", 100 - (nbrFaute * 100 / nbrTour))
    
