# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cuerpa.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui

def estilo(ventana):
	ventana.setStyleSheet("""
	

	

	/* Style the tab using the tab sub-control. Note that
		it reads QTabBar _not_ QTabWidget */
	QTabBar::tab {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
									stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
		border: 2px solid #C4C4C3;
		border-bottom-color: #C2C7CB; /* same as the pane color */
		border-top-left-radius: 4px;
		border-top-right-radius: 4px;
		min-width: 8ex;
		padding: 2px;
		width: 100px;
	}

	QTabBar::tab:selected, QTabBar::tab:hover {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #fafafa, stop: 0.4 #f4f4f4,
									stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
	}

	QTabBar::tab:selected {
		border-color: #9B9B9B;
		border-bottom-color: #C2C7CB; /* same as pane color */
	}

	QTabBar::tab:!selected {
		margin-top: 2px; /* make non-selected tabs look smaller */
	}

	/* make use of negative margins for overlapping tabs */
	QTabBar::tab:selected {
		/* expand/overlap to the left and right by 4px */
		margin-left: -4px;
		margin-right: -4px;
	}

	QTabBar::tab:first:selected {
		margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
	}

	QTabBar::tab:last:selected {
		margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
	}

	QTabBar::tab:only-one {
		margin: 0; /* if there is only one tab, we don't want overlapping margins */
	}
	""")

def estilo2(ventana):
	ventana.setStyleSheet("""
	QListWidget {
    show-decoration-selected: 1; /* make the selection span the entire width of the view */
	}

	QListWidget::item:alternate {
		background: #EEEEEE;
	}

	QListWidget::item:selected {
		border: 1px solid #6a6ea9;
	}

	QListWidget::item:selected:!active {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #ABAFE5, stop: 1 #8588B2);
	}

	QListWidget::item:selected:active {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #6a6ea9, stop: 1 #888dd9);
	}

	QListWidget::item:hover {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #FAFBFE, stop: 1 #DCDEF1);
	}
	
	""")

class QCustomQWidget (QtWidgets.QWidget):
	def __init__ (self, parent = None):
		super(QCustomQWidget, self).__init__(parent)
		self.textQVBoxLayout = QtWidgets.QVBoxLayout()
		self.textUpQLabel    = QtWidgets.QLabel()
		self.textDownQLabel  = QtWidgets.QLabel()
		self.textQVBoxLayout.addWidget(self.textUpQLabel)
		self.textQVBoxLayout.addWidget(self.textDownQLabel)
		self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
		self.iconQLabel      = QtWidgets.QLabel()
		self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
		self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
		self.setLayout(self.allQHBoxLayout)
		# setStyleSheet
		self.textUpQLabel.setStyleSheet('''
		color: rgb(0, 0, 255);
		''')
		self.textDownQLabel.setStyleSheet('''
		color: rgb(255, 0, 0);
		''')

	def setTextUp (self, text):
		self.textUpQLabel.setText(text)

	def setTextDown (self, text):
		self.textDownQLabel.setText(text)

	def setIcon (self, imagePath):
		icon = QtGui.QPixmap()
		icon.load(imagePath)
		self.iconQLabel.setPixmap(icon)

class Ui_Form(object):
	def setupUi(self, Form):
	
		Form.setObjectName("Principal")
		Form.setFixedSize(521, 469)
		Form.setWindowTitle("Pollos ChatRoom")
		
		self.text = QtWidgets.QApplication.clipboard().text()
		QtWidgets.QApplication.clipboard().dataChanged.connect(lambda: self.actionPegar.setEnabled(True))
		
		self.tabWidget = QtWidgets.QTabWidget(Form)
		self.tabWidget.setGeometry(QtCore.QRect(15, 20, 491, 441))
		self.tabWidget.setObjectName("tabWidget")
		estilo(self.tabWidget)
		
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("Sala_Default")
		
		############################################################################################
		self.textEdit = QtWidgets.QTextEdit(self.tab)
		self.textEdit.setGeometry(QtCore.QRect(30, 10, 321, 331))
		self.textEdit.setObjectName("textEdit")
		self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.textEdit.customContextMenuRequested.connect(self.menuContextualQTextEdit)
		self.textEdit.setReadOnly(True)
		self.accionesQTextEdit()
		self.textEdit.selectionChanged.connect(self.verificarQTextEdit)
		self.textEdit.textChanged.connect(self.verificarQTextEdit)
		#################################################################################################
		
		self.pushButton = QtWidgets.QPushButton(self.tab)
		self.pushButton.setGeometry(QtCore.QRect(400, 360, 61, 21))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Enviar")
		self.pushButton.clicked.connect(self.send)
		
		###################################################################
		self.lineEdit = QtWidgets.QLineEdit(self.tab)
		self.lineEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.lineEdit.customContextMenuRequested.connect(self.menuContextualQLineEdit)
		self.lineEdit.setGeometry(QtCore.QRect(30, 350, 321, 41))
		self.lineEdit.setObjectName("lineEdit")
		self.accionesQLineEdit()
		self.lineEdit.returnPressed.connect(self.pushButton.click)
		self.lineEdit.textChanged.connect(self.verificarQLineEdit)
		self.lineEdit.mouseReleaseEvent = self.eventoMouseQLineEdit
		
		######################################################################
		
		self.pushButton_2 = QtWidgets.QPushButton(self.tab)
		self.pushButton_2.setGeometry(QtCore.QRect(360, 360, 21, 21))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.setIcon(QtGui.QIcon('adjunto.png'))
		self.pushButton_2.setIconSize(QtCore.QSize(20,20))
		self.pushButton_2.setStyleSheet('QPushButton{border: 0px solid;}')
		self.pushButton_2.clicked.connect(self.openFileNameDialog)
		
		self.tabWidget.addTab(self.tab, "Sala_Default")
		
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		
		self.tabWidget.addTab(self.tab_2, "")

		menu = QtWidgets.QMenu()
		
		exitAction = QtWidgets.QAction(QtGui.QIcon('editar.png'), '&Editar Cuenta', self.tab)        
		exitAction.triggered.connect(self.send)
		
		action_b = QtWidgets.QAction(QtGui.QIcon('eliminar.png'), '&Eliminar Cuenta', self.tab)
		action_b.triggered.connect(self.send)
		
		action_c = QtWidgets.QAction(QtGui.QIcon('cerrar.png'), '&Cerrar Sesión\tCTRL + Q', self.tab)
		action_c.setShortcut('CTRL+Q')
		action_c.triggered.connect(self.send)
		
		action_d = QtWidgets.QAction(QtGui.QIcon('salir.png'), '&Salir\tALT + F4', self.tab)
		action_d.setShortcut('ALT+F2')
		action_d.triggered.connect(self.send)
		
		menu.addAction(exitAction)
		menu.addAction(action_b)
		menu.addAction(action_c)
		menu.addAction(action_d)
		
		self.toolButton = QtWidgets.QPushButton(Form)
		self.toolButton.setGeometry(QtCore.QRect(477, 5, 29, 29))
		self.toolButton.setObjectName("Opciones")
		self.toolButton.setIcon(QtGui.QIcon('opciones.png'))
		self.toolButton.setIconSize(QtCore.QSize(25, 25))
		self.toolButton.setMenu(menu)
		#self.toolButton.setStyleSheet('border: 0px solid;')
		
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(240, 10, 100, 13))
		self.label.setObjectName("Usuario")
		self.label.setText("Bienvenide asjajsj")

		self.label2 = QtWidgets.QLabel(self.tab)
		self.label2.setGeometry(QtCore.QRect(380, 380, 50, 20))
		self.label2.setText("Cancelar")
		self.label2.mouseReleaseEvent = self.ensayo
		self.label2.hide()
		"""
		self.list = QtWidgets.QListView(self.tab)
		#list.MultiSelec(False)
		self.list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.list.setWindowTitle('Example List')
		self.list.resize(120, 331)
		self.list.move(358,10)
		estilo2(self.list)
		model = QtGui.QStandardItemModel(self.list)
		foods = [
		'Cookie dough', 'A'# Must be store-bought
		'Hummus', # Must be homemade
		'Spaghetti', # Must be saucy
		'Dal makhani', # Must be spicy
		'Chocolate whipped cream' # Must be plentiful
		]

		for food in foods:
		# Create an item with a caption
			item = QtGui.QStandardItem(food)
			model.appendRow(item)
		self.list.setModel(model)
		self.list.clicked.connect(self.printi)
		
		"""
		self.list2 = QtWidgets.QListView(self.tab)
		#list.MultiSelec(False)
		self.list2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		#self.list2.setWindowTitle('Example List')
		self.list2.setFixedSize(321, 65.5)
		#self.textEdit.resize(321, 265.5)
		self.list2.move(30,276.5)
		model2 = QtGui.QStandardItemModel(self.list2)
		foods2 = [
		'Cookie dough', 'A'# Must be store-bought
		'Hummus', # Must be homemade
		'Spaghetti', # Must be saucy
		'Dal makhani', # Must be spicy
		'Chocolate whipped cream' # Must be plentiful
		]
		for food2 in foods2:
		# Create an item with a caption
			item2 = QtGui.QStandardItem(food2)
			model2.appendRow(item2)
		self.list2.setModel(model2)
		self.list2.clicked.connect(self.si)
		self.list2.hide()
		
		self.label3 = QtWidgets.QLabel(self.tab)
		self.label3.setGeometry(QtCore.QRect(378, 10, 100, 20))
		self.label3.setText("Miembros de la sala")
		
		self.myQListWidget = QtWidgets.QListWidget(self.tab)
		for index, name, icon in [
			('No.1', 'Meyoko',  'man.png'),
			('No.2', 'Nyaruko', 'woman.png'),
			('No.3', 'Louise',  'man.png')]:
			# Create QCustomQWidget
			myQCustomQWidget = QCustomQWidget()
			myQCustomQWidget.setTextUp(index)
			myQCustomQWidget.setTextDown(name)
			myQCustomQWidget.setIcon(icon)
			# Create QListWidgetItem
			myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)
			myQListWidgetItem.dato=name
			# Set size hint
			myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
			# Add QListWidgetItem into QListWidget
			self.myQListWidget.addItem(myQListWidgetItem)
			self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
		self.myQListWidget.resize(120, 280)
		self.myQListWidget.move(358,30)
		estilo2(self.myQListWidget)
		self.myQListWidget.itemClicked.connect(self.printi)
		self.myQListWidget.show()
		
		self.toolButton2 = QtWidgets.QPushButton(self.tab)
		self.toolButton2.setGeometry(QtCore.QRect(405, 315, 25, 25))
		self.toolButton2.setObjectName("Opciones2")
		self.toolButton2.setIcon(QtGui.QIcon('opciones.png'))
		self.toolButton2.setIconSize(QtCore.QSize(21, 21))
		self.toolButton2.setMenu(menu)
		
	def printi(self):
		print(self.myQListWidget.currentItem().dato)
		self.myQListWidget.takeItem(self.myQListWidget.currentRow())
		
	
	def accionesQLineEdit(self):
		self.actionCortar = QtWidgets.QAction(QtGui.QIcon('accioncortar.png'), '&Cortar\tCTRL+X', self.lineEdit)
		#self.actionCortar.triggered.connect(lambda: pyautogui.hotkey('ctrl','x'))
		self.actionCortar.setEnabled(False)
		
		self.actionCopiar = QtWidgets.QAction(QtGui.QIcon('accioncopiar.png'), '&Copiar\tCTRL+C', self.lineEdit)
		self.actionCopiar.triggered.connect(lambda: pyautogui.hotkey('ctrl','c'))
		self.actionCopiar.setEnabled(False)
	
		self.actionPegar = QtWidgets.QAction(QtGui.QIcon('accionpegar.png'), '&Pegar\tCTRL+V', self.lineEdit)
		self.actionPegar.triggered.connect(lambda: pyautogui.hotkey('ctrl','v'))
		if len(self.text):
			self.actionPegar.setEnabled(True)
		else:
			self.actionPegar.setEnabled(False)
	
		self.actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A', self.lineEdit)
		self.actionSeleccionarTodo.triggered.connect(lambda: pyautogui.hotkey('ctrl','a'))
		self.actionSeleccionarTodo.setEnabled(False)
		
		self.actionEliminar = QtWidgets.QAction(QtGui.QIcon('accionborrar.png'), '&Eliminar', self.lineEdit)
		self.actionEliminar.triggered.connect(lambda:pyautogui.press('backspace'))
		self.actionEliminar.setEnabled(False)
		
		self.lineEdit.addAction(self.actionCortar)
		self.lineEdit.addAction(self.actionCopiar)
		self.lineEdit.addAction(self.actionPegar)
		self.lineEdit.addAction(self.actionSeleccionarTodo)
		self.lineEdit.addAction(self.actionEliminar)
		
	def verificarQLineEdit(self):
		if len(self.lineEdit.text()) == 0:
			self.actionCortar.setEnabled(False)
			self.actionCopiar.setEnabled(False)
			self.actionEliminar.setEnabled(False)
			self.actionSeleccionarTodo.setEnabled(False)
			self.list2.hide()
			self.textEdit.resize(321, 331)
		else:
			self.actionSeleccionarTodo.setEnabled(True)
			if '@' in self.lineEdit.text():
				if len(self.lineEdit.text()) == 1:
					self.list2.show()
					self.textEdit.resize(321, 262.5)
					
				else:
					texto = self.lineEdit.text().split(' ')
					ultimo_elemento = texto[-1]
					if '@' in self.lineEdit.text()[-1]:
						if ultimo_elemento.count('@') == len(ultimo_elemento):
							self.list2.show()
							self.textEdit.resize(321, 262.5)
							
						else:
							self.list2.hide()
							self.textEdit.resize(321, 331)
							
					elif ' ' in self.lineEdit.text()[-1]:
						self.list2.hide()
						self.textEdit.resize(321, 331)
						
			else:
				self.list2.hide()
				self.textEdit.resize(321, 331)
				
	
	def menuContextualQLineEdit(self):
		"""self._normalMenu = QtWidgets.QMenu()
		if self.lineEdit.selectionStart() != -1:
			self.actionCortar.setEnabled(True)
			self.actionCopiar.setEnabled(True)
			self.actionEliminar.setEnabled(True)
		else:
			self.actionCortar.setEnabled(False)
			self.actionCopiar.setEnabled(False)
			self.actionEliminar.setEnabled(False)
		self._normalMenu.addAction(self.actionCortar)
		self._normalMenu.addAction(self.actionCopiar)
		self._normalMenu.addAction(self.actionPegar)
		self._normalMenu.addAction(self.actionSeleccionarTodo)
		self._normalMenu.addAction(self.actionEliminar)
		self._normalMenu.exec_(QtGui.QCursor.pos())"""
		
		"""
		self.cb = QtWidgets.QComboBox(self.tab)
		self.cb.addItem("C")
		self.cb.addItem("C++")
		self.cb.addItems(["Java", "C#", "Python"])
		self.cb.currentIndexChanged.connect(self.si)
		self.cb.setFixedSize(321,65.5)
		self.cb.move(30,276.5)
		self.cb.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.cb.show()
		"""
	
		
	def eventoMouseQLineEdit(self, event):
		if self.lineEdit.selectionStart() != -1:
			self.actionCortar.setEnabled(True)
			self.actionCopiar.setEnabled(True)
			self.actionEliminar.setEnabled(True)
		else:
			self.actionCortar.setEnabled(False)
			self.actionCopiar.setEnabled(False)
			self.actionEliminar.setEnabled(False)

	def accionesQTextEdit(self):
		self.actionCopiar2 = QtWidgets.QAction(QtGui.QIcon('accioncopiar.png'), '&Copiar', self.textEdit)
		self.actionCopiar2.triggered.connect(lambda:pyautogui.hotkey('ctrl','c'))
		self.actionCopiar2.setEnabled(False)
		
		self.actionSeleccionarTodo2 = QtWidgets.QAction(QtGui.QIcon('accionseleccionar.png'), '&Seleccionar Todo', self.textEdit)
		self.actionSeleccionarTodo2.triggered.connect(self.textEdit.selectAll)
		self.actionSeleccionarTodo2.setEnabled(False)

	def verificarQTextEdit(self):
		cursor = self.textEdit.textCursor()
		text = self.textEdit.toPlainText()
		if len(text):
			self.actionSeleccionarTodo2.setEnabled(True)
		else:
			self.actionSeleccionarTodo2.setEnabled(False)
		if cursor.selectionStart() - cursor.selectionEnd() == 0:
			self.actionCopiar2.setEnabled(False)
		else:
			self.actionCopiar2.setEnabled(True)
		if cursor.selectionEnd() - cursor.selectionStart() == len(text):
			self.actionSeleccionarTodo2.setEnabled(False)
		else:
			self.actionSeleccionarTodo2.setEnabled(True)
	
	def menuContextualQTextEdit(self):
		self.menucontextualQText = QtWidgets.QMenu()
		self.menucontextualQText.addAction(self.actionCopiar2)
		self.menucontextualQText.addAction(self.actionSeleccionarTodo2)
		self.menucontextualQText.exec_(QtGui.QCursor.pos())
	
	
	def send(self):
		"""texto = self.lineEdit.text()
		self.textEdit.append(texto)
		print("me envié")"""
		self.ensayo = NewDialog(Form)
		self.ensayo.show()
	
	def ensayo(self, event):
		self.fileName = None
		self.pushButton_2.setEnabled(True)
		self.lineEdit.setText("")
		self.lineEdit.setEnabled(True)
		self.label2.hide()
	

	def openFileNameDialog(self):    
		options = QtWidgets.QFileDialog.Options()
		self.label2.hide()
		#options |= QtWidgets.QFileDialog.DontUseNativeDialog
		self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.tab,"Selecciona un archivo adjunto", "","Todos los archivos (*)", options=options)
		if self.fileName:
			self.pushButton_2.setEnabled(False)
			self.lineEdit.setText("")
			self.lineEdit.setEnabled(False)
			self.label2.show()
			print(self.fileName)

	def si(self):
		print("si")
	
class NewDialog(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(NewDialog, self).__init__(parent)
		self.setParent(None)
		self.setFixedSize(200,200)
		self.setObjectName("Principal")
		self.setFixedSize(521, 469)
		self.setWindowTitle("Pollos ChatRoom")

		

	
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

