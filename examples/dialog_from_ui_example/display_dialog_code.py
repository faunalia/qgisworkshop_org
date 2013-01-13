### How to load a dialog generated from a .ui file?
### This code is just for testing purpose!
###
### If you want to run this code from QGis Python Console you have to
### set up PYTHONPATH so it can find this module by running

#>>> # insert the module dirpath into PYTHONPATH (e.g. /home/brushtyler/display_from_ui_example/)
#>>> import sys
#>>> sys.path.insert(0, "/home/brushtyler/display_from_ui_example")


### 1. create a new module dlg_about containing the DlgAbout class 
###    (have a look at dlg_about.py)

# import pyqt4 classes
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import the class generated from .ui
from DlgAbout_ui import Ui_DlgAbout

# define the DlgAbout class
class DlgAbout(QDialog, Ui_DlgAbout):
  def __init__(self):
    # call the parent QDialog class constructor
    QDialog.__init__(self)
    # call setupUi defined in the Ui_DlgAbout class
    self.setupUi(self)


### 2. instanziate an DlgAbout dialog and then display it

# create an instance of the dialog and run it
dlg = DlgAbout()
dlg.exec_()

