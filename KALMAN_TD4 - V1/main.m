dt = 0.01;
t=0;
x=[0;0;0;4;0.1]; 
% //Vitesse initale à 0.5 et angle de volant à 0.1
u=[0;0];

while(t < 30)
    
    alphatheta = mvnrnd(0,0.01 * dt);
    alphav     = mvnrnd(0,0.01 * dt);
    alphadelta = mvnrnd(0,0.01 * dt);
    
    x = x + dt * f(x,u)+ [0; 0; alphatheta; alphav; alphadelta];
    
    clf;
    hold on;
    axis([-20 20 -20 20]);
    axis square;
    draw(x, u);
    pause(dt);
    t=t+dt;
    
end