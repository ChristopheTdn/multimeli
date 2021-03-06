#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Action
from PyQt5 import QtMultimedia
from . import core

def joue_son(son="sounds/clic.wav"):
    sound=QtMultimedia.QSound.play(son)

def Push_ButtonA(self,action):
    joue_son()
    if action == "Début":        
        core.bouclePrincipale(self)
    if action == "Répondre":      
       DisableButtons(self)
       core.Answer(self,self.label_Reponse_A.text())
  
def Push_ButtonB(self,action):
    joue_son()
    if action == "Répondre":      
       DisableButtons(self)
       core.Answer(self,self.label_Reponse_B.text())

def Push_ButtonC(self,action):
    joue_son()
    if action == "Quitter":
        self.close() 
    if action == "Répondre":      
       DisableButtons(self)
       core.Answer(self,self.label_Reponse_C.text())
    
def DisableButtons(self):
    self.timer.stop()
    self.pushButton_ReponseA.setEnabled(False)
    self.pushButton_ReponseB.setEnabled(False)
    self.pushButton_ReponseC.setEnabled(False)
 
