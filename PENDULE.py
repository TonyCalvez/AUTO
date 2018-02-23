import numpy as np
import matplotlib.pyplot as plt
    
#EQUATION D'EVOLUTION -> avec x qui est un tableau à deux dimensions : x1 , x2 et u est l'entrée
def f(x,u): 
    m=1.0
    g=9.81
    l=2.0
    
    Xdot =   [x[1], -g*np.sin( x[0] )/l - mu*x[1]/(m*l**2) + u/(m*l**2) ]
    return np.array(Xdot)

#METHODE D'EULER
def methode_euler(t,X0, h):
    #CONDITION INITIALES
    u=0
    X=np.zeros((len(X0), len(t)),'float')
    X[:,0]=X0
    
    for i in range( 0, len(t)-1):
        X[:, i+1] = X[:, i] + h*f(X[:, i], u)
        
    return X


#METHODE RK2 - Runge Kutta
def methode_RK(t,X0, h):
    #CONDITION INITIALES
    u=0
    X=np.zeros((len(X0), len(t)),'float')
    X[:,0]=X0
    
    for i in range( 0, len(t)-1):
        X[:, i+1] = X[:, i] + h*f(X[:, i] + h/2*f( X[ :, i], u), u)
        
    return X

def creationgraphique(X, Y, graphiquenumero, titre, labelX, labelY, nomcourbe):  
    plt.figure(graphiquenumero)
    plt.plot(X, Y, label=nomcourbe)
    plt.title(titre)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.legend()
    plt.show()
        
#MAIN
if __name__ == "__main__":
    print("Test Modele")
    
    X0=np.array([ 1.0 , 0]) # Valeur initiale de X0
    
    #PARAMETRE DE SIMULATION
    h = 0.05
    duree = 20.0
    t=np.arange( 0.0, duree, h)
    print("taille: ", len(t),"duree: ", t[-1])

    for i in range( 0, 10, 2 ) :
        mu=i/10
        #METHODE EULER
        X=methode_euler(t, X0, h)   
        creationgraphique(t, X[1], 1, "Vitesse avec la méthode d'EULER", "Temps", "Vitesse", mu)
        creationgraphique(t, X[0], 2, "Position avec la méthode d'EULER", "Temps", "Position", mu)
        creationgraphique(X[0], X[1], 3, "Phase avec la méthode d'EULER", "Distance", "Vitesse", mu)
        
        #METHODE RUNGE KUTTA
        X=methode_RK(t, X0, h)   
        creationgraphique(t, X[1], 4, "Vitesse  avec la méthode de RUNGE KUTTA", "Temps", "Vitesse",mu)
        creationgraphique(t, X[0], 5, "Position  avec la méthode de RUNGE KUTTA", "Temps", "Position", mu)
        creationgraphique(X[0], X[1], 6, "Phase  avec la méthode de RUNGE KUTTA", "Distance", "Vitesse", mu)
        # mu élevé pour Euler et mu faible pour Runge Kuta
    
    #RESULTATS
print(t,",",X0)
