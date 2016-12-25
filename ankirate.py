# import the main window object (mw) from aqt
from aqt import mw
#import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

def rateFunction():
    # display message box
    showInfo("action happened")

# create menu item
action = QAction("ankiRate", mw)
# make it call rateFunction
action.triggered.connect(rateFunction)
# add item to tools menu
mw.form.menuTools.addAction(action)
