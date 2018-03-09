#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:45:37 2018

@author: canevean
"""

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

###############################################################################
# Fonction d'evolution de la voiture : X_dot = f(X,U)
# Vecteur d'état   : X=[x, y, theta, v, delta]
# Vecteur d'entrée : U=[u1, u2]
def car_dyn(X, U):
    
    # TODO
 
    return [ X[3]*np.cos( X[2] + X[4]), X[3]*np.sin( X[2] + X[4]), -0.30, u[0], u[1]]

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

    # Affichage de la position initial de la voiture (exemple) 
    """- A mettre en commentaire pour faire tourner EULER """
    print("Estimation position à t=0")
    d_0 = Y_0[0]                # distance du mobile / à la forme 
    car.draw(X_0, d_0, track)   # Pour dessiner la petite voiture et le polygone
    pl.show()                   # Pour afficher l'ensemble (pas necessairement besoin mais on ne sais jamais)
    
    # Simulation Euler ou/et RK2
    # Conditions initiales
    tmin = 0.0
    tmax = 40.0
    L = 3
    d = Y_0[0]
    h = 0.05
    t = np.arange(tmin, tmax, h)
    Xc = np.zeros( len(t) )
    Yc = np.zeros( len(t) )
    teta = np.zeros( len(t) )
    vitesse = np.zeros( len(t) )
    delta = np.zeros( len(t) )
    u=U_0
    Xc[0] = X_0[0]
    Yc[0] = X_0[1]
    teta[0] = X_0[2]
    vitesse[0] = X_0[3]
    delta[0] = X_0[4]
    
    for i in range( len(t) - 1) :
        
        vecteur = np.array([ Xc[i], Yc[i], teta[i], vitesse[i], delta[i]])
        vecteur = vecteur.reshape(( 5, 1))
        
        d = observation_func( vecteur, track)[0]
        u[0] = observation_func( vecteur, track)[1]
        u[1] = observation_func( vecteur, track)[2]

        
        Xc[i+1] = Xc[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[0]
        Yc[i+1] = Yc[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[1]
        teta[i+1] = teta[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[2]
        vitesse[i+1] = u[0]
        delta[i+1] = u[1]
    
        car.draw(vecteur, d, track)   # Pour dessiner la petite voiture et le polygone
        pl.plot(Xc, Yc)
        pl.show()
