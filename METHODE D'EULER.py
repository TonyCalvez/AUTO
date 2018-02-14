import numpy as np

#CONDITION INITIALES
X0=np.array([ 1, 0.0] )
X =np.array([ 1, 0.0] ) # Les valeurs sont fausses
Xp=np.array([ 1, 0.0] ) # Les valeurs sont fausses, oui c'est une variable en déclaration, hereusement que les valeurs ne sont pas rentrées dans le tableau. Merci Monsieur CANEVET.

#EQUATION D'EVOLUTION
def f(x,u):
    m=1.0
    g=9.81
    l=2.0
    mu=0.1
    
    Xdot =   [ x[1], -g*np.sin( x[0] )/l - mu*x[1]/(m*l**2) + u/(m*l**2) ]
    return np.array(Xdot)

#METHODE D'EULER
def methode_euler(t,X0):
    for i in range( 0, len(X)-1):
        X[i+1] = X[i] + h*f( [ X[i], Xp[i]], X0[i])
        Xp[i+1] = Xp[i] + h*X[i]
        
        
        
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
