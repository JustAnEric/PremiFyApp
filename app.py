import webview, webbrowser#, tkinterweb.tkhtml
from urllib import request
#from tkinterweb import HtmlFrame
#from tkinterhtml import HtmlFrame
#from tkinter import messagebox
#import tkinter as tk
from io import StringIO as strio

#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)
        self.setWindowTitle('PremiFy')
        self.show()

    def loadPage(self):
        url = QUrl.fromUserInput(str("https://p.justaneric.co/open"))
        #with open('test.html', 'r') as f:

            #html = f.read()
        self.webEngineView.load(url)
        self.webEngineView.setZoomFactor(1.5)

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()