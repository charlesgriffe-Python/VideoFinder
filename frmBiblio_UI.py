# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmBiblio_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindowBiblio(object):
    def setupUi(self, mainWindowBiblio):
        mainWindowBiblio.setObjectName("mainWindowBiblio")
        mainWindowBiblio.resize(700, 483)
        self.lblIcone = QtWidgets.QLabel(mainWindowBiblio)
        self.lblIcone.setGeometry(QtCore.QRect(30, 20, 131, 111))
        self.lblIcone.setText("")
        self.lblIcone.setPixmap(QtGui.QPixmap("Ressources/BiblioRoot.png"))
        self.lblIcone.setScaledContents(True)
        self.lblIcone.setObjectName("lblIcone")
        self.lblTitre = QtWidgets.QLabel(mainWindowBiblio)
        self.lblTitre.setGeometry(QtCore.QRect(170, 20, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitre.setFont(font)
        self.lblTitre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitre.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblTitre.setLineWidth(0)
        self.lblTitre.setTextFormat(QtCore.Qt.RichText)
        self.lblTitre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTitre.setWordWrap(True)
        self.lblTitre.setObjectName("lblTitre")
        self.frame = QtWidgets.QFrame(mainWindowBiblio)
        self.frame.setGeometry(QtCore.QRect(10, 150, 271, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lstBiblio = QtWidgets.QListWidget(self.frame)
        self.lstBiblio.setGeometry(QtCore.QRect(10, 30, 256, 291))
        self.lstBiblio.setObjectName("lstBiblio")
        self.frame_2 = QtWidgets.QFrame(mainWindowBiblio)
        self.frame_2.setGeometry(QtCore.QRect(290, 150, 391, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 251, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 56, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 56, 16))
        self.label_4.setObjectName("label_4")
        self.btSupprimer = QtWidgets.QPushButton(self.frame_2)
        self.btSupprimer.setGeometry(QtCore.QRect(120, 130, 93, 28))
        self.btSupprimer.setObjectName("btSupprimer")
        self.lneNom = QtWidgets.QLineEdit(self.frame_2)
        self.lneNom.setGeometry(QtCore.QRect(90, 50, 291, 21))
        self.lneNom.setObjectName("lneNom")
        self.lneChemin = QtWidgets.QLineEdit(self.frame_2)
        self.lneChemin.setGeometry(QtCore.QRect(90, 90, 291, 21))
        self.lneChemin.setObjectName("lneChemin")
        self.btSauver = QtWidgets.QPushButton(self.frame_2)
        self.btSauver.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.btSauver.setObjectName("btSauver")
        self.btOuvrir = QtWidgets.QPushButton(self.frame_2)
        self.btOuvrir.setGeometry(QtCore.QRect(290, 130, 93, 28))
        self.btOuvrir.setObjectName("btOuvrir")
        self.frame_3 = QtWidgets.QFrame(mainWindowBiblio)
        self.frame_3.setGeometry(QtCore.QRect(290, 330, 391, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 331, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnRacine = QtWidgets.QPushButton(self.frame_3)
        self.btnRacine.setGeometry(QtCore.QRect(20, 40, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRacine.sizePolicy().hasHeightForWidth())
        self.btnRacine.setSizePolicy(sizePolicy)
        self.btnRacine.setMinimumSize(QtCore.QSize(75, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ressources/parcourir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRacine.setIcon(icon)
        self.btnRacine.setIconSize(QtCore.QSize(32, 32))
        self.btnRacine.setObjectName("btnRacine")
        self.btnFermer = QtWidgets.QPushButton(mainWindowBiblio)
        self.btnFermer.setGeometry(QtCore.QRect(590, 450, 93, 28))
        self.btnFermer.setObjectName("btnFermer")

        self.retranslateUi(mainWindowBiblio)
        QtCore.QMetaObject.connectSlotsByName(mainWindowBiblio)

    def retranslateUi(self, mainWindowBiblio):
        _translate = QtCore.QCoreApplication.translate
        mainWindowBiblio.setWindowTitle(_translate("mainWindowBiblio", "Dialog"))
        self.lblTitre.setText(_translate("mainWindowBiblio", "Gestion des bibliothèques"))
        self.label.setText(_translate("mainWindowBiblio", "Liste des bibliothèques :"))
        self.label_2.setText(_translate("mainWindowBiblio", "Edition d\'une bibliothèque :"))
        self.label_3.setText(_translate("mainWindowBiblio", "Nom :"))
        self.label_4.setText(_translate("mainWindowBiblio", "Chemin :"))
        self.btSupprimer.setText(_translate("mainWindowBiblio", "Supprimer"))
        self.btSauver.setText(_translate("mainWindowBiblio", "Sauver"))
        self.btOuvrir.setText(_translate("mainWindowBiblio", "Ouvrir"))
        self.label_5.setText(_translate("mainWindowBiblio", "Ajouter une nouvelle bibliothèque :"))
        self.btnRacine.setText(_translate("mainWindowBiblio", "Parcourir"))
        self.btnFermer.setText(_translate("mainWindowBiblio", "Fermer"))
