

if __name__ == '__main__':

    import sys

    import os
    from clase import Equity
    from carga import vxx, vix
    from openpyxl import load_workbook
    p = load_workbook('parametros.xlsx')
    ps = p.active
    capital_disponible = int(ps['B2'].value)
    ino = float(ps['B5'].value)/100
    primer_rebote = float(ps['B3'].value)/100
    avu = float(ps['B4'].value)/100
    stop_prof = float(ps['B6'].value)
    stop_loss = float(ps['B7'].value)/100
    dias_stop_loss = int(ps['B9'].value)
    exp_stop_loss = float(ps['B8'].value)/100
    pos_expocicion = float(ps['B10'].value)/100

    Equity(capital_disponible,ino,primer_rebote,avu,stop_prof,stop_loss,dias_stop_loss,vxx,vix,exp_stop_loss,pos_expocicion)
