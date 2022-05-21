# -*- coding: utf-8 -*-

import os
from re import S
from turtle import up
import PySide2
import sys
import pandas as pd

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from PySide2.QtUiTools import QUiLoader
import matplotlib
matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PySide2.QtGui import QDoubleValidator, QIntValidator

import numpy as np
from Nozzle.nozzle import nozzle
import matplotlib.animation as animation  
import imageio
from PIL import Image, ImageSequence
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel,QWidget
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        #self.ui=Ui_GUI()
        self.ui.setupUi(self)
        self.setWindowTitle('可压缩流体喷管问题')
        #self.resize(640, 780)
        # self.ui.resize(1200,1200)
        self.fig1 = plt.figure(figsize=(10,6),dpi=80)
        axis1 = self.fig1.add_subplot(1,1,1)  # Prep empty plot
        self.fig2 = plt.figure(figsize=(10,6),dpi=80)
        axis2 = self.fig2.add_subplot(1,1,1)
        self.initialize_figure(self.fig1, axis1, self.fig2, axis2)
        self.init_event()
        self.init_para()
        #self.change_plot()
        
    def init_event(self):
        self.doubleOnly=QDoubleValidator() # 限制输入为浮点数
        self.intOnly=QIntValidator() # 限制输入为整型数
        
        self.ui.plotbu.clicked.connect(self.plot)
        self.ui.anibu.clicked.connect(self.ani_1)
        self.ui.clearbu1.clicked.connect(self.clear_1)
        self.ui.clearbu2.clicked.connect(self.clear_2)

        #self.ui.auto_y.toggled.connect(lambda: self.sety(self.ui.auto_y))
        #self.ui.fix_y.toggled.connect(lambda: self.sety(self.ui.fix_y))

        #self.IsFixY =False
        #self.up_y=0
        #self.down_y=0

        self.ui.alpha.textChanged.connect(self.set_alpha)
        self.ui.alpha.setValidator(self.doubleOnly)

        self.ui.gamma.textChanged.connect(self.set_gamma)
        self.ui.gamma.setValidator(self.doubleOnly)

        self.ui.dx.textChanged.connect(self.set_dx)
        self.ui.dx.setValidator(self.doubleOnly)

        self.ui.eps.textChanged.connect(self.set_eps)
        self.ui.eps.setValidator(self.doubleOnly)

        self.ui.Cx.textChanged.connect(self.set_Cx)
        self.ui.Cx.setValidator(self.doubleOnly)

        ''' self.ui.lineEdit_6.textChanged.connect(self.change_step_y)
        self.ui.lineEdit_6.setValidator(self.doubleOnly)

        self.ui.lineEdit_7.textChanged.connect(self.change_eps)
        self.ui.lineEdit_7.setValidator(self.doubleOnly)

        self.ui.lineEdit_8.textChanged.connect(self.change_incre)
        self.ui.lineEdit_8.setValidator(self.doubleOnly)

        self.ui.lineEdit_9.textChanged.connect(self.change_num)
        self.ui.lineEdit_9.setValidator(self.intOnly) '''

        self.ui.pro1.toggled.connect(lambda: self.change_type(self.ui.pro1))
        self.ui.pro2.toggled.connect(lambda: self.change_type(self.ui.pro2))
        self.ui.pro3.toggled.connect(lambda: self.change_type(self.ui.pro3))

        self.ui.arti.toggled.connect(lambda: self.change_arti(self.ui.arti))
        #self.ui.FTFS.toggled.connect(lambda: self.change_method(self.ui.FTFS))
        #self.ui.FTCS.toggled.connect(lambda: self.change_method(self.ui.FTCS))

        self.ui.rho.toggled.connect(lambda:self.change_sav(self.ui.rho))
        self.ui.p.toggled.connect(lambda: self.change_sav(self.ui.p))
        self.ui.T.toggled.connect(lambda: self.change_sav(self.ui.T))
        self.ui.Ma.toggled.connect(lambda:self.change_sav(self.ui.Ma))

        self.ui.plot_rho.toggled.connect(lambda:self.change_plot(self.ui.plot_rho))
        self.ui.plot_p.toggled.connect(lambda:self.change_plot(self.ui.plot_p))
        self.ui.plot_T.toggled.connect(lambda:self.change_plot(self.ui.plot_T))
        self.ui.plot_Ma.toggled.connect(lambda:self.change_plot(self.ui.plot_Ma))

        self.ui.ani_rho.toggled.connect(lambda:self.change_ani(self.ui.ani_rho))
        self.ui.ani_p.toggled.connect(lambda:self.change_ani(self.ui.ani_p))
        self.ui.ani_T.toggled.connect(lambda:self.change_ani(self.ui.ani_T))
        self.ui.ani_Ma.toggled.connect(lambda:self.change_ani(self.ui.ani_Ma))
        

    def set_alpha(self):
        self.alpha=float(self.ui.alpha.text()) if self.ui.alpha.text()!="" and self.ui.alpha.text()!="-" else 0

    def set_gamma(self):
        self.gamma=float(self.ui.gamma.text()) if self.ui.gamma.text()!="" and self.ui.gamma.text()!="-" else 0

    def set_dx(self):
        self.dx=float(self.ui.dx.text()) if self.ui.dx.text()!="" and self.ui.dx.text()!="-" else 0
    
    def set_eps(self):
        self.eps=float(self.ui.eps.text()) if self.ui.eps.text()!="" and self.ui.eps.text()!="-" else 0

    def set_Cx(self):
        self.Cx=float(self.ui.Cx.text()) if self.ui.Cx.text()!="" and self.ui.Cx.text()!="-" else 0

    def change_type(self,button):
        if button.text() == '亚声速-超声速':
            if button.isChecked()== True:
                self.type=1

        elif button.text() == '完全亚声速':
           if button.isChecked()== True:
               self.type=2

        elif button.text() == '激波捕捉':
            if button.isChecked()== True:
                self.type=3
    
    def change_arti(self,button):
        if button.text()=='人工黏性':
            if button.isChecked()==True:
                self.arti=1
    
    def change_sav(self,button):
        if button.text()=='密度':
            if button.isChecked()==True:
                self.sav=1
        elif button.text()=='压强':
            if button.isChecked()==True:
                self.sav=2
        elif button.text()=='温度':
            if button.isChecked()==True:
                self.sav=3
        elif button.text()=='马赫数':
            if button.isChecked()==True:
                self.sav=4
    #清屏            
    def clear_1(self):
        self.ax1.clear()
        self.canvas1.draw()

    def clear_2(self):
        self.ax2.clear()
        self.canvas2.draw()

        
    ''' def exit_1(self):
        sender = self.sender()
        self.exit()

    def exit(self): #退出应用程序
        app = QApplication.instance()
        app.quit()
        #sys.exit(self.exec_()) '''
    
    def change_plot(self,button):
        if button.text()=='密度':
            if button.isChecked()==True:
                self.plot_type=1
        elif button.text()=='压强':
            if button.isChecked()==True:
                self.plot_type=2
        elif button.text()=='温度':
            if button.isChecked()==True:
                self.plot_type=3
        elif button.text()=='马赫数':
            if button.isChecked()==True:
                self.plot_type=4

    def plot(self):
        sender = self.sender()
        #self.showcal()
        self.change_plot1()
    #绘制数值解与精确解的对比图
    def change_plot1(self):
        self.clear_1()



        ''' print('type:',self.type)
        print('p',self.p_)
        print('length:',self.length)
        print('alpha:',self.alpha)
        print('gamma',self.gamma) '''
        No = nozzle(type=self.type,p_=self.p_,length=self.length,alpha=self.alpha,gamma=self.gamma)
        
        if self.type==3:#含激波问题需要用61个网格点进行求解
            self.dx=0.05

            if self.arti==0: #当激波问题不采用人工黏性求解时，精度较低，这里为人性化设计，自动变换内置精度
                self.eps=1e-3
        ''' print(self.dx)
        print(self.arti)
        print(self.eps)
        print(self.Cx) '''

        x, rho, p, T, Ma=No.cal(dx=self.dx,arti_viscosity_flag=self.arti,Cx=self.Cx,eps=self.eps)
        ''' x, rho, p, T, Ma=No.cal(0.05,0,0.2,eps=1e-5) '''
        
        x_pre, rho_pre, p_pre, T_pre, Ma_pre = No.return_acu()

        font = {'family':'Times New Roman',
        'color':'darkred',
        'weight':'900',
        'size':15
        }
        
        if self.plot_type==1:
            self.ax1.set_xlabel('x(m)',fontdict={'weight':'normal','size':12})
            self.ax1.set_ylabel(r'$\frac{\rho}{\rho_0}$',fontdict={'weight':'normal','size':12},rotation=0)
            self.ax1.plot(x,rho[-1,:],label='数值解')
            self.ax1.scatter(x_pre,rho_pre,c='r',label='精确解')
            self.ax1.set_title('$\\rho-x$',fontdict=font)

        elif self.plot_type==2:
            self.ax1.set_xlabel('x(m)',fontdict={'weight':'normal','size':12})
            self.ax1.set_ylabel(r'$\frac{p}{p_0}$',fontdict={'weight':'normal','size':12},rotation=0)
            self.ax1.plot(x,p[-1,:],label='数值解')
            self.ax1.scatter(x_pre,p_pre,c='r',label='精确解')
            self.ax1.set_title('$p-x$',fontdict=font)

        elif self.plot_type==3:
            self.ax1.set_xlabel('x(m)',fontdict={'weight':'normal','size':12})
            self.ax1.set_ylabel(r'$\frac{T}{T_0}$',fontdict={'weight':'normal','size':12},rotation=0)
            self.ax1.plot(x,T[-1,:],label='数值解')
            self.ax1.scatter(x_pre,T_pre,c='r',label='精确解')
            self.ax1.set_title('$T-x$',fontdict=font)

        elif self.plot_type==4:
            self.ax1.set_xlabel('x(m)',fontdict={'weight':'normal','size':12})
            self.ax1.set_ylabel(r'$Ma$',fontdict={'weight':'normal','size':12},rotation=0)
            self.ax1.plot(x,Ma[-1,:],label='数值解')
            self.ax1.scatter(x_pre,Ma_pre,c='r',label='精确解')
            self.ax1.set_title('$Ma-x$',fontdict=font)
        
        
        self.ax1.grid()
        self.ax1.legend()
        self.canvas1.draw()
        
        if self.sav==1:
            data =pd.DataFrame(rho[-1,:])
            data.to_excel('output_rho.xlsx')
        elif self.sav==2:
            data =pd.DataFrame(p[-1,:])
            data.to_excel('output_p.xlsx')
        elif self.sav==2:
            data =pd.DataFrame(T[-1,:])
            data.to_excel('output_T.xlsx')
        elif self.sav==4:
            data =pd.DataFrame(Ma[-1,:])
            data.to_excel('output_Ma.xlsx')
             
    
    def change_ani(self,button):
        if button.text() == '密度':
            if button.isChecked()== True:
                self.ani_type=1

        elif button.text() == '压强':
           if button.isChecked()== True:
               self.ani_type=2

        elif button.text() == '温度':
            if button.isChecked()== True:
                self.ani_type=3
        
        elif button.text() == '马赫数':
            if button.isChecked()== True:
                self.ani_type=4

    def ani_1(self):
        sender = self.sender()
        self.ani()

    def ani(self): #绘制物理量收敛动画
        self.clear_2()

        No = nozzle(type=self.type,p_=self.p_,length=self.length,alpha=self.alpha,gamma=self.gamma)

        if self.type==3:#含激波问题需要用61个网格点进行求解
            self.dx=0.05

            if self.arti==0: #当激波问题不采用人工黏性求解时，精度较低，这里为人性化设计，自动变换内置精度
                self.eps=1e-3

        x, rho, p, T, Ma=No.cal(dx=self.dx,arti_viscosity_flag=self.arti,Cx=self.Cx,eps=self.eps)
        
        font = {'family':'Times New Roman',
        'color':'darkred',
        'weight':'900',
        'size':15
        }
        def init():
            self.ax2.grid()

        def run(i):
            self.ax2.clear()
            self.ui.t_num.setText("num:"+str(i))
            self.ax2.grid()
            self.ax2.set_xlabel('x(m)',fontdict={'weight':'normal','size':12})
            if self.ani_type==1:
                self.ax2.set_ylabel(r'$\frac{\rho}{\rho_0}$',fontdict={'weight':'normal','size':12},rotation=0)
                self.ax2.set_title('The Development of $\\rho-x$',fontdict=font)
                self.ax2.plot(x,rho[i,:])
            elif self.ani_type==2:
                self.ax2.set_ylabel(r'$\frac{p}{p_0}$',fontdict={'weight':'normal','size':12},rotation=0)
                self.ax2.set_title('The Development of $p-x$',fontdict=font)
                self.ax2.plot(x,p[i,:])
            elif self.ani_type==3:
                self.ax2.set_ylabel(r'$\frac{T}{T_0}$',fontdict={'weight':'normal','size':12},rotation=0)
                self.ax2.set_title('The Development of $T-x$',fontdict=font)
                self.ax2.plot(x,T[i,:])
            elif self.ani_type==4:
                self.ax2.set_ylabel(r'$Ma$',fontdict={'weight':'normal','size':12},rotation=0)
                self.ax2.set_title('The Development of $Ma-x$',fontdict=font)
                self.ax2.plot(x,Ma[i,:])
            
        #print(len(rho)-1)
        #注意一定要写self.ani1而不是ani1
        self.ani1 = animation.FuncAnimation(self.fig2, run, frames=len(rho)-1, blit=False, interval=20, repeat=False,init_func=init)
        self.ui.stop.clicked.connect(self.ani1.pause)
        self.ui.continue_2.clicked.connect(self.ani1.resume)
        self.canvas2.draw()
        
        if self.sav==1:
            data =pd.DataFrame(rho)
            data.to_excel('output_rho_all.xlsx')
        elif self.sav==2:
            data =pd.DataFrame(p)
            data.to_excel('output_p_all.xlsx')
        elif self.sav==2:
            data =pd.DataFrame(T)
            data.to_excel('output_T_all.xlsx')
        elif self.sav==4:
            data =pd.DataFrame(Ma)
            data.to_excel('output_Ma_all.xlsx')
    #初始化参数        
    def init_para(self):
        self.p_=0.93
        self.length=3
        self.alpha=0.7
        self.gamma=1.4
        self.p0=1
        self.rho0=1
        self.T0=1
        self.dx=0.1
        self.eps=1e-5
        
        self.arti=0
        self.Cx=0.2
        
        self.sav=0

        self.plot_type=0

        self.ani_type=0
    #初始化图像
    def initialize_figure(self, fig1, ax1, fig2, ax2):
        ''' 
        Initializes a matplotlib figure inside a GUI container.
        Only call this once when initializing.
        '''

        plt.rcParams["font.sans-serif"] = "SimHei"
        plt.rcParams["axes.unicode_minus"] = False
        # Figure creation (self.fig and self.ax)
        self.fig1 = fig1
        self.ax1 = ax1
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.fig2 = fig2
        self.ax2 = ax2
        self.ax2.set_xlabel('x')
        self.ax2.set_ylabel('y')

        # Canvas creation
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas2 = FigureCanvas(self.fig2)

        self.toolbar1 = NavigationToolbar(self.canvas1, self, coordinates=True)
        self.ui.bar_1.addWidget(self.toolbar1)

        self.toolbar2 = NavigationToolbar(self.canvas2, self, coordinates=True)
        self.ui.bar2.addWidget(self.toolbar2)
        
        self.ui.plot_2.addWidget(self.canvas1)
        self.ui.ani.addWidget(self.canvas2)
        # self.fig.tight_layout()
        self.canvas1.draw()
        self.canvas2.draw()


