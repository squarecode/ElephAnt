# Form implementation generated from reading ui file 'ElephAnt.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ElephAnt(object):
    def setupUi(self, ElephAnt):
        ElephAnt.setObjectName("ElephAnt")
        ElephAnt.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        ElephAnt.resize(931, 610)
        ElephAnt.setMinimumSize(QtCore.QSize(800, 600))
        ElephAnt.setLocale(QtCore.QLocale(QtCore.QLocale.Language.German, QtCore.QLocale.Country.Germany))
        self.centralwidget = QtWidgets.QWidget(parent=ElephAnt)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setStatusTip(0, "")
        self.treeWidget.header().setDefaultSectionSize(256)
        self.treeWidget.header().setMinimumSectionSize(256)
        self.treeWidget.header().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_general)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_general)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.tb_setup_name = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.tb_setup_name.setObjectName("tb_setup_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_setup_name)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.tb_setup_comment = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.tb_setup_comment.setObjectName("tb_setup_comment")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_setup_comment)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.l_last_modified = QtWidgets.QLabel(parent=self.groupBox_2)
        self.l_last_modified.setObjectName("l_last_modified")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l_last_modified)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab_general)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.tb_aut_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.tb_aut_name.setObjectName("tb_aut_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_aut_name)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_hwSetup = QtWidgets.QWidget()
        self.tab_hwSetup.setObjectName("tab_hwSetup")
        self.tabWidget.addTab(self.tab_hwSetup, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.setStretch(1, 6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.logDisplayArea = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.logDisplayArea.setFont(font)
        self.logDisplayArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.logDisplayArea.setReadOnly(True)
        self.logDisplayArea.setPlainText("")
        self.logDisplayArea.setObjectName("logDisplayArea")
        self.verticalLayout_3.addWidget(self.logDisplayArea)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        ElephAnt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ElephAnt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        ElephAnt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ElephAnt)
        self.statusbar.setObjectName("statusbar")
        ElephAnt.setStatusBar(self.statusbar)
        self.actionOpen_Setup = QtGui.QAction(parent=ElephAnt)
        self.actionOpen_Setup.setObjectName("actionOpen_Setup")
        self.actionNew_Setup = QtGui.QAction(parent=ElephAnt)
        self.actionNew_Setup.setObjectName("actionNew_Setup")
        self.actionSave_Setup = QtGui.QAction(parent=ElephAnt)
        self.actionSave_Setup.setObjectName("actionSave_Setup")
        self.actionExit = QtGui.QAction(parent=ElephAnt)
        self.actionExit.setObjectName("actionExit")
        self.actionClose_Setup = QtGui.QAction(parent=ElephAnt)
        self.actionClose_Setup.setObjectName("actionClose_Setup")
        self.actionSave_Setup_As = QtGui.QAction(parent=ElephAnt)
        self.actionSave_Setup_As.setObjectName("actionSave_Setup_As")
        self.menuFile.addAction(self.actionNew_Setup)
        self.menuFile.addAction(self.actionOpen_Setup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Setup)
        self.menuFile.addAction(self.actionSave_Setup_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Setup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ElephAnt)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ElephAnt)

    def retranslateUi(self, ElephAnt):
        _translate = QtCore.QCoreApplication.translate
        ElephAnt.setWindowTitle(_translate("ElephAnt", "ElephAnt - Trunkloads of Power for Antenna Measurements"))
        self.treeWidget.headerItem().setText(0, _translate("ElephAnt", "Setup List"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("ElephAnt", "New Setup"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("ElephAnt", "Setup Information"))
        self.label_2.setText(_translate("ElephAnt", "Setup Name"))
        self.label_3.setText(_translate("ElephAnt", "Comment"))
        self.label_4.setText(_translate("ElephAnt", "Last Modified"))
        self.l_last_modified.setText(_translate("ElephAnt", "---"))
        self.groupBox.setTitle(_translate("ElephAnt", "AUT Information"))
        self.label_6.setText(_translate("ElephAnt", "AUT Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("ElephAnt", "General Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hwSetup), _translate("ElephAnt", "Hardware Setup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ElephAnt", "Tab 2"))
        self.label.setText(_translate("ElephAnt", "Log Output:"))
        self.menuFile.setTitle(_translate("ElephAnt", "File"))
        self.actionOpen_Setup.setText(_translate("ElephAnt", "Open Setup"))
        self.actionNew_Setup.setText(_translate("ElephAnt", "New Setup"))
        self.actionSave_Setup.setText(_translate("ElephAnt", "Save Setup"))
        self.actionExit.setText(_translate("ElephAnt", "Exit"))
        self.actionClose_Setup.setText(_translate("ElephAnt", "Close Setup"))
        self.actionSave_Setup_As.setText(_translate("ElephAnt", "Save Setup As ..."))
