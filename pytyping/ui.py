from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 642, 476))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(640, 100))
        self.textBrowser.setMaximumSize(QtCore.QSize(640, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.time_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.time_label.setMinimumSize(QtCore.QSize(199, 30))
        self.time_label.setMaximumSize(QtCore.QSize(199, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(12)
        font.setUnderline(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color:rgb(255, 0, 0)")
        self.time_label.setTextFormat(QtCore.Qt.PlainText)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_lable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.info_lable.setEnabled(False)
        self.info_lable.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.info_lable.setFont(font)
        self.info_lable.setStyleSheet("color:rgb(255, 0, 0)")
        self.info_lable.setTextFormat(QtCore.Qt.AutoText)
        self.info_lable.setObjectName("info_lable")
        self.horizontalLayout_2.addWidget(self.info_lable, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(600, 150))
        self.textEdit.setMaximumSize(QtCore.QSize(640, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.horizontalGroupBox.setMaximumSize(QtCore.QSize(640, 200))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.submit_btn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.submit_btn.setEnabled(True)
        self.submit_btn.setMinimumSize(QtCore.QSize(140, 50))
        self.submit_btn.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout.addWidget(self.submit_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.next_btn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.next_btn.setMinimumSize(QtCore.QSize(140, 50))
        self.next_btn.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.next_btn.setFont(font)
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        spacerItem2 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.horizontalGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "打字训练器"))
        self.label_2.setText(_translate("Form", "此次训练的句子为："))
        self.time_label.setText(_translate("Form", "TextLabel"))
        self.info_lable.setText(_translate("Form", "TextLabel"))
        self.submit_btn.setText(_translate("Form", "提  交"))
        self.next_btn.setText(_translate("Form", "下一句"))