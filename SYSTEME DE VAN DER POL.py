import numpy as np
import matplotlib.pyplot as plt


#def f(x,u): 
    #alpha=0.1
    #Xdot = (x[2] + alpha*((x[0]**2) − 1)*x[1] + x[0])
    #return np.array(Xdot)

def f( x, u, entreetype) :
    if entreetype == "lineaire" :
        coeff=(x[0], x[1])
        fonctionlinearise=np.dot(matricejacob,coeff)
        return np.array(fonctionlinearise)
    else :
        coeff=(x[0], x[1])
        fonctionlinearise=np.dot(matricejacob,coeff)
        return np.array(fonctionlinearise)

#METHODE RK2 - Runge Kutta
def methode_RK(t,X0, h, entreetype):
    #CONDITION INITIALES
    u=0
    X=np.zeros((len(X0), len(t)),'float')
    X[:,0]=X0
    
    for i in range( 0, len(t)-1):
        X[:, i+1] = X[:, i] + h*f(X[:, i] + h/2*f( X[ :, i], u, entreetype), u, entreetype)
        
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
    
    X0=np.array([ 0.1 , 0]) # Valeur initiale de X0
    
    #PARAMETRE DE SIMULATION
    x0_0 = 0.1
    x1_0 = 0
    h = 0.05
    duree = 20.0
    
    matricejacob=np.array([[0, 1], [-1, 1]])
    
    t=np.arange( 0.0, duree, h)
    print("taille: ", len(t),"duree: ", t[-1])

    for i in range( 0, 10, 2 ) :         
        #METHODE FONCTION AVEC MATRICE JACOBIENNE
        X=methode_RK(t, X0, h, "lineaire")   
        creationgraphique(t, X[1], 4, "Vitesse à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Temps", "Vitesse","1")
        creationgraphique(t, X[0], 5, "Position à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Temps", "Position", "2")
        creationgraphique(X[0], X[1], 6, "Phase à partir de la fonction linéarisée avec la méthode de RUNGE KUTTA", "Distance", "Vitesse", "3")
        
        #METHODE FONCTION AVEC LA FONCTION INITIALE
        X=methode_RK(t, X0, h, "dynamique") 
        creationgraphique(t, X[1], 4, "Vitesse à partir de la fonction dynamique avec la méthode de RUNGE KUTTA", "Temps", "Vitesse","1")
        creationgraphique(t, X[0], 5, "Position à partir de la fonction dynamique avec la méthode de RUNGE KUTTA", "Temps", "Position", "2")
        creationgraphique(X[0], X[1], 6, "Phase à partir de la fonction dynamique avec la méthode de RUNGE KUTTA", "Distance", "Vitesse", "3")
    
    #RESULTATS
print(t,",",X0)


##MAIN
#if __name__ == "__main__":
#    #valeurspropres = np.eigh(systemelinearise)
#    #print valeurspropres
#    # Conditions initiales
#    x0_0 = 0.1
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
