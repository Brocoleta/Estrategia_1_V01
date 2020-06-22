
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QLabel)
from parametros import *
from clase import *



nombre, clase = uic.loadUiType("form.ui")
class MenuInicio(nombre, clase):
    def __init__(self,vxx, vix):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.vxx = vxx
        self.vix = vix
        self.pushButton.clicked.connect(self.mandar_datos)
    def mandar_datos(self):
        self.capital_disponible = self.capital_inicial_box.value()
        self.ino = self.inversion_inicial_box.value()
        self.primer_rebote = self.primer_rebote_box.value()
        self.segundo_rebote = self.segundo_rebote_box.value()
        self.tercer_rebote = self.tercer_rebote_box.value()
        self.avu = self.aumento_posicion_box.value()
        self.stop_prof = self.stop_prof_box.value()
        self.stop_loss = self.stop_loss_box.value()
        self.dias_stop_loss = self.dias_stop_loss_box.value()
        e = Equity(self.capital_disponible,self.ino,self.primer_rebote,self.segundo_rebote,self.tercer_rebote,self.avu,False,False,False,self.stop_prof,self.stop_loss,self.dias_stop_loss,self.vxx,self.vix)
        e.start()
        while not e.isFinished():
            None

        self.close()
