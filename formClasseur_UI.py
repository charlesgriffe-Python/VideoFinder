# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formClasseur_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(781, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Ressources/classeurs.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lblTitre = QtWidgets.QLabel(Dialog)
        self.lblTitre.setGeometry(QtCore.QRect(90, 10, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitre.setFont(font)
        self.lblTitre.setTextFormat(QtCore.Qt.RichText)
        self.lblTitre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTitre.setWordWrap(True)
        self.lblTitre.setObjectName("lblTitre")
        self.listClasseur = QtWidgets.QListWidget(Dialog)
        self.listClasseur.setGeometry(QtCore.QRect(10, 80, 256, 391))
        self.listClasseur.setObjectName("listClasseur")
        self.tabWidgetClasseur = QtWidgets.QTabWidget(Dialog)
        self.tabWidgetClasseur.setGeometry(QtCore.QRect(280, 60, 491, 411))
        self.tabWidgetClasseur.setObjectName("tabWidgetClasseur")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 14))
        self.label_2.setObjectName("label_2")
        self.lneNom = QtWidgets.QLineEdit(self.tab)
        self.lneNom.setGeometry(QtCore.QRect(10, 40, 461, 31))
        self.lneNom.setObjectName("lneNom")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 461, 111))
        self.textEdit.setObjectName("textEdit")
        self.btnAnnuler = QtWidgets.QPushButton(self.tab)
        self.btnAnnuler.setGeometry(QtCore.QRect(390, 350, 75, 23))
        self.btnAnnuler.setObjectName("btnAnnuler")
        self.btnSauver = QtWidgets.QPushButton(self.tab)
        self.btnSauver.setGeometry(QtCore.QRect(310, 350, 75, 23))
        self.btnSauver.setObjectName("btnSauver")
        self.btnDelete = QtWidgets.QPushButton(self.tab)
        self.btnDelete.setGeometry(QtCore.QRect(10, 350, 75, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.btnNouveau = QtWidgets.QPushButton(self.tab)
        self.btnNouveau.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.btnNouveau.setObjectName("btnNouveau")
        self.chkDefaut = QtWidgets.QCheckBox(self.tab)
        self.chkDefaut.setGeometry(QtCore.QRect(10, 240, 81, 20))
        self.chkDefaut.setObjectName("chkDefaut")
        self.tabWidgetClasseur.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidgetClasseur.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidgetClasseur.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestion des classeurs"))
        self.lblTitre.setText(_translate("Dialog", "Gestion des Classeurs"))
        self.label_2.setText(_translate("Dialog", "Nom :"))
        self.label_3.setText(_translate("Dialog", "Commentaire :"))
        self.btnAnnuler.setText(_translate("Dialog", "Annuler"))
        self.btnSauver.setText(_translate("Dialog", "Sauver"))
        self.btnDelete.setText(_translate("Dialog", "Supprimer"))
        self.btnNouveau.setText(_translate("Dialog", "Nouveau"))
        self.chkDefaut.setText(_translate("Dialog", "Défaut"))
        self.tabWidgetClasseur.setTabText(self.tabWidgetClasseur.indexOf(self.tab), _translate("Dialog", "Général"))
        self.tabWidgetClasseur.setTabText(self.tabWidgetClasseur.indexOf(self.tab_2), _translate("Dialog", "Vidéos"))
