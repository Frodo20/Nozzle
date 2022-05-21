import os
import PySide2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from Nozzle.nozzle import nozzle

''' def main():
    No1 = nozzle(3)
    No1.cal(0.05,0,0.2,eps=1e-5)
    #No1.cal_acu()
    No1.return_acu()
    No1.plot() '''
    
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2.QtWidgets import QApplication
from run_ui import MainWindow


if __name__ =="__main__":
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_() 

''' if __name__=="__main__":
    main() '''