import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

class nozzle:
    def __init__(self,type=1, p_=0.93,length=3, alpha=0.5, gamma=1.4, p0=1, rho0=1, T0=1):
        self.length = length
        self.alpha = alpha #柯朗数
        self.gamma = gamma #流体比热
        self.p_ = p_ #p_=p_N/p_0
        #self.width = _width
        #self.r = _r
        ''' type = 1: Subsonic-Supersonic
        type = 2: all-subsonic
        type = 3: containing shock waves '''
        self.type = type 
        self.p0 = p0
        self.rho0 = rho0
        self.T0 = T0
        self.x=0
        self.rho = 0
        self.v = 0
        self.T = 0
        self.Ma = 0
        self.p = 0
        
        #精确解
        self.rho_pre = 0
        self.T_pre = 0
        self.p_pre = 0
        self.Ma_pre = 0
        self.x_pre=0
        
        '''  data1 = {"length":self.length,"width":self.width}
        assert self.width<=self.length,'Invalid shape:{length}<={width}'.format(**data1)
        
        data2 = {"width":self.width,"r":self.r}
        assert self.r<=self.width,'Invalid radius:{width}<={r}'.format(**data2) '''
        
    def cal(self, dx=0.1, arti_viscosity_flag=0, Cx=0.2, eps=1e-5, max_iter=5000):
        '''
        :param x: step of x
        :param y: step of t
        :param eps: the error permission of the solution
        :return: difference stream function matrix
        '''  
        #定义参数
        self.x = np.arange(0,self.length+dx,dx)
        x_num = len(np.arange(0,self.length,dx))
        #t_num = len(np.arange(0,self.t,dt))
        
        #构造物理量
        rho = np.zeros((1,x_num+1))
        v = np.zeros((1,x_num+1))
        T = np.zeros((1,x_num+1))
        
        A = np.zeros(x_num+1)

        
        #构造容器
        temp_rho = np.zeros((1,x_num+1))
        temp_v = np.zeros((1,x_num+1))
        temp_T = np.zeros((1,x_num+1))
        
        
        #存放偏导数
        drho = np.zeros(x_num+1)
        dv = np.zeros(x_num+1)
        dT = np.zeros(x_num+1)
        
        drho1 = np.zeros(x_num+1)
        dv1 = np.zeros(x_num+1)
        dT1 = np.zeros(x_num+1)
        
        drho2 = np.zeros(x_num+1)
        dv2 = np.zeros(x_num+1)
        dT2 = np.zeros(x_num+1)
        
        #print(rho.shape)
        
        #Subsonic-Supersonic
        if self.type==1:
            #设定流场初值
            for i in range(x_num+1):
                rho[0,i] = 1 - 0.3146*i*dx
                T[0,i] = 1 - 0.2314*i*dx
                v[0,i] = (0.1+1.09*i*dx)*np.sqrt(T[0,i])
                A[i] = 1+2.2*(i*dx-1.5)**2

            #循环迭代
            t_num = 0
            t = [0]
            #循环终止条件
            delta = 1
            while(delta>eps):

                assert t_num<=max_iter, 'Improper initial condition(over the max iter_num)'
                
                #if t_num==64:
                    #print(T[t_num,:])
                
                #每次循环迭代前，计算最小的时间步长
                dt = 1
                #print(t_num)
                for i in range(x_num+1):
                    dt1 = self.alpha*dx/(np.abs(v[t_num,i])+np.sqrt(T[t_num,i]/self.T0))
                    ''' if t_num==0:
                        print(dt1) '''
                    if dt1 < dt:
                        dt = dt1

                t.append(t[t_num]+dt)
                ''' if t_num==0:
                    print(dt) '''
                ''' if t_num==1:
                    print(dt) '''

                
                #print(dt)
                #预估步
                for i in range(1,x_num):
        
                    drho1[i] =  -rho[t_num,i]*(v[t_num,i+1]-v[t_num,i])/dx \
                                -rho[t_num,i]*v[t_num,i]*(np.log(A[i+1])-np.log(A[i]))/dx \
                                -v[t_num,i]*(rho[t_num,i+1]-rho[t_num,i])/dx
                    
                    dv1[i] =    -v[t_num,i]*(v[t_num,i+1]-v[t_num,i])/dx \
                                - ((T[t_num,i+1]-T[t_num,i])/dx 
                                +T[t_num,i]*(rho[t_num,i+1]-rho[t_num,i])/rho[t_num,i]/dx)/self.gamma
                    
                    dT1[i] =    -v[t_num,i]*(T[t_num,i+1]-T[t_num,i])/dx \
                                -(self.gamma-1)*T[t_num,i]*((v[t_num,i+1]-v[t_num,i])/dx
                                +v[t_num,i]*(np.log(A[i+1])-np.log(A[i]))/dx)
                    
                for i in range(1,x_num):
                    temp_rho[0,i] = rho[t_num,i] + drho1[i]*dt
                    temp_v[0,i] = v[t_num,i] + dv1[i]*dt
                    temp_T[0,i] =  T[t_num,i] + dT1[i]*dt              
                
                temp_rho[0,0]=self.rho0
                temp_T[0,0]=self.T0
                temp_v[0,0] = 2*temp_v[0,1]-temp_v[0,2] 
                
                ''' temp_rho[0,-1]=2*temp_rho[0,-2]-temp_rho[0,-3]
                temp_T[0,-1]=2*temp_T[0,-2]-temp_T[0,-3]
                temp_v[0,-1]=2*temp_v[0,-2]-temp_v[0,-3] '''
                #if t_num==75:
                    #print(temp_rho[0,:])
                #修正步
                for i in range(1,x_num):
                    drho2[i] =  -temp_rho[0,i]*(temp_v[0,i]-temp_v[0,i-1])/dx \
                                -temp_rho[0,i]*temp_v[0,i]*(np.log(A[i])-np.log(A[i-1]))/dx \
                                -temp_v[0,i]*(temp_rho[0,i]-temp_rho[0,i-1])/dx
                    
                    dv2[i] =    -temp_v[0,i]*(temp_v[0,i]-temp_v[0,i-1])/dx \
                                -((temp_T[0,i]-temp_T[0,i-1])/dx
                                +temp_T[0,i]*(temp_rho[0,i]-temp_rho[0,i-1])/temp_rho[0,i]/dx)/self.gamma
                    
                    dT2[i] =    -temp_v[0,i]*(temp_T[0,i]-temp_T[0,i-1])/dx \
                                -(self.gamma-1)*temp_T[0,i]*((temp_v[0,i]-temp_v[0,i-1])/dx
                                +temp_v[0,i]*(np.log(A[i])-np.log(A[i-1]))/dx)
                
                drho = (drho1+drho2)/2
                dv = (dv1+dv2)/2
                dT = (dT1+dT2)/2
                
                #print(drho)
                for i in range(1,x_num):    
                    
                    temp_rho[0,i] = rho[t_num,i] + drho[i]*dt
                    temp_v[0,i] = v[t_num,i] + dv[i]*dt
                    temp_T[0,i] =  T[t_num,i] + dT[i]*dt       
                
                temp_rho[0,0]=self.rho0
                temp_T[0,0]=self.T0
                temp_v[0,0] = 2*temp_v[0,1]-temp_v[0,2]
                
                temp_rho[0,-1]=2*temp_rho[0,-2]-temp_rho[0,-3]
                temp_T[0,-1]=2*temp_T[0,-2]-temp_T[0,-3]
                temp_v[0,-1]=2*temp_v[0,-2]-temp_v[0,-3]
                
                #print(temp_rho)
                #print(rho)
                
                rho=np.concatenate((rho,temp_rho),axis=0)
                v=np.concatenate((v,temp_v),axis=0)
                T=np.concatenate((T,temp_T),axis=0)
                
                #print(rho)
                
                delta_rho = np.max(np.absolute(temp_rho-rho[t_num,:]))
                delta_v = np.max(np.absolute(temp_v-v[t_num,:]))
                delta_T = np.max(np.absolute(temp_T-T[t_num,:]))
                delta = np.max(np.array([delta_rho, delta_v, delta_T]))
                #print(delta)
                
                #容器释放
                temp_rho.fill(0)
                temp_T.fill(0)
                temp_v.fill(0)
                
                drho1.fill(0)
                drho2.fill(0)
                dv1.fill(0)
                dv2.fill(0)
                dT1.fill(0)
                dT2.fill(0)
                
                t_num += 1
                
        elif self.type==2: #all-subsonic
            
            #设定流场初值
            for i in range(x_num+1):
                rho[0,i] = 1 - 0.023*i*dx
                T[0,i] = 1 - 0.00933*i*dx
                v[0,i] = 0.05+0.11*i*dx
                if i <= x_num/2:
                    A[i] = 1+2.2*(i*dx-1.5)**2
                else:
                    A[i] = 1+0.2223*(i*dx-1.5)**2
                    
            #循环迭代
            t_num = 0
            t = [0]
            #循环终止条件
            delta = 1
            
            while(delta>eps):
                
                assert t_num<=max_iter, 'Improper initial condition(over the max iter_num)'
                
                #每次循环迭代前，计算最小的时间步长
                dt = 1
                #print(t_num)
                for i in range(x_num+1):
                    dt1 = self.alpha*dx/(v[t_num,i]+np.sqrt(T[t_num,i]/self.T0))
                    if dt1 < dt:
                        dt = dt1
                #print(dt1)
                t.append(t[t_num]+dt)
                #print(t)
                
                #预估步
                for i in range(1,x_num):
        
                    drho1[i] = -rho[t_num,i]*(v[t_num,i+1]-v[t_num,i])/dx-rho[t_num,i]*v[t_num,i]*(np.log(A[i+1])-np.log(A[i]))/dx-v[t_num,i]*(rho[t_num,i+1]-rho[t_num,i])/dx
                    dv1[i] = -v[t_num,i]*(v[t_num,i+1]-v[t_num,i])/dx- ((T[t_num,i+1]-T[t_num,i])/dx+T[t_num,i]*(rho[t_num,i+1]-rho[t_num,i])/rho[t_num,i]/dx)/self.gamma
                    dT1[i] = -v[t_num,i]*(T[t_num,i+1]-T[t_num,i])/dx-(self.gamma-1)*T[t_num,i]*((v[t_num,i+1]-v[t_num,i])/dx+v[t_num,i]*(np.log(A[i+1])-np.log(A[i]))/dx)
                    
                    
                for i in range(1,x_num):
                    temp_rho[0,i] = rho[t_num,i] + drho1[i]*dt
                    temp_v[0,i] = v[t_num,i] + dv1[i]*dt
                    temp_T[0,i] =  T[t_num,i] + dT1[i]*dt              
                
                
                temp_rho[0,0]=self.rho0
                temp_T[0,0]=self.T0
                temp_v[0,0] = 2*temp_v[0,1]-temp_v[0,2]
                #if t_num==75:
                    #print(temp_rho[0,:])
                #修正步
                for i in range(1,x_num):
                    drho2[i] = -temp_rho[0,i]*(temp_v[0,i]-temp_v[0,i-1])/dx-temp_rho[0,i]*temp_v[0,i]*(np.log(A[i])-np.log(A[i-1]))/dx-temp_v[0,i]*(temp_rho[0,i]-temp_rho[0,i-1])/dx
                    dv2[i] = -temp_v[0,i]*(temp_v[0,i]-temp_v[0,i-1])/dx-((temp_T[0,i]-temp_T[0,i-1])/dx+temp_T[0,i]*(temp_rho[0,i]-temp_rho[0,i-1])/temp_rho[0,i]/dx)/self.gamma
                    dT2[i] = -temp_v[0,i]*(temp_T[0,i]-temp_T[0,i-1])/dx-(self.gamma-1)*temp_T[0,i]*((temp_v[0,i]-temp_v[0,i-1])/dx+temp_v[0,i]*(np.log(A[i])-np.log(A[i-1]))/dx)
                

                drho = (drho1+drho2)/2
                dv = (dv1+dv2)/2
                dT = (dT1+dT2)/2
                
                for i in range(1,x_num):    
                    temp_rho[0,i] = rho[t_num,i] + drho[i]*dt
                    temp_v[0,i] = v[t_num,i] + dv[i]*dt
                    temp_T[0,i] =  T[t_num,i] + dT[i]*dt 
                
                
                temp_rho[0,0]=self.rho0
                temp_T[0,0]=self.T0
                temp_v[0,0] = 2*temp_v[0,1]-temp_v[0,2]
                
                #temp_rho[0,x_num]=2*temp_rho[0,x_num-1]-temp_rho[0,x_num-2]
                temp_T[0,x_num]=2*temp_T[0,x_num-1]-temp_T[0,x_num-2]
                temp_v[0,x_num]=2*temp_v[0,x_num-1]-temp_v[0,x_num-2]
                temp_rho[0,x_num]=self.p_*self.p0/temp_T[0,x_num]
                

                rho=np.concatenate((rho,temp_rho),axis=0)
                v=np.concatenate((v,temp_v),axis=0)
                T=np.concatenate((T,temp_T),axis=0)
                
                #print(rho)
                
                delta_rho = np.max(np.absolute(temp_rho-rho[t_num,:]))
                delta_v = np.max(np.absolute(temp_v-v[t_num,:]))
                delta_T = np.max(np.absolute(temp_T-T[t_num,:]))
                delta = np.max(np.array([delta_rho, delta_v, delta_T]))
                #print(delta)
                
                #容器释放
                temp_rho.fill(0)
                temp_T.fill(0)
                temp_v.fill(0)
                
                t_num += 1
        
        
        #containing shock wave        
        else:
            
            #构造物理量
            dA = np.zeros(x_num+1)
            
            if arti_viscosity_flag==1:
                p = np.zeros((1,x_num+1))
            
            #构造守恒量
            U1 = np.zeros((1,x_num+1))
            U2 = np.zeros((1,x_num+1))
            U3 = np.zeros((1,x_num+1))
            
            F1 = np.zeros((1,x_num+1))
            F2 = np.zeros((1,x_num+1))
            F3 = np.zeros((1,x_num+1))
            
            #J2 = np.zeros((1,x_num+1))
            
            #构造守恒量容器
            temp_U1 = np.zeros((1,x_num+1))
            temp_U2 = np.zeros((1,x_num+1))
            temp_U3 = np.zeros((1,x_num+1))
            
            temp_F1 = np.zeros((1,x_num+1))
            temp_F2 = np.zeros((1,x_num+1))
            temp_F3 = np.zeros((1,x_num+1)) 
            
            #temp_J2 = np.zeros((1,x_num+1))
            
            if arti_viscosity_flag==1:
                #人工黏性项
                assert dx<=0.05, 'Improper x step(the shock waves need higher precision to show)'
                temp_S1 = np.zeros((1,x_num+1))
                temp_S2 = np.zeros((1,x_num+1))
                temp_S3 = np.zeros((1,x_num+1))
                
            #存放偏导数
            dU1 = np.zeros(x_num+1)
            dU2 = np.zeros(x_num+1)
            dU3 = np.zeros(x_num+1)
            
            dU11 = np.zeros(x_num+1)
            dU21 = np.zeros(x_num+1)
            dU31 = np.zeros(x_num+1)
            
            dU12 = np.zeros(x_num+1)
            dU22 = np.zeros(x_num+1)
            dU32 = np.zeros(x_num+1)
            
            #print(dx)
            #设定流场初值
            for i in range(x_num+1):
                if i < x_num/6:
                    rho[0,i]=1
                    T[0,i]=1
                elif i>=x_num/6 and i<x_num/2:
                    rho[0,i]=1-0.366*(i*dx-0.5)
                    T[0,i]=1-0.167*(i*dx-0.5)
                    ''' else:
                    rho[0,i] = 0.634-0.3879*(i*dx-1.5)
                    T[0,i] = 0.833-0.3507*(i*dx-1.5) '''
                elif i>=x_num/2 and i<7*x_num/10:
                    rho[0,i]=0.634-0.702*(i*dx-1.5)
                    T[0,i] = 0.833-0.4908*(i*dx-1.5)  
                else:
                    rho[0,i]=0.5892-0.10228*(i*dx-2.1)
                    T[0,i]=0.93968-0.0622*(i*dx-2.1)
                 
            for i in range(x_num+1):  
                    A[i] = 1+2.2*(i*dx-1.5)**2
                    dA[i] = 4.4*(i*dx-1.5)   
            
            for i in range(x_num+1):
                v[0,i] = 0.59/rho[0,i]/A[i]
            
            ''' print(A)
            print(rho)
            print(v)
            print(T) ''' 
                
            #设定守恒量初始值
            U1 = rho*A
            U2 = rho*A*v
            U3 = rho*(T/(self.gamma-1)+self.gamma*v**2/2)*A
            
            ''' print(U1)
            print(U2)
            print(U3) '''
            
            F1 = U2
            F2 = U2**2/U1 + 1/self.gamma * U1*(self.gamma-1)*(U3/U1 - self.gamma/2*(U2/U1)**2)
            F3 = self.gamma*U2*U3/U1-self.gamma*(self.gamma-1)/2*U2**3/U1**2
            
            #J2 = rho*T/self.gamma
            
            if arti_viscosity_flag==1:
                for i in range(x_num+1):
                    p[0,i]=rho[0,i]*T[0,i]
                
            #循环迭代
            t_num = 0
            t = [0]
            #循环终止条件
            delta = 1
            while(delta>eps):
                assert t_num<=max_iter, 'Improper initial condition(over the max iter_num)'
                #print(t_num)
                #每次循环迭代前，计算最小的时间步长
                dt = 1
                #if t_num==2:
                    #print(T)
                for i in range(x_num+1):
                    dt1 = self.alpha*dx/(v[t_num,i]+np.sqrt(T[t_num,i]/self.T0))
                    ''' if t_num==0:
                        print(dt1) '''
                    if dt1 < dt:
                        dt = dt1
                #print(dt)
                t.append(t[t_num]+dt)
                #print(t)
                
                #print(p)
                      
                #预估步
                for i in range(1,x_num):
        
                    dU11[i] = -(F1[t_num,i+1]-F1[t_num,i])/dx
                    dU21[i] = -(F2[t_num,i+1]-F2[t_num,i])/dx+(self.gamma-1)/self.gamma*(U3[t_num,i]-self.gamma/2*U2[t_num,i]**2/U1[t_num,i])*(np.log(A[i+1])-np.log(A[i]))/dx
                    ''' dU21[i] = -(F2[t_num,i+1]-F2[t_num,i])/dx+U1[t_num,i]*(self.gamma-1)*(U3[t_num,i]/U1[t_num,i]-self.gamma/2*(U2[t_num,i]/U1[t_num,i])**2)*(A[i+1]-A[i])/self.gamma/A[i]/dx '''
                    dU31[i] = -(F3[t_num,i+1]-F3[t_num,i])/dx
                
                for i in range(1,x_num):
                            
                    if arti_viscosity_flag==1:
                        #print(p[t_num,i+1]+p[t_num,i-1]-2*p[t_num,i])
                        temp_S1[0,i] = Cx*np.abs(p[t_num,i+1]+p[t_num,i-1]-2*p[t_num,i])/(p[t_num,i+1]+p[t_num,i-1]+2*p[t_num,i])*(U1[t_num,i+1]+U1[t_num,i-1]-2*U1[t_num,i])
                        temp_S2[0,i] = Cx*np.abs(p[t_num,i+1]+p[t_num,i-1]-2*p[t_num,i])/(p[t_num,i+1]+p[t_num,i-1]+2*p[t_num,i])*(U2[t_num,i+1]+U2[t_num,i-1]-2*U2[t_num,i])
                        temp_S3[0,i] = Cx*np.abs(p[t_num,i+1]+p[t_num,i-1]-2*p[t_num,i])/(p[t_num,i+1]+p[t_num,i-1]+2*p[t_num,i])*(U3[t_num,i+1]+U3[t_num,i-1]-2*U3[t_num,i])
                        
                        temp_U1[0,i] = U1[t_num,i]+dU11[i]*dt+temp_S1[0,i]
                        temp_U2[0,i] = U2[t_num,i]+dU21[i]*dt+temp_S2[0,i]
                        temp_U3[0,i] = U3[t_num,i]+dU31[i]*dt+temp_S3[0,i]
                        
                    else:     
                        temp_U1[0,i] = U1[t_num,i]+dU11[i]*dt
                        temp_U2[0,i] = U2[t_num,i]+dU21[i]*dt
                        temp_U3[0,i] = U3[t_num,i]+dU31[i]*dt
                
                #边界条件
                temp_U1[0,0] = U1[0,0]
                temp_U2[0,0] = 2*temp_U2[0,1]-temp_U2[0,2]
                temp_U3[0,0] = temp_U1[0,0]*(self.T0/(self.gamma-1)+self.gamma*(temp_U2[0,0]/temp_U1[0,0])**2/2)
                
                temp_U1[0,-1] = 2*temp_U1[0,-2]-temp_U1[0,-3]
                temp_U2[0,-1] = 2*temp_U2[0,-2]-temp_U2[0,-3]
                temp_U3[0,-1] = 0.6784*A[-1]/(self.gamma-1)+self.gamma*temp_U2[0,-1]**2/2/temp_U1[0,-1] #p_N'=0.6784为给定值
                ''' temp_U3[0,-1] = 2*temp_U3[0,-2]-temp_U3[0,-3] '''
                
                #更新守恒量
                temp_F1 = temp_U2
                temp_F2 = temp_U2**2/temp_U1+1/self.gamma * temp_U1*(self.gamma-1)*(temp_U3/temp_U1 - self.gamma/2*(temp_U2/temp_U1)**2)
                temp_F3 = self.gamma*temp_U2*temp_U3/temp_U1-self.gamma*(self.gamma-1)/2*temp_U2**3/temp_U1**2
                
                #temp_J2 = temp_U1*(self.gamma-1)*((temp_U3/temp_U1)-self.gamma*(temp_U2/temp_U1)**2/2)*dA/self.gamma/A
                
                if arti_viscosity_flag==1:
                    temp_p = temp_U1*(self.gamma-1)*(temp_U3/temp_U1-self.gamma*(temp_U2/temp_U1)**2/2)/A
                
                #修正步
                for i in range(1,x_num):
                    
                    ''' dU12[i] = -(F1[t_num,i]-F1[t_num,i-1])/dx
                    dU22[i] = -(F2[t_num,i]-F2[t_num,i-1])/dx+J2[t_num,i]
                    dU32[i] = -(F3[t_num,i]-F3[t_num,i-1])/dx '''
                    
                    dU12[i] = -(temp_F1[0,i]-temp_F1[0,i-1])/dx
                    dU22[i] = -(temp_F2[0,i]-temp_F2[0,i-1])/dx+(self.gamma-1)/self.gamma*(temp_U3[0,i]-self.gamma/2*temp_U2[0,i]**2/temp_U1[0,i])*(np.log(A[i])-np.log(A[i-1]))/dx
                    ''' dU22[i] = -(temp_F2[0,i]-temp_F2[0,i-1])/dx+temp_U1[0,i]*(self.gamma-1)*(temp_U3[0,i]/temp_U1[0,i]-self.gamma/2*(temp_U2[0,i]/temp_U1[0,i])**2)*(A[i]-A[i-1])/self.gamma/A[i]/dx '''
                    dU32[i] = -(temp_F3[0,i]-temp_F3[0,i-1])/dx
                
                for i in range(1,x_num):
                        
                    dU1 = (dU11+dU12)/2
                    dU2 = (dU21+dU22)/2
                    dU3 = (dU31+dU32)/2
                
                for i in range(1,x_num):
                    if arti_viscosity_flag==1:
                        temp_S1[0,i] = Cx*np.abs(temp_p[0,i+1]+temp_p[0,i-1]-2*temp_p[0,i])/(temp_p[0,i+1]+temp_p[0,i-1]+2*temp_p[0,i])*(temp_U1[0,i+1]+temp_U1[0,i-1]-2*temp_U1[0,i])
                        temp_S2[0,i] = Cx*np.abs(temp_p[0,i+1]+temp_p[0,i-1]-2*temp_p[0,i])/(temp_p[0,i+1]+temp_p[0,i-1]+2*temp_p[0,i])*(temp_U2[0,i+1]+temp_U2[0,i-1]-2*temp_U2[0,i])
                        temp_S3[0,i] = Cx*np.abs(temp_p[0,i+1]+temp_p[0,i-1]-2*temp_p[0,i])/(temp_p[0,i+1]+temp_p[0,i-1]+2*temp_p[0,i])*(temp_U3[0,i+1]+temp_U3[0,i-1]-2*temp_U3[0,i])
                        
                        temp_U1[0,i] = U1[t_num,i]+dU1[i]*dt+temp_S1[0,i]
                        temp_U2[0,i] = U2[t_num,i]+dU2[i]*dt+temp_S2[0,i]
                        temp_U3[0,i] = U3[t_num,i]+dU3[i]*dt+temp_S3[0,i]
                    else:
                        temp_U1[0,i] = U1[t_num,i]+dU1[i]*dt
                        temp_U2[0,i] = U2[t_num,i]+dU2[i]*dt
                        temp_U3[0,i] = U3[t_num,i]+dU3[i]*dt
                
                
                #边界条件
                temp_U1[0,0] = U1[0,0]
                temp_U2[0,0] = 2*temp_U2[0,1]-temp_U2[0,2]
                temp_U3[0,0] = temp_U1[0,0]*(self.T0/(self.gamma-1)+self.gamma*(temp_U2[0,0]/temp_U1[0,0])**2/2)
                
                temp_U1[0,-1] = 2*temp_U1[0,-2]-temp_U1[0,-3]
                temp_U2[0,-1] = 2*temp_U2[0,-2]-temp_U2[0,-3]
                temp_U3[0,-1] = 0.6784*A[-1]/(self.gamma-1)+self.gamma*temp_U2[0,-1]**2/2/temp_U1[0,-1]
                ''' temp_U3[0,-1] = 2*temp_U3[0,-2]-temp_U3[0,-3] '''
            
                ''' if t_num==0: '''
                ''' print(temp_U1) '''
                ''' print(temp_U2)
                print(temp_U3) '''
                
                #更新守恒量
                temp_F1 = temp_U2
                temp_F2 = temp_U2**2/temp_U1+1/self.gamma * temp_U1*(self.gamma-1)*(temp_U3/temp_U1 - self.gamma/2*(temp_U2/temp_U1)**2)
                temp_F3 = self.gamma*temp_U2*temp_U3/temp_U1-self.gamma*(self.gamma-1)/2*temp_U2**3/temp_U1**2
                
                #temp_J2 = temp_U1*(self.gamma-1)*((temp_U3/temp_U1)-self.gamma*(temp_U2/temp_U1)**2/2)*dA/self.gamma/A
                
                if arti_viscosity_flag==1:
                    temp_p = temp_U1*(self.gamma-1)*(temp_U3/temp_U1-self.gamma*(temp_U2/temp_U1)**2/2)/A
                    
                #将守恒量转换回物理量
                temp_rho = temp_U1/A
                temp_v = temp_U2/temp_U1
                temp_T = (self.gamma-1)*(temp_U3/temp_U1-self.gamma*temp_v**2/2)
                
                #添加入表
                U1=np.concatenate((U1,temp_U1),axis=0)
                U2=np.concatenate((U2,temp_U2),axis=0)
                U3=np.concatenate((U3,temp_U3),axis=0)
                
                F1=np.concatenate((F1,temp_F1),axis=0)
                F2=np.concatenate((F2,temp_F2),axis=0)
                F3=np.concatenate((F3,temp_F3),axis=0) 
                
                #J2 = np.concatenate((J2,temp_J2),axis=0)
                
                if arti_viscosity_flag==1:
                    p=np.concatenate((p,temp_p),axis=0)
                
                rho=np.concatenate((rho,temp_rho),axis=0)
                v=np.concatenate((v,temp_v),axis=0)
                T=np.concatenate((T,temp_T),axis=0)
                
                #print(rho)
                
                delta_rho = np.max(np.absolute(temp_rho-rho[t_num,:]))
                delta_v = np.max(np.absolute(temp_v-v[t_num,:]))
                delta_T = np.max(np.absolute(temp_T-T[t_num,:]))
                delta = np.max(np.array([delta_rho, delta_v, delta_T]))
                #print(delta)
                
                #容器释放
                temp_rho.fill(0)
                temp_T.fill(0)
                temp_v.fill(0)
                
                temp_U1.fill(0)
                temp_U2.fill(0)
                temp_U3.fill(0)
                
                temp_F1.fill(0)
                temp_F2.fill(0)
                temp_F3.fill(0)
                
                #temp_J2.fill(0)
                
                
                if arti_viscosity_flag==1:
                    temp_p.fill(0)
                    temp_S1.fill(0)
                    temp_S2.fill(0)
                    temp_S3.fill(0)
                
                t_num += 1
            
        self.rho=rho
        self.v=v
        self.T=T
        
        p=rho*T
        Ma = v/np.sqrt(T)

        self.p=p
        self.Ma=Ma

        x=self.x
        
        ''' data =pd.DataFrame(T)
        data.to_excel('ouput.xlsx') '''
        
        return x, rho, p, T, Ma

    #计算精确解各点位置的马赫数
    def cal_acu(self,dx=0.1):
        
        x_num = len(np.arange(0,self.length,dx))

        x = sp.symbols('x')
        
        #设置容器
        Ma = []

        if self.type==1:

            for x0 in np.arange(0,self.length,dx):
                A = 1+2.2*(x0-1.5)**2
                eqn = 1/x**2*(2/(self.gamma+1)*(1+(self.gamma-1)/2*x**2))**((self.gamma+1)/(self.gamma-1))-A**2
                #print(1)
                outputs = sp.solve(eqn,x)
                #print(outputs)

                for output in outputs:
                    if sp.im(output) ==0 and sp.re(output)>0:
                        if x0<1.5:
                            if output<1:
                                Ma.append(output)
                        elif x0==1.5:
                            Ma.append(1)
                        else:
                            if output > 1:
                                Ma.append(output)

            print(Ma)

            ''' elif self.type==2:

            y = sp.symbols('y')
            eqn1 = 0.93-(1+(self.gamma-1)/2*y**2)**((-self.gamma)/(self.gamma-1))
            print(1)
            output = sp.solve(eqn1,y)
            print(output)

            for x0 in np.arange(0,self.length,dx):
                if x0<=1.5:
                    A = 1+2.2*(x-1.5)**2
                else:
                    A = 1+0.2223*(x-1.5)**2
                

            Mae = solve(0.93-(1+(self.gamma-1)/2*x**2)**((-self.gamma)/(self.gamma-1)))[0]

            y = Symbol('y')

            A_ = solve(1.500175/y-(2*(1+(self.gamma)*Mae**2/2)/(self.gamma+1))**((self.gamma+1)/(self.gamma-1))/Mae**2)[0]

            z = Symbol('z')

            for i in range(x_num+1):
                if i <= x_num/2:
                    A[i] = 1+2.2*(i*dx-1.5)**2
                else:
                    A[i] = 1+0.2223*(i*dx-1.5)**2
                
                Ma[i] = solve((A[i]/A_)**2-(2*(1+(self.gamma)*z**2/2)/(self.gamma+1))**((self.gamma+1)/(self.gamma-1))/z**2)[0]
                p[i] = (1+(self.gamma-1)/2*Ma[i]**2)**((-self.gamma)/(self.gamma-1))
                rho[i] = (1+(self.gamma-1)/2*Ma[i]**2)**((-1)/(self.gamma-1))
                T[i] = (1+(self.gamma-1)/2*Ma[i]**2)**(-1) '''

        else:
            Ma2 = 0.1431
            Ae = 1+2.2*(3-1.5)**2
            print(1)
            astar = Ae/np.sqrt(1/Ma2**2*(2/(self.gamma+1)*(1+(self.gamma-1)/2*Ma2**2))**((self.gamma+1)/(self.gamma-1)))
            #print(astar)

            for x0 in np.arange(2.1,3,0.1):
                A = 1+2.2*(x0-1.5)**2
                eqn = 1/x**2*(2/(self.gamma+1)*(1+(self.gamma-1)/2*x**2))**((self.gamma+1)/(self.gamma-1))-(A/1.4533668392912007)**2
                outputs = sp.solve(eqn, x)
                for output in outputs:
                    if sp.im(output) ==0 and sp.re(output)>0:
                        if output<1:
                            print(output)
       
    #根据各点马赫数的值计算各点物理量
    def return_acu(self):
        x=np.arange(0, 3, 0.1)
        if self.type==1:
            ma=np.array([0.0978206034939950, 0.109731682553067, 0.123789919776600, 0.140495344506729, 0.160484052713488, 0.184566410048765, 0.213773136314217, 0.249407010900465, 0.293092705570777, 0.346807253908325, 0.412857182193025, 0.493746986457211, 0.591869921259453, 0.708978789098207, 0.845506751305335, 1, 1.16904155212089, 1.34785900270909, \
            1.53136467063195, 1.71510359021959, 1.89575135460289, 2.07115949804550, 2.24014468795662, 2.40220988465202, 2.55729900914802, 2.70561578551664, 2.84750255300281, 2.98336428599161, 3.11362332944497, 3.23869379894824])
        elif self.type==2:
            ma=np.array([0.077, 0.086, 0.097, 0.110, 0.126, 0.144, 0.167, 0.194, 0.226, 0.265, 0.312, 0.365, 0.423, 0.480, 0.524, 0.541, 0.539, 0.534, 0.526, 0.514, 0.500, 0.485, 0.468, 0.450, 0.431, 0.413, 0.394, 0.376, 0.358, 0.340])
        else:
            ma=np.array([0.0978206034939950, 0.109731682553067, 0.123789919776600, 0.140495344506729, 0.160484052713488, 0.184566410048765, 0.213773136314217, 0.249407010900465, 0.293092705570777, 0.346807253908325, 0.412857182193025, 0.493746986457211, 0.591869921259453, 0.708978789098207, 0.845506751305335, 1, 1.16904155212089, 1.34785900270909, \
            1.53136467063195, 1.71510359021959, 1.89575135460289, 0.565162944895497, 0.457811823757440, 0.380511427123903, 0.321460045647811, 0.274935622113095, 0.237538345843194, 0.207025782932360, 0.181827777110537, 0.160802931944560])
        
        p = (1+(self.gamma-1)/2*ma**2)**((-self.gamma)/(self.gamma-1))
        rho = (1+(self.gamma-1)/2*ma**2)**((-1)/(self.gamma-1))
        T = (1+(self.gamma-1)/2*ma**2)**(-1) 

        if self.type==3:
            p[-9:] = (1+(self.gamma-1)/2*ma[-9:]**2)**((-self.gamma)/(self.gamma-1))*0.6784
            rho[-9:] = (1+(self.gamma-1)/2*ma[-9:]**2)**((-1)/(self.gamma-1))*0.6784
        
        self.rho_pre=rho
        self.p_pre=p
        self.T_pre=T
        self.Ma_pre=ma
        self.x_pre=x

        return x,rho,p,T,ma

    def plot(self):
        font = {'family':'Times New Roman',
        'color':'darkred',
        'weight':'900',
        'size':12
        }

        plt.figure(1)
        plt.plot(self.x,self.rho[-1,:])
        plt.scatter(self.x_pre,self.rho_pre,c='r')
        plt.ylabel('$ \\rho $',fontsize=8)
        plt.xlabel('$x$',fontsize=8)
        plt.title('$\\rho-x$',fontdict=font)

        plt.figure(2)
        plt.plot(self.x,self.p[-1,:])
        plt.scatter(self.x_pre,self.p_pre,c='r')
        plt.ylabel('$ p $',fontsize=8)
        plt.xlabel('$x$',fontsize=8)
        plt.title('$p-x$',fontdict=font)

        plt.figure(3)
        plt.plot(self.x,self.T[-1,:])
        plt.scatter(self.x_pre,self.T_pre,c='r')
        plt.ylabel('$ T $',fontsize=8)
        plt.xlabel('$x$',fontsize=8)
        plt.title('$T-x$',fontdict=font)

        plt.figure(4)
        plt.plot(self.x,self.Ma[-1,:])
        plt.scatter(self.x_pre,self.Ma_pre,c='r')
        plt.ylabel('$ Ma $',fontsize=8)
        plt.xlabel('$x$',fontsize=8)
        plt.title('$Ma-x$',fontdict=font)

        plt.show()


    def ani(self):
        1
                
    ''' def solve1(self,A):
        temp = 1
        delta = 1
        while(delta>1e-5):
            fx=A**2-1/temp**2*(2/2.4*(1+0.2*temp**2))**6
            dfx=-1/1.2**6*(6*(1+0.2*temp**2)**5*temp-2*(1+0.2*temp**2)**6)/temp**3
            x = temp-fx/dfx
            delta = np.abs(x-temp)
            temp=x
        
        return temp '''
              