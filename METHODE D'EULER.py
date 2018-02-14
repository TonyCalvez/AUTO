import numpy as np

#EQUATION D'EVOLUTION
def f(x,u):
    m=1.0
    g=9.81
    l=2.0
    mu=0.1
    
    Xdot =   [ x[1], -g*np.sin( x[0] )/l - mu*x[1]/(m*l**2) + u/(m*l**2) ]
    return np.array(Xdot)

#METHODE D'EULER
def methode_euler(t,Xo):
    for i in range( 0, 10 ):
        X[i+1] = X[i] + h*f( X, u)
        
        
        
#MAIN
if __name__ == "__main__":
    print("Test Modele")
    
    #CONDITION INITIALES
    X_0=
    
    #PARAMETRE DE SIMULATION
    h=
    duree=
    t=np.arange(0.0, duree,h)
    print("taille: ", len(t),"duree: ", t[-1])

    #METHODE EULER
    X_euler=methode_euler(t, Xo)
    
    #RESULTATS
    print(t,X_0)
