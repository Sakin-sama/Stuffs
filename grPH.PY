import sys, os, random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

    self.textbox.setText('1 2 3 4')
    self.on_draw()

  def save_plot(self):
    file_choices = "PNG (*.png) |*.png"

    path, ext, = QFileDialog.getSaveFileName(self,'Save         file','',file_choices)
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
    str = self.textbox.text().encode('utf-8')
    self.data = [int(s) for s in str.split()]

    x = range(len(self.data))
    self.axes.clear()
    self.axes.grid(self.grid_cb.isChecked())

    self.axes.bar(
      x=x,
      height=self.data,
      width=self.slider.value()/100.0,
      align='center',
      alpha=0.44,
      picker=5)
    self.canvas.draw()

  def create_main_frame(self):
    self.main_frame = QWidget()

    self.dpi = 100
    self.fig = Figure((5,4),dpi = self.dpi)
    self.canvas = FigureCanvas(self.fig)
    self.canvas.setParent(self.main_frame)

    self.axes = self.fig.add_subplot(111)

    self.canvas.mpl_connect('pick_event',self.on_pick)

    self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

    self.textbox = QLineEdit()
    self.textbox.setMinimumWidth(200)
    self.textbox.editingFinished.connect(self.on_draw)

    self.draw_button = QPushButton("&Draw")
    self.draw_button.clicked.connect(self.on_draw)
    
    self.grid_cb = QCheckBox("Show &Grid")
    self.grid_cb.setChecked(False)
    self.grid_cb.stateChanged.connect(self.on_draw)

    slider_label = QLabel('Bar width (%):')
    self.slider = QSlider(Qt.Horizontal)
    self.slider.setRange(1,100)
    self.slider.setValue(20)
    self.slider.setTracking(True)
    self.slider.setTickPosition(QSlider.TicksBothSides)
    self.slider.valueChanged.connect(self.on_draw)

    hbox = QHBoxLayout()

    for w in [self.textbox, self.draw_button, self.grid_cb,
               slider_label, self.slider]:
      hbox.addWidget(w)
      hbox.setAlignment(w,Qt.AlignVCenter)

    vbox = QVBoxLayout()
    vbox.addWidget(self.canvas)
    vbox.addWidget(self.mpl_toolbar)
    vbox.addLayout(hbox)

    self.main_frame.setLayout(vbox)
    self.setCentralWidget(self.main_frame)

  def create_status_bar(self):
      self.status_text = QLabel("This is a demo")
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

    





# x = np.linspace(0, 8 * np.pi, 1000)

# a = np.random.rand()
# b = np.random.rand()


# y = np.sin(x*b)
# z = np.cos(x*a)


# plt.plot(y,z,'k')
# plt.axis('square')
# plt.axis([-1.1,1.1,-1.1,1.1])
# plt.axis('off')
# plt.title('a=%s,b=%s' %(np.round(a,2),np.round(b,2)))

# plt.show()


if __name__ == "__main__":
  main()