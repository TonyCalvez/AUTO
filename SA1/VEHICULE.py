# -*- coding: utf-8 -*-
import car          # module pour afficher la petite voiture
import numpy as np  # module pour la manipulation de matrice
import pylab as pl  # pour la manipulation graphique

""" 
# BE Voiture
# Simulation d'un vehicule simple autour d'un Polygone SANS Régulation
# Vecteur d'état du modele vehicule  : X = [x, y, theta, v, delta] Vecteur colonne
# Vecteur consigne pour le véhicule  : U = [u1, u2]                Vecteur colonne
# Equation d'évolution du vehicule   : car_dyn(X, U)
# Equation d'observation du véhicule : observation_func(X, track) (donné dans le code)
# Vecteur d'observation pour le vehicule : Y = observation_func(X, track) = [d, v, delta]
"""

def methode_RK(t,X0, h, longueur, U0):
    #CONDITION INITIALES    
    for i in range(t):
        X0[:, i+1] = X0[:, i] + h*car_dyn(X0[:, i], U0, longueur) #euler
       # X[:, i+1] = X[:, i] + h*car_dyn(X[:, i] + h/2*car_dyn( X[ :, i], U0, longueur), U0, longueur)
        
    return X   
    
###############################################################################
# Fonction d'evolution de la voiture : X_dot = f(X,U)
# Vecteur d'état   : X=[x, y, theta, v, delta]
# Vecteur d'entrée : U=[u1, u2]
def car_dyn(X, U, longueur):
    sh=X.shape
    X=X.flatten() #x ne sera pas remplis de 0
    xdot=[[X[3]*np.cos(X[4])*np.cos(X[2])],
          [X[3]*np.cos(X[4])*np.sin(X[2])],
          [X[3]*(1/longueur)*np.sin(X[4])],
          [U[0]],
          [U[1]]] # xpoint
 

    return np.array(xdot).reshape(sh)

#####################
# Fonction d'observation de la voiture (NE PAS MODIFIER)
# Vecteur Y : [d,v,delta]
def observation_func(X, track):
    X = X.flatten()
    d = car.dist_to_track(X, track)
    return np.array([[d], [X[3]], [X[4]]]) # Vecteur colonne (ecriture bourrin - on formate à la main - plus mieux avec reshape() )

## ############################################################################    
# methode main pour tester notre code
if __name__ == "__main__":
    print("Test du modele voiture")

    # Track (Coordonnées de la forme autour duquelle doit tourner la voiture)
    track = np.array([[-10,-12,-10,0,10,20,32,35,30,20,0,-10],
                  [-5,0,5,15,20,20,15,10,0,-3,-6,-5]])
                  
    # Conditions initiales pour la simulation du mobile
    X_0 = np.array([-15.0, 0.0, np.pi/2.0, 7.0, -0.15])   # Etat initial du véhicule [x,y,theta,v,delta]  
    X_0 = X_0.reshape((5,1)) # Vecteur colonne !                                 
    U_0 = np.array([0.0, 0.0])                            # Consigne initiale U pour le mobile [u1,u2]
    U_0 = U_0.reshape((2,1)) # Vecteur colonne !
    Y_0 = observation_func(X_0, track)                    # Observation initiale du mobile à t=0
    print('X_0 : \n', X_0, '\nU_0 : \n ', U_0, '\nY_0 : \n', Y_0)

    matricejacob=np.array([[1, 0, 0, 0], [0, 0, 1, 0]])
    t=20
    h=0.05
    longueur=3
    for i in range( 0, 10, 2 ) :         
    #METHODE FONCTION AVEC MATRICE JACOBIENNE
        X=methode_RK(t, X_0, h, longueur, U_0)   
        print("Estimation position à t=0")
        # Affichage de la position initial de la voiture (exemple) 
        """- A mettre en commentaire pour faire tourner EULER """
        d_0 = Y_0[0]                # distance du mobile / à la forme 
        car.draw(X_0, d_0, track)   # Pour dessiner la petite voiture et le polygone
        pl.show()                   # Pour afficher l'ensemble (pas necessairement besoin mais on ne sais jamais)


    