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
		self._initUI()

	def _initUI(self):
		self.setWindowTitle(self.title)
		#self.setWindowIcon(QIcon('lib/meta/ico.png'))
		self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
		self.setFixedSize(self.size())
		self.setAttribute(Qt.WA_DeleteOnClose)
		self._initMenus()
		self.show()

	def _initMenus(self):
		mainMenu = self.menuBar()
		menuFichier  = mainMenu.addMenu('Fichier')
		nouveaufichierButton = QAction('Nouveau fichier', self)
		nouveaufichierButton.triggered.connect(self.start_nouveaufichierWindow)
		menuFichier.addAction(nouveaufichierButton)
		ouvrirunfichierButton = QAction('Ouvrir un Fichier', self)
		ouvrirunfichierButton.triggered.connect(self.start_ouvrirunfichierWindow)
		menuFichier.addAction(ouvrirunfichierButton)
		menuFichier.addSeparator()
		exitButton = QAction('Exit', self)
		exitButton.setShortcut('Ctrl+Q')
		exitButton.setStatusTip('Exit application')
		exitButton.triggered.connect(self.close)
		menuFichier.addAction(exitButton)

# *------------------------------Windows Handlers----------------------------- *

	def start_nouveaufichierWindow(self):
		self.wnouveaufichierWindow = nouveaufichierWindow()
		self.wnouveaufichierWindow.show()

	def start_ouvrirunfichierWindow(self):
		self.wouvrirunfichierWindow = ouvrirunfichierWindow()
		self.wouvrirunfichierWindow.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = AppUI()
	sys.exit(app.exec_())
