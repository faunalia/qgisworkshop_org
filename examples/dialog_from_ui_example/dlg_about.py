from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DlgAbout_ui import Ui_DlgAbout

class DlgAbout(QDialog, Ui_DlgAbout):
  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)

