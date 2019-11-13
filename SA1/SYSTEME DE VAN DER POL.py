import numpy as np
import matplotlib.pyplot as plt


#def f(x,u): 
    #alpha=0.1
    #Xdot = (x[2] + alpha*((x[0]**2) − 1)*x[1] + x[0])
    #return np.array(Xdot)

def f( x, u, entreetype) :
    coeff = np.array( [x[0], x[1]])
    fonctionlinearise = np.dot( matricejacob, coeff)
    return np.array( fonctionlinearise)

def f2( x, u, entreetype) :
    return -(x[0]**2 - 1)*x[1] - x[0]

#METHODE RK2 - Runge Kutta
def methode_RK(t,X0, h, entreetype):
    #CONDITION INITIALES
    u=0
    X=np.zeros(len(t),'float')
    X[0]=X0[0]
    
    vitesse=np.zeros(len(t),'float')
    vitesse[0]=X0[1]
    
    for i in range( 0, len(t)-1):
        vitesse[i+1] = vitesse[i] + h*f( [ X[i], vitesse[i]], u, entreetype)[1]
        
        X[i+1] = X[i] + h*f( [ X[i], vitesse[i]], u, entreetype)[0]
        
    return X, vitesse

def methode_Euler(t,X0, h, entreetype):
    #CONDITION INITIALES
    u=0
    M=np.zeros(len(t),'float')
    Xdot=np.zeros(len(t),'float')

    M[0] = x0_0
    Xdot[0] = x1_0

    
    for i in range( 0, len(t)-1):
        Xdot[i+1] = Xdot[i] + h*f2( [M[i], Xdot[i]], u, entreetype)
        M[i+1] = M[i] + h*( Xdot[i])
    return M, Xdot

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
    
    X0=np.array([ 0.1 , 0]) # Valeur initiale de X0
    
    #PARAMETRE DE SIMULATION
    x0_0 = 0.1
    x1_0 = 0
    h = 0.05
    duree = 20.0
    
    matricejacob=np.array([[0, 1], [-1, 1]])
    
    t=np.arange( 0.0, duree, h)
    print("taille: ", len(t),"duree: ", t[-1])

       
    #METHODE FONCTION AVEC MATRICE JACOBIENNE
    Z=methode_RK(t, X0, h, "lineaire")   
    creationgraphique(t, Z[1], 1, "Vitesse à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Temps", "Vitesse","LINEAIRE")
    creationgraphique(t, Z[0], 2, "Position à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Temps", "Position", "LINEAIRE")
    creationgraphique(Z[0], Z[1], 3, "Phase à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Distance", "Vitesse", "LINEAIRE")
        
    #METHODE FONCTION AVEC LA FONCTION INITIALE
    Y=methode_Euler(t, X0, h, "dynamique") 
    creationgraphique(t, Y[1], 1, "Vitesse à partir de la fonction dynamique avec la méthode linéarisée", "Temps", "Vitesse","DYNAMIQUE")
    creationgraphique(t, Y[0], 2, "Position à partir de la fonction dynamique avec la méthode linéarisée", "Temps", "Position","DYNAMIQUE")
    creationgraphique(Y[0], Y[1], 3, "Phase à partir de la fonction dynamique avec la méthode linéarisé", "Distance", "Vitesse","DYNAMIQUE")
    
    #RESULTATS
print(t,",",X0)


##MAIN
#if __name__ == "__main__":
#    #valeurspropres = np.eigh(systemelinearise)
#    #print valeurspropres
#    # Conditions initiales
#    x0_0 = 0.1vitesse
#    x1_0 = 0
#    x = np.arange(0, 10, 1)
#    X1dot = np.arange(0, 10, 1)
#    X2dot = np.arange(0, 10, 1)
#    for i in range(0, len(x) - 1) :
#        X1dot[i] = fonction([x[i], X1dot[i-1]])[0]
#        X2dot[i] = fonction([x[i], X1dot[i-1]])[1]
#    
#    plt.figure()
#    plt.plot( x, X2dot)
#    plt.show()
