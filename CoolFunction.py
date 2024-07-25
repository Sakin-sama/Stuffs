import sys, random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import numpy as np

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



class AppForm(QMainWindow):
  def __init__(self,parent=None):
    QMainWindow.__init__(self, parent)
    self.setWindowTitle('Demo: PyQt with matplotlib')

    self.create_menu()
    self.create_main_frame()
    self.create_status_bar()

    # self.textbox.setText('1 2 3 4')

    self.on_draw()

  def save_plot(self):
    file_choices = "PNG (*.png) |*.png"

    path, ext, = QFileDialog.getSaveFileName(self,'Save file','',file_choices)
    path = path.encode('utf-8')
    if not path[-4] == file_choices[-4:].encode('utf-8'):
      path += file_choices[-4:].encode('utf-8')
    print(path)
    if path:
      self.canvas.print_figure(path.decode(),dpi = self.dpi)
      self.statusBar().showMessage('saved to %s' % path,2000)

  def on_about(self):
    msg = QMessageBox.about(self, "about the demo",msg.strip())

  def on_pick(self, event):

    box_points = event.artist.getbbox().getpoints()
    msg = "You've clicked on a bar with coords:\n %s" %box_points
    QMessageBox.information(self, "CLICK!", msg)

  def on_draw(self):
    self.axes.clear()


    
       

    self.slide1_value.setText(f'{self.slider1.value()/1000}')
    self.slide2_value.setText(f'{self.slider2.value()/1000}')

    self.axes.grid(self.grid_cb.isChecked())

    if self.textbox.text():
      r = np.linspace(0, float(self.textbox.text()) * np.pi, 1000)
    else:
      r = np.linspace(0, np.pi, 1000)


    a = self.slider1.value() / 1000
    b = self.slider2.value() / 1000

    x1 = np.sin(r * b)
    y1 = np.cos(r * a)

    self.axes.plot(x1,y1,'k')
    self.canvas.draw()

  def randomize(self):
    self.slider1.setValue(round(random.uniform(0,1000)))
    self.slider2.setValue(round(random.uniform(0,1000)))
    self.textbox.setText(str(round(random.uniform(1,100))))

  def create_main_frame(self):
    self.main_frame = QWidget()
    font_var = QFont("PT Mono")
    self.dpi = 100
    self.fig = Figure((5,4),dpi = self.dpi)
    self.canvas = FigureCanvas(self.fig)
    self.canvas.setParent(self.main_frame)

    self.axes = self.fig.add_subplot(111)

    self.canvas.mpl_connect('pick_event',self.on_pick)

    self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

    self.grid_cb = QCheckBox("Show &Grid")
    self.grid_cb.setChecked(False)
    self.grid_cb.stateChanged.connect(self.on_draw)

    self.slider2_label = QLabel('sin val:')
    self.slider2 = QSlider(Qt.Horizontal)
    self.slider2.setRange(0,1000)
    self.slider2
    self.slider2.setValue(1000)
    self.slider2.setTracking(True)
    self.slider2.valueChanged.connect(self.on_draw)
    self.slide2_value = QLabel("1000")
    self.slide2_value.setMinimumWidth(50)
    self.slide2_value.setFont(font_var)
    # self.slider2.sliderMoved.connect(self.on_slider2_moved)
  
    # fonts = QFontDatabase()
    # names = fonts.families()
    # print(names) 
    self.random_button = QPushButton("&Randomize")
    self.random_button.clicked.connect(self.randomize)
    self.random_button.clicked.connect(self.on_draw)
    
    slider_label1 = QLabel('cos val:')
    self.slider1 = QSlider(Qt.Horizontal)

    self.slider1.setRange(0,1000)
    self.slider1
    self.slider1.setValue(1000)
    self.slider1.setTracking(True)
    self.slider1.valueChanged.connect(self.on_draw)
    self.slide1_value = QLabel("1000")
    self.slide1_value.setMinimumWidth(50)
    self.slide1_value.setFont(font_var)
    # self.slider1.sliderMoved.connect(self.on_slider1_moved)
    
    self.textlabel = QLabel("number of x values to input in the functions for f(x)")

    self.textbox = QLineEdit()
    # self.textbox.setMinimumWidth(25)
    # self.textbox.setMaximumWidth()
    self.textbox.textChanged.connect(self.on_draw)
    self.textbox.setText("8")

    hbox = QHBoxLayout()
    hbox2 = QHBoxLayout()


    for w in [self.grid_cb, self.slider2_label,self.slide2_value,
              self.slider2, slider_label1, self.slide1_value, self.slider1]:
      hbox.addWidget(w)
      hbox.setAlignment(w,Qt.AlignVCenter)

    for c in [self.textlabel,self.textbox, self.random_button]:
       hbox2.addWidget(c)
       hbox2.setAlignment(c,Qt.AlignVCenter)

    vbox = QVBoxLayout()
    vbox.addWidget(self.canvas)
    vbox.addWidget(self.mpl_toolbar)
    vbox.addLayout(hbox)
    vbox.addLayout(hbox2)




    self.main_frame.setLayout(vbox)
    self.setCentralWidget(self.main_frame)

  def create_status_bar(self):
      self.status_text = QLabel("It works?")
      self.statusBar().addWidget(self.status_text,1)

  def create_menu(self):
      self.file_menu = self.menuBar().addMenu("&file")

      load_file_action = self.create_action("&Save plot",
            shortcut="Ctrl+S",slot=self.save_plot,
            tip="save the plot")
      quit_action = self.create_action("&Quit", slot=self.close,
                                        shortcut="Ctrl+Q", tip="Close the application")
      self.add_actions(self.file_menu,
                        (load_file_action,None,quit_action))
      self.help_menu = self.menuBar().addMenu("&Help")
      about_action = self.create_action("&About",
                                            shortcut='F1', slot=self.on_about,
                                            tip='About the demo')
      self.add_actions(self.help_menu, (about_action,))

  def add_actions(self,target,actions):
      for action in actions:
          if action is None:
                target.addSeparator()
          else:
                target.addAction(action)


  def create_action(  self, text, slot=None, shortcut=None, 
                    icon=None, tip=None, checkable=False):
      action = QAction(text, self)
      if icon is not None:
          action.setIcon(QIcon(":/%s.png" % icon ))
      if shortcut is not None:
          action.setShortcut(shortcut)
      if tip is not None:
          action.setToolTip(tip)
          action.setStatusTip(tip)
      if slot is not None:
          action.triggered.connect(slot)
      if checkable:
          action.setCheckable(True)
      return action

def main():
  app = QApplication(sys.argv)
  form = AppForm()
  form.show()
  app.exec_()

    






if __name__ == "__main__":
  main()