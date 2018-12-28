#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
NewApp -> ouvrirunfichierWindow

Author: John Doe
Last edited: December 2018
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ui import *
from lib.core import *

class ouvrirunfichierWindow(QWidget):
	def __init__(self, parent=None):
		super(ouvrirunfichierWindow, self).__init__()
		self.title = 'ouvrirunfichierWindow'
		self.marginleft = 0
		self.margintop  = 0
		self.width      = 300
		self.height     = 200
		self._initUI()
		self.show()

	def _initUI(self):
		self.setWindowTitle(self.title)
		self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
		self.setGeometry(self.marginleft, self.margintop, self.width, self.height)
		self.label = QLabel("<b>" + NewAppInfos.get_name() + " " + NewAppInfos.get_version() + " </b><br><br>" + NewAppInfos.get_credits(), self)
		self.label.setAlignment(Qt.AlignCenter)
		self.layout = QGridLayout()
		self.layout.addWidget(self.label, 0, 0)
		self.setLayout(self.layout)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = ouvrirunfichierWindow()
	sys.exit(app.exec_())
