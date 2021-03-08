from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *

import sys
import pyttsx3

class Backend:
	def __init__(self):
		self.engine = pyttsx3.init()

	def speak(self, text, voice="male"):
		voices = self.engine.getProperty('voices')
		if voice == "male":
			self.engine.setProperty('voice', voices[0].id)
		elif voice == "female":
			self.engine.setProperty('voice', voices[1].id)
		else:
			self.engine.setProperty('voice', voices[0].id)

		self.engine.say(text)
		self.engine.runAndWait()

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Hello")

		self.engine = Backend()

		self.edit = QPlainTextEdit()

		self.speakBtn = QPushButton(text="Speak")
		self.speakBtn.clicked.connect(self.speak_text)

		self.saveBtn = QPushButton(text="Save To Mp3")
		self.saveBtn.clicked.connect(self.save_to_mp3)

		self.enter_text()

	#GUI functions
	def enter_text(self):
		layout = QVBoxLayout()
		self.setLayout(layout)

		layout.addWidget(self.edit)

		btnGroup = QHBoxLayout()
		btnGroup.addWidget(self.speakBtn)
		#btnGroup.addWidget(self.saveBtn)
		layout.addLayout(btnGroup)

	def save_to_mp3(self):
		pass

	#Backend Scripting functions
	def speak_text(self):
		text = self.edit.toPlainText()
		self.engine.speak(text)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)