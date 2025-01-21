# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
import requests
import webbrowser
import threading
from PyQt5.QtWidgets import QApplication
from tkinter import messagebox

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.resize(642, 417)
MainWindow.setMinimumSize(642, 417)
MainWindow.setMaximumSize(642, 417)
centralwidget = QtWidgets.QWidget(MainWindow)
centralwidget.setObjectName("centralwidget")

frame = QtWidgets.QFrame(centralwidget)
frame.setGeometry(QtCore.QRect(0, 0, 648, 61))
frame.setStyleSheet("background-color: rgb(235, 235, 235);")
frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
frame.setFrameShadow(QtWidgets.QFrame.Raised)
frame.setObjectName("frame")

def track_ip():
     global lista_datos
     global latitud
     global longitud

     ip = ip_entry.text()

     api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"
     data = requests.get(api).json()
     lista_datos = []

     if data.get('message') == 'invalid query':
        messagebox.showerror('IPScope', 'ERROR: La IP no es valida.')
        try:
          label_localizacion.setVisible(False)
          label_imagen_local.setVisible(False)
          label_cords.setVisible(False)
          eliminardatos()
        except:
          pass
     else:
        copiar_btn.setVisible(True)
        clear_btn.setVisible(True)

        # Rellenar la tabla con la informacion
        item = entry_datos_ip.item(0, 0)
        item.setText(data['query'])
        item = entry_datos_ip.item(0, 1)
        item.setText(data['isp'])
        item = entry_datos_ip.item(0, 2)
        item.setText(data['org'])
        item = entry_datos_ip.item(0, 3)
        item.setText(data['city'])
        item = entry_datos_ip.item(0, 4)
        item.setText(data['country'])
        item = entry_datos_ip.item(0, 5)
        item.setText(data['regionName'])
        #------------------------------------#
        item = entry_datos_ip2.item(0, 0)
        item.setText(data['continent'])
        item = entry_datos_ip2.item(0, 1)
        item.setText(data['reverse'])
        item = entry_datos_ip2.item(0, 2)
        if data["proxy"] == True:
          item.setText('Si')
        else:
          item.setText('No')
        item = entry_datos_ip2.item(0, 3)
        item.setText(data['zip'])
        item = entry_datos_ip2.item(0, 4)
        item.setText(str(data['lat']))
        item = entry_datos_ip2.item(0, 5)
        item.setText(str(data['lon']))

        latitud = str(data["lat"])
        longitud = str(data["lon"])

        # Agregar los datos de la IP a la lista 'lista_datos'
        lista_datos.append('\n'.join([
          f'IP: {data["query"]}',
          f'ISP: {data["isp"]}',
          f'Organizacion: {data["org"]}',
          f'Ciudad: {data["city"]}',
          f'Pais: {data["country"]}',
          f'Region/Estado: {data["regionName"]}',
          f'Continente: {data["continent"]}',
          f'DNS Inverso: {data["reverse"]}',
          f'VPN: {data["proxy"]}',
          f'Codigo ZIP: {data["zip"]}',
          f'Latitud: {data["lat"]}',
          f'Longitud: {data["lon"]}'
        ]))

iniciar_btn = QtWidgets.QPushButton(frame)
iniciar_btn.setGeometry(QtCore.QRect(10, 10, 111, 41))
iniciar_btn.setStyleSheet("QPushButton {\n"
"                font: 12pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("icons/lup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
iniciar_btn.setIcon(icon)
iniciar_btn.setIconSize(QtCore.QSize(20, 20))
iniciar_btn.setObjectName("iniciar_btn")
iniciar_btn.clicked.connect(track_ip)

def trackme():
     global lista_datos
     global latitud
     global longitud

     api = f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"
     data = requests.get(api).json()
     lista_datos = []

     copiar_btn.setVisible(True)
     clear_btn.setVisible(True)

     # Rellenar la tabla con la informacion
     item = entry_datos_ip.item(0, 0)
     item.setText(data['query'])
     item = entry_datos_ip.item(0, 1)
     item.setText(data['isp'])
     item = entry_datos_ip.item(0, 2)
     item.setText(data['org'])
     item = entry_datos_ip.item(0, 3)
     item.setText(data['city'])
     item = entry_datos_ip.item(0, 4)
     item.setText(data['country'])
     item = entry_datos_ip.item(0, 5)
     item.setText(data['regionName'])
     #------------------------------------#
     item = entry_datos_ip2.item(0, 0)
     item.setText(data['continent'])
     item = entry_datos_ip2.item(0, 1)
     item.setText(data['reverse'])
     item = entry_datos_ip2.item(0, 2)
     if data["proxy"] == True:
        item.setText('Si')
     else:
        item.setText('No')
     item = entry_datos_ip2.item(0, 3)
     item.setText(data['zip'])
     item = entry_datos_ip2.item(0, 4)
     item.setText(str(data['lat']))
     item = entry_datos_ip2.item(0, 5)
     item.setText(str(data['lon']))     
     
     latitud = str(data["lat"])
     longitud = str(data["lon"])

     # Agregar los datos de la IP a la lista 'lista_datos'
     lista_datos.append('\n'.join([
        f'IP: {data["query"]}',
        f'ISP: {data["isp"]}',
        f'Organizacion: {data["org"]}',
        f'Ciudad: {data["city"]}',
        f'Pais: {data["country"]}',
        f'Region/Estado: {data["regionName"]}',
        f'Continente: {data["continent"]}',
        f'DNS Inverso: {data["reverse"]}',
        f'VPN: {data["proxy"]}',
        f'Codigo ZIP: {data["zip"]}',
        f'Latitud: {data["lat"]}',
        f'Longitud: {data["lon"]}'
     ]))

trackme_btn = QtWidgets.QPushButton(frame)
trackme_btn.setGeometry(QtCore.QRect(130, 10, 111, 41))
trackme_btn.setStyleSheet("font: 10pt \"Arial\";\n""background-color: rgb(221, 221, 221);")
trackme_btn.setStyleSheet("QPushButton {\n"
"                font: 10pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
trackme_btn.setObjectName("trackme_btn")
trackme_btn.clicked.connect(trackme)

frame_2 = QtWidgets.QFrame(centralwidget)
frame_2.setGeometry(QtCore.QRect(0, 60, 648, 31))
frame_2.setStyleSheet("background-color: rgb(235, 235, 235);")
frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
frame_2.setObjectName("frame_2")

line = QtWidgets.QFrame(frame_2)
line.setGeometry(QtCore.QRect(0, 0, 643, 3))
line.setFrameShape(QtWidgets.QFrame.HLine)
line.setFrameShadow(QtWidgets.QFrame.Sunken)
line.setObjectName("line")

ip_entry = QtWidgets.QLineEdit(frame_2)
ip_entry.setGeometry(QtCore.QRect(10, 6, 311, 20))
ip_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
ip_entry.setClearButtonEnabled(True)
ip_entry.setObjectName("ip_entry")

label_example = QtWidgets.QLabel(frame_2)
label_example.setGeometry(QtCore.QRect(330, 7, 271, 16))
label_example.setStyleSheet("color: rgb(113, 113, 113);")
label_example.setObjectName("label_example")

frame_3 = QtWidgets.QFrame(centralwidget)
frame_3.setGeometry(QtCore.QRect(0, 90, 648, 331))
frame_3.setStyleSheet("background-color: rgb(235, 235, 235);")
frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
frame_3.setObjectName("frame_3")

line_2 = QtWidgets.QFrame(frame_3)
line_2.setGeometry(QtCore.QRect(0, 0, 643, 3))
line_2.setFrameShape(QtWidgets.QFrame.HLine)
line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
line_2.setObjectName("line_2")

tabWidget = QtWidgets.QTabWidget(frame_3)
tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 291))
tabWidget.setObjectName("tabWidget")

tab = QtWidgets.QWidget()
tab.setObjectName("tab")

entry_datos_ip = QtWidgets.QTableWidget(tab)
entry_datos_ip.setGeometry(QtCore.QRect(0, 0, 615, 71))
entry_datos_ip.setObjectName("entry_datos_ip")
entry_datos_ip.setColumnCount(6)
entry_datos_ip.setRowCount(1)

item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setVerticalHeaderItem(0, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(0, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(1, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(2, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(3, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(4, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip.setHorizontalHeaderItem(5, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip.setItem(0, 0, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip.setItem(0, 1, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip.setItem(0, 2, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip.setItem(0, 3, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip.setItem(0, 4, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

entry_datos_ip.setItem(0, 5, item)
entry_datos_ip2 = QtWidgets.QTableWidget(tab)
entry_datos_ip2.setGeometry(QtCore.QRect(0, 70, 615, 71))
entry_datos_ip2.setObjectName("entry_datos_ip2")
entry_datos_ip2.setColumnCount(6)
entry_datos_ip2.setRowCount(1)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setVerticalHeaderItem(0, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(0, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(1, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(2, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(3, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(4, item)
item = QtWidgets.QTableWidgetItem()
entry_datos_ip2.setHorizontalHeaderItem(5, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 0, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 1, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 2, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 3, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 4, item)
item = QtWidgets.QTableWidgetItem()
item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
entry_datos_ip2.setItem(0, 5, item)

def copiar_datos():
  for data in lista_datos:
    clipboard = QApplication.clipboard()
    clipboard.setText(data)
  messagebox.showinfo('IPScope', 'Copiado al portapapeles.')

copiar_btn = QtWidgets.QPushButton(tab)
copiar_btn.setGeometry(QtCore.QRect(20, 180, 191, 41))
copiar_btn.setStyleSheet("QPushButton {\n"
"                font: 12pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
icon1 = QtGui.QIcon()
icon1.addPixmap(QtGui.QPixmap("icons/clip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
copiar_btn.setIcon(icon1)
copiar_btn.setIconSize(QtCore.QSize(25, 25))
copiar_btn.setObjectName("copiar_btn")
copiar_btn.clicked.connect(copiar_datos)
copiar_btn.setVisible(False)

def eliminardatos():
   item = entry_datos_ip.item(0, 0)
   item.setText('')
   for i in range(6):
       item = entry_datos_ip.item(0, i)
       item.setText('')

   item = entry_datos_ip2.item(0, 0)
   item.setText('')
   for i in range(6):
       item = entry_datos_ip2.item(0, i)
       item.setText('') 

   copiar_btn.setVisible(False)
   clear_btn.setVisible(False)
   try:
      label_localizacion.setVisible(False)
      label_imagen_local.setVisible(False)
      label_cords.setVisible(False)
   except:
    pass


clear_btn = QtWidgets.QPushButton(tab)
clear_btn.setGeometry(QtCore.QRect(330, 180, 191, 41))
clear_btn.setStyleSheet("QPushButton {\n"
"                font: 12pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
icon2 = QtGui.QIcon()
icon2.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
clear_btn.setIcon(icon2)
clear_btn.setIconSize(QtCore.QSize(25, 25))
clear_btn.setObjectName("clear_btn")
clear_btn.setVisible(False)
clear_btn.clicked.connect(eliminardatos)

tabWidget.addTab(tab, "")
tab_2 = QtWidgets.QWidget()
tab_2.setObjectName("tab_2")

label_imagen_local = QtWidgets.QLabel(tab_2)
label_imagen_local.setGeometry(QtCore.QRect(200, 20, 391, 231))
label_imagen_local.setStyleSheet("background-color: transparent;")
label_imagen_local.setObjectName("label_imagen_local")
label_imagen_local.setVisible(False)

label_localizacion = QtWidgets.QLabel(tab_2)
label_localizacion.setGeometry(QtCore.QRect(330, 1, 81, 17))
label_localizacion.setStyleSheet("font: 10pt \"Arial\";\n""color: rgb(0, 0, 0);")
label_localizacion.setObjectName("label_localizacion")
label_localizacion.setVisible(False)

def locate_func():
  messagebox.showinfo('IPScope', 'Obteniendo localizacion con latitud y longitud...')
  try:
    res = requests.get(f'https://cache.ip-api.com/{longitud},{latitud},10')
    if res.status_code == 200:
      image_data = res.content
      pixmap = QPixmap()
      pixmap.loadFromData(image_data)
      if not pixmap.isNull():
        label_imagen_local.setPixmap(pixmap)
        label_imagen_local.setScaledContents(True)
        
      label_localizacion.setVisible(True)
      label_imagen_local.setVisible(True)
      label_cords.setVisible(True)
      label_cords.setText(f"{longitud}, {latitud}")
  except:
    messagebox.showerror('IPScope', 'ERROR: No se ha podido determinar la longitud y latitud.')

def locate():
  th = threading.Thread(target=locate_func)
  th.start()

iniciar_btn_3 = QtWidgets.QPushButton(tab_2)
iniciar_btn_3.setGeometry(QtCore.QRect(10, 10, 151, 31))
iniciar_btn_3.setStyleSheet("QPushButton {\n"
"                font: 12pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
icon3 = QtGui.QIcon()
icon3.addPixmap(QtGui.QPixmap("icons/init_btn_lg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
iniciar_btn_3.setIcon(icon3)
iniciar_btn_3.setIconSize(QtCore.QSize(25, 25))
iniciar_btn_3.setObjectName("iniciar_btn_3")
iniciar_btn_3.clicked.connect(locate)

line_3 = QtWidgets.QFrame(tab_2)
line_3.setGeometry(QtCore.QRect(180, 0, 16, 265))
line_3.setFrameShape(QtWidgets.QFrame.VLine)
line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
line_3.setObjectName("line_3")

def abrirgl():
  try:
    webbrowser.open_new_tab(f'https://www.google.com/maps/place/{latitud},{longitud}')
  except:
    messagebox.showerror('IPScope', 'ERROR: No se ha podido abrir una ventana en el navegador.')

iniciar_btn_4 = QtWidgets.QPushButton(tab_2)
iniciar_btn_4.setGeometry(QtCore.QRect(10, 60, 151, 31))
iniciar_btn_4.setStyleSheet("QPushButton {\n"
"                font: 12pt \"Arial\";"
"                background-color: #b3b3b3;\n"
"                border-radius: 2px;\n"
"                padding: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"                background-color: #bfbfbf\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #999999\n"
"}")
icon4 = QtGui.QIcon()
icon4.addPixmap(QtGui.QPixmap("icons/gl_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
iniciar_btn_4.setIcon(icon4)
iniciar_btn_4.setIconSize(QtCore.QSize(25, 25))
iniciar_btn_4.setObjectName("iniciar_btn_4")
iniciar_btn_4.clicked.connect(abrirgl)

label_cords = QtWidgets.QLabel(tab_2)
label_cords.setGeometry(QtCore.QRect(330, 250, 121, 17))
label_cords.setStyleSheet("font: 9pt \"Arial\";\n""color: rgb(0, 0, 0);""\nbackground-color: transparent;")
label_cords.setObjectName("label_cords")
label_cords.setVisible(False)

tabWidget.addTab(tab_2, "")

label_2 = QtWidgets.QLabel(frame_3)
label_2.setGeometry(QtCore.QRect(185, 303, 241, 20))
label_2.setStyleSheet("font: 11pt \"Bahnschrift\";")
label_2.setAlignment(QtCore.Qt.AlignCenter)
label_2.setObjectName("label_2")

tabWidget.setCurrentIndex(0)
MainWindow.setCentralWidget(centralwidget)
QtCore.QMetaObject.connectSlotsByName(MainWindow)

def retranslateUi(MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "IPScope"))
    iniciar_btn.setText(_translate("MainWindow", "Iniciar"))
    trackme_btn.setText(_translate("MainWindow", "¿Cual es mi IP?"))
    label_example.setText(_translate("MainWindow", "Ejemplo: 142.250.113.113, 2607:f8b0:4023:1000::71"))
    item = entry_datos_ip.verticalHeaderItem(0)
    item.setText(_translate("MainWindow", "1"))
    item = entry_datos_ip.horizontalHeaderItem(0)
    item.setText(_translate("MainWindow", "IP"))
    item = entry_datos_ip.horizontalHeaderItem(1)
    item.setText(_translate("MainWindow", "ISP"))
    item = entry_datos_ip.horizontalHeaderItem(2)
    item.setText(_translate("MainWindow", "Organizacion"))
    item = entry_datos_ip.horizontalHeaderItem(3)
    item.setText(_translate("MainWindow", "Ciudad"))
    item = entry_datos_ip.horizontalHeaderItem(4)
    item.setText(_translate("MainWindow", "Pais"))
    item = entry_datos_ip.horizontalHeaderItem(5)
    item.setText(_translate("MainWindow", "Region/Estado"))
    __sortingEnabled = entry_datos_ip.isSortingEnabled()
    entry_datos_ip.setSortingEnabled(False)
    entry_datos_ip.setSortingEnabled(__sortingEnabled)
    item = entry_datos_ip2.verticalHeaderItem(0)
    item.setText(_translate("MainWindow", "2"))
    item = entry_datos_ip2.horizontalHeaderItem(0)
    item.setText(_translate("MainWindow", "Continente"))
    item = entry_datos_ip2.horizontalHeaderItem(1)
    item.setText(_translate("MainWindow", "DNS Inverso"))
    item = entry_datos_ip2.horizontalHeaderItem(2)
    item.setText(_translate("MainWindow", "VPN"))
    item = entry_datos_ip2.horizontalHeaderItem(3)
    item.setText(_translate("MainWindow", "Codigo ZIP"))
    item = entry_datos_ip2.horizontalHeaderItem(4)
    item.setText(_translate("MainWindow", "Latitud"))
    item = entry_datos_ip2.horizontalHeaderItem(5)
    item.setText(_translate("MainWindow", "Longitud"))
    __sortingEnabled = entry_datos_ip2.isSortingEnabled()
    entry_datos_ip2.setSortingEnabled(False)
    entry_datos_ip2.setSortingEnabled(__sortingEnabled)
    copiar_btn.setText(_translate("MainWindow", "Copiar Datos"))
    clear_btn.setText(_translate("MainWindow", "Limpiar Datos"))
    tabWidget.setTabText(tabWidget.indexOf(tab), _translate("MainWindow", "Informacion"))
    label_localizacion.setText(_translate("MainWindow", "Localizacion:"))
    iniciar_btn_3.setText(_translate("MainWindow", "Geolocalizar"))
    iniciar_btn_4.setText(_translate("MainWindow", "Google Maps"))
    tabWidget.setTabText(tabWidget.indexOf(tab_2), _translate("MainWindow", "Geolocalizacion"))
    label_2.setText(_translate("MainWindow", "By: Euronymou5"))

retranslateUi(MainWindow)

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())