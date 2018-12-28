#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
AppUI -> AppUI

Author: John Doe
Last edited: December 2018
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ui import *
from lib.core import *

class AppUI(QMainWindow):
	"""docstring for AppUI."""
	def __init__(self, parent=None):
		super(AppUI, self).__init__()
		self.title        = AppInfos.get_name() + " - " + AppInfos.get_version_tag()
		self.margin_left  = 200
		self.margin_top   = 200
		self.width        = 800
		self.height       = 600
		self.j2t 		  = JSON2Tex()
		self._initUI()

	def _initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
		self.setFixedSize(self.size())
		self.setAttribute(Qt.WA_DeleteOnClose)
		self._initMenus()
		self.show()

	def _initMenus(self):
		mainMenu = self.menuBar()
		menuFile  = mainMenu.addMenu('File')
		newFileButton = QAction('New File', self)
		newFileButton.triggered.connect(self.start_newFileWindow)
		menuFile.addAction(newFileButton)
		openFileButton = QAction('Open File', self)
		openFileButton.triggered.connect(self.start_openFileWindow)
		menuFile.addAction(openFileButton)
		menuFile.addSeparator()
		exportToJsonButton = QAction('Export To JSON', self)
		exportToJsonButton.triggered.connect(self.action_exportToJSON)
		menuFile.addAction(exportToJsonButton)
		exportToTexButton = QAction('Export To Tex', self)
		exportToTexButton.triggered.connect(self.action_exportToTex)
		menuFile.addAction(exportToTexButton)
		menuFile.addSeparator()
		exitButton = QAction('Exit', self)
		exitButton.setShortcut('Ctrl+Q')
		exitButton.setStatusTip('Exit application')
		exitButton.triggered.connect(self.close)
		menuFile.addAction(exitButton)

		menuEdit  = mainMenu.addMenu('Edit')
		sortASC_Button = QAction('Sort data ASC', self)
		sortASC_Button.triggered.connect(self.action_sortdataASC)
		menuEdit.addAction(sortASC_Button)
		sortDESC_Button = QAction('Sort data DESC', self)
		sortDESC_Button.triggered.connect(self.action_sortdataDESC)
		menuEdit.addAction(sortDESC_Button)

# *------------------------------Windows Handlers----------------------------- *

	def start_newFileWindow(self):
		self.wnewFileWindow = newFileWindow()
		self.wnewFileWindow.show()

	def start_openFileWindow(self):
		self.wopenFileWindow = openFileWindow()
		self.wopenFileWindow.show()

# *------------------------------Actions Handlers----------------------------- *

	def action_sortdataASC(self):
		self.j2t.sortData("ASC")

	def action_sortdataDESC(self):
		self.j2t.sortData("DESC")

	def action_exportToTex(self):
		pass

	def action_exportToJSON(self):
		pass




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = AppUI()
	sys.exit(app.exec_())
