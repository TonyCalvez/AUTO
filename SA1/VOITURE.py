#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import car          # module pour afficher la petite voiture
import numpy as np  # module pour la manipulation de matrice
import pylab as pl  # pour la manipulation graphique
import scipy.signal as spy
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

def car_dyn(x, u):
    L_car=3
    sh=x.shape
    x=x.flatten() #x ne sera pas remplis de 0
    xdot=[[x[3]*np.cos(x[4])*np.cos(x[2])],
          [x[3]*np.cos(x[4])*np.sin(x[2])],
          [x[3]*(1/L_car)*np.sin(x[4])],
          [u[0]],
          [u[1]]] # xpoint
    return np.array(xdot).reshape(sh) #XDOT




def regul_dyn(xreg,y,w):

    A=np.array([[0, 7, 0, 0], [0, 0, 0, 7/3], [0,0,0,0], [0,0,0,0]])
    B=np.array([[0,0],[0,0],[1,0],[0,1]])
    C=np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0,0,0,1]])
    D=np.array([[0,0],[0,0],[0,0]])
    
    Pobs=[-2.01,-2.02,-2.03,-2.04]
    Pcom=[-2,-1.01,-1.02,-1.03]
    
    res = spy.place_poles(A, B, Pcom) 
    K= res.gain_matrix
    
    res2 = spy.place_poles(A.T, C.T, Pobs)
    L= (res2.gain_matrix).T
    
    E=np.array([[1, 0, 0, 0], [0, 0, 1, 0]])
    
    H = -E(((A-B*K)**-1)*B)**-1
    
    ytilde=y-np.array([5],[7],[0])

    wtilde=w-np.array([5],[7])

    Xchap_dot=(A-L*C-B*K)*xchap+L*ytilde+B*H*wtilde
    
    return Xchap_dot

#####################
# Fonction d'observation de la voiture (NE PAS MODIFIER)
# Vecteur Y : [d,v,delta]
def observation_func(X, track):
    X = X.flatten()
    d = car.dist_to_track(X, track)
    return np.array([[d], [X[3]], [X[4]]]) # Vecteur colonne (ecritucfre bourrin - on formate à la main - plus mieux avec reshape() )

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
        
#        vecteur = np.array([ Xc[i], Yc[i], teta[i], vitesse[i], delta[i]])
#        vecteur = vecteur.reshape(( 5, 1))
#        
#        d = observation_func( vecteur, track)[0]
#        u[0] = observation_func( vecteur, track)[1]
#        u[1] = observation_func( vecteur, track)[2]
#
#        
#        Xc[i+1] = Xc[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[0]
#        Yc[i+1] = Yc[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[1]
#        teta[i+1] = teta[i] + h*car_dyn( [Xc[i], Yc[i], teta[i], vitesse[i], delta[i]], u)[2]
#        vitesse[i+1] = u[0]
#        delta[i+1] = u[1]
    
        
        X_0[0]=X_0[0] + h.car_dyn(X_0[0],u)
        y=observation_func(X_0[0], track)
        
        #REGULATION
        xreg=xreg+h.regul_dyn(xreg,y,w)
        
        
        
        car.draw(vecteur, d, track)   # Pour dessiner la petite voiture et le polygone
        pl.show()
