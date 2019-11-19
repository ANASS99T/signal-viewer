import numpy as np
import matplotlib.pyplot as plt

# deffenir une classe :
class td1() :
   # def __init__(self): # ligne obligatoire
    def __init__(self, parent=None):   
        self.trace_TD1()

    def trace_TD1(self):
        T = np.linspace(0,9,1000)
        F = self.X(T)
        plt.figure()
        plt.axhline(color='black')
        plt.axvline(color='black')
        plt.plot(T,F[0], ls='--', label="x(t)", c="green")
        plt.plot(T,F[1], ls='-', label="y(t)", c="blue")
        plt.legend()
        plt.show()


    def R(self,t):
        if(t < 0):
            r = 0
        else:
            r = t
        return(r)

    def X(self,t):
        x=[]
        y=[]
        i=0
        Ak=[1, -2, 1, -1, 1]
        Tk=[0, 3, 4, 6, 8]

        for j in t:
            s1 = 0
            s2 = 0
            for i in range(5):
                s1 += (Ak[i]*self.R(j-Tk[i]))
                s2 += (Ak[i]*self.R((-4*j)+8-Tk[i]))
            x.append(s1)
            y.append(s2)

        return [x,y]
    

        
  
class R:
    def __init__(self, parent = None):
        self.graphe_R(self.Ramp,"la rampe unitaire",-10,10)

    def Ramp(self,t):
        if(t < 0):
            r = 0
        else:
            r = t
        return(r)
    def graphe_R(self,f,nom,vi,vf):
        t = np.linspace(vi,vf,1000)
        x = [f(i) for i in t]
        plt.figure()
        plt.plot(t,x)
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title(nom) # titre du graphe
        plt.show()

class U:
    def __init__(self, parent = None):
        self.graphe_R(self.Unite,"L’échelon unité",-10,10)

    def Unite(self,t):
        if( t < 0):
            u = 0
        else:
            u = 1
        return(u)
    def graphe_R(self,f,nom,vi,vf):
        t = np.linspace(vi,vf,1000)
        x = [f(i) for i in t]
        plt.figure()
        plt.plot(t,x)
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title(nom) # titre du graphe
        plt.show()

class Sgn:
    def __init__(self, parent = None):
        self.graphe_R(self.sgn,"La fonction signe",-10,10)

    def sgn(self,t):
        if(t > 0):
            sgn = 1
        elif(t < 0):
            sgn = -1
        else:
            sgn = 0
        return(sgn)
    def graphe_R(self,f,nom,vi,vf):
        t = np.linspace(vi,vf,1000)
        x = [f(i) for i in t]
        plt.figure()
        plt.plot(t,x)
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title(nom) # titre du graphe
        plt.show()

class Rect:
    def __init__(self, parent = None):
        self.graphe_R(self.rect,"Signal rectangulaire",-10,10)

    def rect(self,t):
        if(np.abs(t) <= 1/2):
            rect = 1
        else:
            rect = 0
        return(rect)
    def graphe_R(self,f,nom,vi,vf):
        t = np.linspace(vi,vf,1000)
        x = [f(i) for i in t]
        plt.figure()
        plt.plot(t,x)
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title(nom) # titre du graphe
        plt.show()


class Tri:
    def __init__(self, parent = None):
        self.graphe_R(self.tri,"Signale triangulaire",-10,10)

    def tri(self,t):
        if( np.abs(t) <= (1/2)):
            tri = 1-(2*np.abs(t))
        else:
            tri = 0
        return (tri)

    def graphe_R(self,f,nom,vi,vf):
        t = np.linspace(vi,vf,1000)
        x = [f(i) for i in t]
        plt.figure()
        plt.plot(t,x)
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title(nom) # titre du graphe
        plt.show()



class exo3_td2:
    def __init__(self, parent = None):
        T = np.linspace(-5,5,10000)
        plt.figure()
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.subplot(2,2,1)
        plt.title("X31")
        plt.plot(T,self.X31(T))
        plt.subplot(2,1,2)
        plt.title("X32")
        plt.plot(T,self.X32(T))
        plt.subplot(2,2,2)
        plt.title("X34")
        plt.plot(T,self.X34(T))
        plt.show()



    def X31(self,T):
        s=[]
        for t in T :
            s.append(np.sin(t)**2)
        
        return s

    def X32(self,T):
        s=[]
        for t in T:
            s.append((-2*np.cos(12*np.pi*t)) + (3*np.sin(18*np.pi*t+np.pi/6)) - 1)
        
        return s
    def X34(self,T):
        s = []
        for t in T :
            if t >= 0 or t <= 2:
                s.append(np.sin(np.pi*t))
            elif t >= 2 or t <=4:
                s.append(0)
       
        return s


class exo2_td2:
    def __init__(self, parent = None):
        T = np.linspace(-5,5,10000)
        plt.figure()
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.subplot(2,2,1)
        plt.title("X1")
        plt.plot(T,self.X1(T))
        plt.subplot(2,1,2)
        plt.title("X")
        plt.plot(T,self.X(T))
        plt.subplot(2,2,2)
        plt.title("X2")
        plt.plot(T,self.X2(T))
        plt.show()
    def X1(self,T):
        s=[]
        for t in T:
            a0 = 1/2
            an = 0
            for i in range(1,100):
                if i % 2 == 0:
                    an += ((3/(i*np.pi)**2)-(1/(i*np.pi)**2)) * np.cos(i*np.pi*t)
                else:
                    an += ((-3/(i*np.pi)**2)-(1/(i*np.pi)**2)) * np.cos(i*np.pi*t)
            s.append(a0+an)
        return s

    def X2(self,T):
        s=[]
        for t in T:
            a0 = 0
            an = 0
            for i in range(1,100):
                if i % 2 != 0 :
                    an += (4* np.sin(i * np.pi *t)/(np.pi*i))
                else :
                    continue
            s.append(a0+an)
        return s

    def X(self,T):
        s=[]
        x1 = self.X1(T)
        x2 = self.X2(T)
        for i , j in zip(x1, x2):
            s.append(i+j)
        return s

class exo1_td2:
    def __init__(self, parent = None):
        T = np.linspace(-10,10,10000)
        plt.figure()
        plt.axhline(color = 'k') # le couleur de l'axe t est noire
        plt.axvline(color = 'k') # le couleur de l'axe x est noire
        plt.axis("equal") #l’axe des abscisses = l’axe des ordonnées
        plt.title("exo 1 td 2")
        plt.plot(T,self.S(T))       
        plt.show()

    def S(self,T):
        s=[]
        for t in T:
            a0 = 5
            an = 0
            for i in range(1,50):
                if i % 2 != 0 :
                    an += (-40/(np.pi*i)**2) * np.cos(i * ((np.pi)/2)*t)
                else :
                    continue
            s.append(a0+an)
        return s

